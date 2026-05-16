from pprint import pprint

from app.services.orchestrator import Orchestrator


messages = [
    {
        "role": "user",
        "content": "Hiring a mid-level Java backend developer"
    },
    {
        "role": "assistant",
        "content": "Here are recommendations..."
    },
    {
        "role": "user",
        "content": "Actually add personality tests"
    }
]

orchestrator = Orchestrator()

result = orchestrator.process(messages)

pprint(result)