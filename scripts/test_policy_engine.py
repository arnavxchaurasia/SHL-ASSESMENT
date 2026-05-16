from pprint import pprint

from app.agent.frame_extractor import (
    ConversationFrameExtractor,
)

from app.agent.policy_engine import (
    PolicyEngine,
)


messages = [
    {
        "role": "user",
        "content": (
            "Hiring graduate management trainees "
            "for high volume campus hiring "
            "with leadership potential"
        ),
    }
]

extractor = (
    ConversationFrameExtractor()
)

frame = extractor.extract(messages)

policy_engine = PolicyEngine()

policy = policy_engine.build_policy(
    frame
)

pprint(frame)
print()
pprint(policy)