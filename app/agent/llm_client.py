import os

from dotenv import load_dotenv
from groq import Groq


load_dotenv()


class LLMClient:
    def __init__(self):
        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

        self.model = "llama-3.1-70b-versatile"

    def generate_recommendation_reply(
        self,
        user_query,
        recommendations,
    ):
        recommendation_text = "\n".join(
            [
                f"- {item['name']} ({item['test_type']})"
                for item in recommendations
            ]
        )

        prompt = f"""
You are an SHL assessment recommendation assistant.

User hiring request:
{user_query}

Recommended assessments:
{recommendation_text}

Write a concise professional response:
- explain why these assessments fit
- mention technical and behavioral coverage if relevant
- keep under 100 words
- do not invent assessments
- do not mention assessments not listed
"""

        try:
            response = (
                self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are a professional SHL "
                                "assessment recommendation assistant."
                            ),
                        },
                        {
                            "role": "user",
                            "content": prompt,
                        },
                    ],
                    temperature=0.3,
                    max_tokens=120,
                )
            )

            return (
                response.choices[0]
                .message.content
                .strip()
            )

        except Exception:
            return (
                "I found assessments that match the "
                "required technical and behavioral "
                "hiring criteria."
            )

    def generate_comparison_reply(
        self,
        comparison_text,
    ):
        prompt = f"""
You are an SHL assessment expert.

Using ONLY the information below:

{comparison_text}

Write a concise comparison summary:
- explain the primary difference
- mention assessment focus areas
- keep under 80 words
- do not invent information
"""

        try:
            response = (
                self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are an SHL assessment expert."
                            ),
                        },
                        {
                            "role": "user",
                            "content": prompt,
                        },
                    ],
                    temperature=0.2,
                    max_tokens=100,
                )
            )

            return (
                response.choices[0]
                .message.content
                .strip()
            )

        except Exception:
            return comparison_text