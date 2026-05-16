from pprint import pprint

from app.agent.frame_extractor import (
    ConversationFrameExtractor,
)


messages = [
    {
        "role": "user",
        "content": (
            "Hiring a mid-level Java backend "
            "developer with stakeholder communication "
            "for high volume campus hiring"
        ),
    }
]

extractor = ConversationFrameExtractor()

frame = extractor.extract(messages)

pprint(frame)