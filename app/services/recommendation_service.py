from app.agent.frame_extractor import (
    ConversationFrameExtractor,
)

from app.agent.hiring_intent_inferencer import (
    HiringIntentInferencer,
)

from app.agent.policy_engine import (
    PolicyEngine,
)

from app.agent.battery_planner import (
    BatteryPlanner,
)

from app.agent.refinement_engine import (
    RefinementEngine,
)

from app.agent.skill_canonicalizer import (
    SkillCanonicalizer,
)

from app.agent.domain_router import (
    DomainRouter,
)

from app.retrieval.hybrid_ranker import (
    HybridRetriever,
)

from app.retrieval.filters import (
    skill_overlap_score,
)

from app.retrieval.category_mapper import (
    infer_assessment_category,
    infer_semantic_family,
)

from app.services.explanation_service import (
    ExplanationService,
)

from app.services.battery_coherence_service import (
    BatteryCoherenceService,
)


class RecommendationService:
    def __init__(self):
        self.frame_extractor = (
            ConversationFrameExtractor()
        )

        self.intent_inferencer = (
            HiringIntentInferencer()
        )

        self.policy_engine = (
            PolicyEngine()
        )

        self.battery_planner = (
            BatteryPlanner()
        )

        self.refinement_engine = (
            RefinementEngine()
        )

        self.skill_canonicalizer = (
            SkillCanonicalizer()
        )

        self.domain_router = (
            DomainRouter()
        )

        self.retriever = HybridRetriever()

        self.explanation_service = (
            ExplanationService()
        )

        self.battery_coherence_service = (
            BatteryCoherenceService()
        )

    def recommend(
        self,
        messages,
        top_k=10,
    ):
        # =========================
        # CONTEXT EXTRACTION
        # =========================
        frame = (
            self.frame_extractor.extract(
                messages
            )
        )

        # =========================
        # HIRING INTENT
        # =========================
        intent = (
            self.intent_inferencer.infer(
                frame
            )
        )

        # =========================
        # REFINEMENT DETECTION
        # =========================
        latest_message = messages[-1][
            "content"
        ]

        refinement = (
            self.refinement_engine
            .detect_refinement(
                latest_message
            )
        )

        # =========================
        # POLICY GENERATION
        # =========================
        policy = (
            self.policy_engine.build_policy(
                frame
            )
        )

        # =========================
        # DOMAIN ROUTING
        # =========================
        domain_config = (
            self.domain_router
            .get_domain_config(
                frame
            )
        )

        boost_keywords = (
            domain_config[
                "boost_keywords"
            ]
        )

        suppress_keywords = (
            domain_config[
                "suppress_keywords"
            ]
        )

        # =========================
        # BATTERY PLANNING
        # =========================
        battery_plan = (
            self.battery_planner.build_plan(
                frame,
                intent,
                policy,
                refinement,
            )
        )

        # =========================
        # SEARCH QUERY BUILDING
        # =========================
        query_parts = []

        canonical_skills = (
            self.skill_canonicalizer
            .canonicalize(
                frame.technical_skills
            )
        )

        query_parts.extend(
            canonical_skills
        )

        query_parts.extend(
            frame.behavioral_requirements
        )

        if frame.seniority:
            query_parts.append(
                frame.seniority
            )

        if frame.role_family:
            query_parts.append(
                frame.role_family
            )

        # =========================
        # PERSONALITY ENRICHMENT
        # =========================
        if (
            policy.prefer_personality
            or refinement.get(
                "add_personality",
                False,
            )
        ):
            query_parts.append(
                "personality leadership behavior"
            )

        # =========================
        # COGNITIVE ENRICHMENT
        # =========================
        if (
            policy.prefer_cognitive
            or refinement.get(
                "add_cognitive",
                False,
            )
        ):
            query_parts.append(
                "cognitive reasoning aptitude"
            )

        # =========================
        # LEADERSHIP REFINEMENT
        # =========================
        if refinement.get(
            "focus_leadership",
            False,
        ):
            query_parts.append(
                "leadership executive potential"
            )

        # =========================
        # SIMULATION ENRICHMENT
        # =========================
        if policy.prefer_simulation:
            query_parts.append(
                "simulation situational judgment"
            )

        search_query = " ".join(
            query_parts
        )

        # =========================
        # HYBRID RETRIEVAL
        # =========================
        retrieval_results = (
            self.retriever.hybrid_search(
                search_query,
                top_k=25,
            )
        )

        # =========================
        # POLICY-AWARE RERANKING
        # =========================
        scored_results = []

        for result in retrieval_results:
            item = result["item"]

            final_score = result["score"]

            overlap = (
                skill_overlap_score(
                    item,
                    canonical_skills,
                )
            )

            final_score += (
                overlap * 2
            )

            test_types = item.get(
                "test_types",
                []
            )

            item_name = item.get(
                "name",
                ""
            )

            lower_name = (
                item_name.lower()
            )

            # =====================
            # DOMAIN BOOSTING
            # =====================
            for keyword in (
                boost_keywords
            ):
                if keyword in lower_name:
                    final_score += 1.5

            # =====================
            # DOMAIN SUPPRESSION
            # =====================
            for keyword in (
                suppress_keywords
            ):
                if keyword in lower_name:
                    final_score -= 3.0

            # =====================
            # MODERN TECH BOOST
            # =====================
            modern_keywords = [
                "react",
                "javascript",
                "angular",
                "cloud",
                "kubernetes",
                "docker",
                "microservices",
                "api",
                "spring",
            ]

            for keyword in (
                modern_keywords
            ):
                if keyword in lower_name:
                    final_score += 0.7

            # =====================
            # HARD NOISE FILTER
            # =====================
            if final_score < -1:
                continue

            # =====================
            # PERSONALITY BOOST
            # =====================
            if (
                policy.prefer_personality
                and "P" in test_types
            ):
                final_score += 1.5

            # =====================
            # COGNITIVE BOOST
            # =====================
            if (
                policy.prefer_cognitive
                and "A" in test_types
            ):
                final_score += 1.2

            # =====================
            # SIMULATION BOOST
            # =====================
            if (
                policy.prefer_simulation
                and "S" in test_types
            ):
                final_score += 1.0

            # =====================
            # SCALABLE SCREENING
            # =====================
            if (
                intent.needs_scalable_screening
                and (
                    "verify" in lower_name
                    or "interactive"
                    in lower_name
                )
            ):
                final_score += 0.8

            # =====================
            # LEADERSHIP PIPELINE
            # =====================
            if (
                intent.leadership_pipeline
                and (
                    "leadership"
                    in lower_name
                    or "opq"
                    in lower_name
                )
            ):
                final_score += 1.2

            # =====================
            # LEADERSHIP REFINEMENT
            # =====================
            if (
                refinement.get(
                    "focus_leadership",
                    False,
                )
                and (
                    "leadership"
                    in lower_name
                    or "hipo"
                    in lower_name
                )
            ):
                final_score += 0.8

            scored_results.append(
                {
                    "score": final_score,
                    "item": item,
                }
            )

        # =========================
        # SORT RESULTS
        # =========================
        scored_results = sorted(
            scored_results,
            key=lambda x: x["score"],
            reverse=True,
        )

        # =========================
        # BATTERY CONSTRUCTION
        # =========================
        recommendations = []

        added_names = set()

        family_counts = {}

        MAX_FAMILY_LIMIT = 1

        MAX_PERSONALITY_ITEMS = 2

        # =========================
        # SLOT-BASED PLANNING
        # =========================
        for slot in battery_plan.slots:
            target_category = (
                slot.category
            )

            priority = (
                slot.priority
            )

            best_candidate = None

            best_score = -999

            for result in scored_results:
                item = result["item"]

                item_name = item.get(
                    "name",
                    ""
                )

                if item_name in added_names:
                    continue

                category = (
                    infer_assessment_category(
                        item
                    )
                )

                family = (
                    infer_semantic_family(
                        item
                    )
                )

                # =====================
                # CATEGORY MATCH
                # =====================
                if (
                    category
                    != target_category
                ):
                    continue

                # =====================
                # FAMILY DIVERSITY
                # =====================
                if (
                    family_counts.get(
                        family,
                        0,
                    )
                    >= MAX_FAMILY_LIMIT
                ):
                    continue

                # =====================
                # PRIORITY ANCHORING
                # =====================
                slot_bonus = 0

                if priority == "core":
                    slot_bonus = 2.0

                elif priority == "supporting":
                    slot_bonus = 1.0

                elif priority == "augment":
                    slot_bonus = 0.5

                adjusted_score = (
                    result["score"]
                    + slot_bonus
                )

                if (
                    adjusted_score
                    > best_score
                ):
                    best_candidate = item

                    best_score = (
                        adjusted_score
                    )

            # =====================
            # ADD BEST SLOT MATCH
            # =====================
            if best_candidate:
                recommendations.append(
                    best_candidate
                )

                added_names.add(
                    best_candidate[
                        "name"
                    ]
                )

                family = (
                    infer_semantic_family(
                        best_candidate
                    )
                )

                family_counts[
                    family
                ] = (
                    family_counts.get(
                        family,
                        0,
                    )
                    + 1
                )

        # =========================
        # CONSERVATIVE BACKFILL
        # =========================
        for result in scored_results:
            if (
                len(recommendations)
                >= top_k
            ):
                break

            item = result["item"]

            item_name = item.get(
                "name",
                ""
            )

            if item_name in added_names:
                continue

            family = (
                infer_semantic_family(
                    item
                )
            )

            if (
                family_counts.get(
                    family,
                    0,
                )
                >= MAX_FAMILY_LIMIT
            ):
                continue

            category = (
                infer_assessment_category(
                    item
                )
            )

            # =====================
            # PERSONALITY LIMIT
            # =====================
            personality_count = sum(
                1
                for recommendation
                in recommendations
                if (
                    infer_assessment_category(
                        recommendation
                    )
                    == "personality"
                )
            )

            if (
                category
                == "personality"
                and personality_count
                >= MAX_PERSONALITY_ITEMS
            ):
                continue

            recommendations.append(
                item
            )

            added_names.add(
                item_name
            )

            family_counts[
                family
            ] = (
                family_counts.get(
                    family,
                    0,
                )
                + 1
            )

        # =========================
        # BATTERY COHERENCE
        # VALIDATION
        # =========================
        recommendations = (
            self.battery_coherence_service
            .validate(
                recommendations
            )
        )

        # =========================
        # EXPLANATION ENRICHMENT
        # =========================
        enriched_recommendations = []

        for item in recommendations:
            explanation = (
                self.explanation_service
                .generate_explanation(
                    item,
                    frame,
                    intent,
                )
            )

            enriched_item = {
                **item,
                "explanation": explanation,
            }

            enriched_recommendations.append(
                enriched_item
            )

        return enriched_recommendations