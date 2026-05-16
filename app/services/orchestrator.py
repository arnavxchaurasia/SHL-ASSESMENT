from app.agent.analyzer import (
    ConversationAnalyzer,
)

from app.agent.state_machine import (
    ConversationStateMachine,
)

from app.agent.llm_client import (
    LLMClient,
)

from app.services.recommendation_service import (
    RecommendationService,
)

from app.services.comparison_service import (
    ComparisonService,
)

from app.services.consultation_service import (
    ConsultationService,
)


class Orchestrator:
    def __init__(self):
        self.analyzer = (
            ConversationAnalyzer()
        )

        self.state_machine = (
            ConversationStateMachine()
        )

        self.recommendation_service = (
            RecommendationService()
        )

        self.comparison_service = (
            ComparisonService()
        )

        self.llm_client = (
            LLMClient()
        )

        self.consultation_service = (
            ConsultationService()
        )

    def process(
        self,
        messages,
        debug=False,
    ):
        # =========================
        # SAFETY CHECK
        # =========================
        if not messages:
            return {
                "reply": (
                    "Please provide a "
                    "message or hiring "
                    "requirement."
                ),
                "recommendations": [],
                "end_of_conversation": False,
            }

        latest_message = (
            messages[-1].get(
                "content",
                "",
            )
        )

        # =========================
        # ANALYZE CONVERSATION
        # =========================
        analysis = (
            self.analyzer.analyze(
                messages
            )
        )

        # =========================
        # DETERMINE STATE
        # =========================
        state = (
            self.state_machine.detect_state(
                messages,
                analysis,
            )
        )

        # =========================
        # CLARIFICATION FLOW
        # =========================
        if state == "CLARIFY":
            return {
                "reply": (
                    self._clarification_reply(
                        analysis
                    )
                ),
                "recommendations": [],
                "end_of_conversation": False,
            }

        # =========================
        # REFUSAL FLOW
        # =========================
        if state == "REFUSE":
            return {
                "reply": (
                    "I can only help with "
                    "SHL assessment "
                    "recommendations, "
                    "assessment comparisons, "
                    "and hiring evaluation "
                    "guidance."
                ),
                "recommendations": [],
                "end_of_conversation": False,
            }

        # =========================
        # COMPARISON FLOW
        # =========================
        if state == "COMPARE":
            comparison = (
                self.comparison_service.compare(
                    latest_message
                )
            )

            natural_reply = (
                self.llm_client.generate_comparison_reply(
                    comparison
                )
            )

            response = {
                "reply": natural_reply,
                "recommendations": [],
                "end_of_conversation": False,
            }

            if debug:
                response["debug"] = {
                    "state": state,
                    "comparison_query": (
                        latest_message
                    ),
                }

            return response

        # =========================
        # RECOMMENDATION FLOW
        # =========================
        recommendations = (
            self.recommendation_service.recommend(
                messages
            )
        )

        # =========================
        # DEBUG TRACE
        # =========================
        debug_trace = {}

        frame = (
            self.recommendation_service
            .frame_extractor.extract(
                messages
            )
        )

        intent = (
            self.recommendation_service
            .intent_inferencer.infer(
                frame
            )
        )

        policy = (
            self.recommendation_service
            .policy_engine.build_policy(
                frame
            )
        )

        domain_config = (
            self.recommendation_service
            .domain_router
            .get_domain_config(
                frame
            )
        )

        battery_plan = (
            self.recommendation_service
            .battery_planner
            .build_plan(
                frame,
                intent,
                policy,
                {},
            )
        )

        if debug:
            debug_trace = {
                "state": state,
                "frame": (
                    frame.__dict__
                ),
                "intent": (
                    intent.__dict__
                ),
                "policy": (
                    policy.__dict__
                ),
                "domain_route": (
                    domain_config
                ),
                "battery_plan": [
                    {
                        "category": (
                            slot.category
                        ),
                        "priority": (
                            slot.priority
                        ),
                    }
                    for slot
                    in battery_plan.slots
                ],
            }

        # =========================
        # FORMAT RESPONSE
        # =========================
        formatted_recommendations = []

        for item in recommendations:
            formatted_item = {
                "name": item.get(
                    "name",
                    "Unknown",
                ),
                "url": item.get(
                    "url",
                    "",
                ),
                "test_type": (
                    item.get(
                        "test_types",
                        ["Unknown"],
                    )[0]
                ),
                "explanation": item.get(
                    "explanation",
                    "",
                ),
            }

            formatted_recommendations.append(
                formatted_item
            )

        # =========================
        # CONSULTATIVE GUIDANCE
        # =========================
        follow_up_guidance = (
            self.consultation_service
            .generate_follow_up(
                frame,
                intent,
            )
        )

        # =========================
        # NATURAL RESPONSE
        # =========================
        natural_reply = (
            self.llm_client
            .generate_recommendation_reply(
                latest_message,
                formatted_recommendations,
            )
        )

        # =========================
        # CONSULTATIVE ENRICHMENT
        # =========================
        if follow_up_guidance:
            natural_reply += (
                "\n\n"
                + follow_up_guidance
            )

        # =========================
        # FINAL RESPONSE
        # =========================
        response = {
            "reply": natural_reply,
            "recommendations": (
                formatted_recommendations
            ),
            "end_of_conversation": True,
        }

        # =========================
        # DEBUG OUTPUT
        # =========================
        if debug:
            response["debug"] = (
                debug_trace
            )

        return response

    def _clarification_reply(
        self,
        analysis,
    ):
        # =========================
        # ROLE / DOMAIN UNCLEAR
        # =========================
        if not analysis.get(
            "tech_skills"
        ):
            return (
                "Could you specify the "
                "role, domain, or core "
                "skills you are hiring for?"
            )

        # =========================
        # SOFT FALLBACK
        # =========================
        return (
            "Could you provide a bit "
            "more detail about the "
            "hiring requirements or "
            "evaluation goals?"
        )