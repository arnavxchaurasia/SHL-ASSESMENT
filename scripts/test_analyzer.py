from app.agent.analyzer import ConversationAnalyzer


messages = [
    {
        "role": "user",
        "content": "Hiring a mid-level Java backend developer with stakeholder communication"
    }
]

analyzer = ConversationAnalyzer()

result = analyzer.analyze(messages)

print(result)