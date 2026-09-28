import os
import json
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()


def get_llm():
    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )


def demo_analysis(feedback):
    """
    Offline fallback used when the API is unavailable.
    This is only for demonstrating the application flow.
    """

    text = feedback.lower()

    communication = 5
    teaching = 5
    comfort = 5
    participation = 5
    atmosphere = 5

    if any(word in text for word in ["clearly", "clear", "explains well", "understand"]):
        communication += 2
        teaching += 2

    if any(word in text for word in ["hesitate", "afraid", "difficult to ask"]):
        communication -= 1
        participation -= 1

    if any(word in text for word in ["participate", "participation", "active"]):
        participation += 2

    if any(word in text for word in ["comfortable", "comfort", "safe"]):
        comfort += 2

    if any(word in text for word in ["positive", "friendly", "supportive", "good atmosphere"]):
        atmosphere += 2

    if any(word in text for word in ["confusing", "unclear", "difficult"]):
        teaching -= 2

    scores = {
        "communication": max(0, min(10, communication)),
        "teaching": max(0, min(10, teaching)),
        "comfort": max(0, min(10, comfort)),
        "participation": max(0, min(10, participation)),
        "atmosphere": max(0, min(10, atmosphere))
    }

    return json.dumps(scores), None


def analyze_feedback(feedback):

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return demo_analysis(feedback)

    try:
        llm = get_llm()

        prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                """
                You are EduBridge, a Classroom Environment & Interaction Analyzer.

                Analyze anonymous student classroom feedback.

                Do NOT rate or judge an individual teacher.
                Analyze only the overall classroom environment.

                Extract approximate scores from 0 to 10 for:

                1. Teacher-student communication
                2. Teaching behaviour/style
                3. Student comfort
                4. Student participation
                5. Classroom atmosphere

                Return ONLY valid JSON:

                {{
                    "communication": 0,
                    "teaching": 0,
                    "comfort": 0,
                    "participation": 0,
                    "atmosphere": 0
                }}
                """
            ),
            ("human", "{feedback}")
        ])

        chain = prompt | llm

        response = chain.invoke({
            "feedback": feedback
        })

        return response.content, None

    except Exception:
        return demo_analysis(feedback)


def generate_explanation(feedback, scores, overall_score):

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return demo_explanation(scores, overall_score), None

    try:
        llm = get_llm()

        prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                """
                You are EduBridge.

                Explain the classroom environment analysis in simple,
                constructive language.

                Do NOT judge or criticize an individual teacher.

                Give:
                1. A short explanation of the result.
                2. 2-3 constructive suggestions.

                Keep the response concise.
                """
            ),
            (
                "human",
                """
                Student feedback:
                {feedback}

                Classroom factors:
                {scores}

                Overall fuzzy score:
                {overall_score}/100
                """
            )
        ])

        chain = prompt | llm

        response = chain.invoke({
            "feedback": feedback,
            "scores": str(scores),
            "overall_score": overall_score
        })

        return response.content, None

    except Exception:
        return demo_explanation(scores, overall_score), None


def demo_explanation(scores, overall_score):

    if overall_score >= 80:
        level = "strong and positive"
    elif overall_score >= 60:
        level = "generally positive"
    elif overall_score >= 40:
        level = "moderate"
    else:
        level = "an area that may need attention"

    return f"""
The fuzzy analysis indicates a {level} overall classroom environment,
with an overall score of {overall_score}/100.

Constructive suggestions:
• Encourage students to ask questions and share their ideas comfortably.
• Continue using clear explanations and interactive classroom activities.
• Create opportunities for students to participate and give anonymous feedback.
"""