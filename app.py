import json
import streamlit as st

from llm_chain import analyze_feedback, generate_explanation
from fuzzy_system import calculate_environment_score


st.set_page_config(
    page_title="EduBridge",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 EduBridge")
st.subheader("Classroom Environment & Interaction Analyzer")

st.write(
    "EduBridge uses AI and fuzzy logic to analyze anonymous student "
    "feedback and understand the overall classroom learning environment."
)

st.info(
    "The system analyzes classroom communication, teaching behaviour, "
    "student comfort, participation and classroom atmosphere — "
    "it does not rate individual teachers."
)

feedback = st.text_area(
    "💬 Share your classroom experience anonymously:",
    placeholder=(
        "Example: The teacher explains concepts well, but students "
        "sometimes hesitate to ask questions. Most students participate "
        "during activities and the classroom feels comfortable."
    ),
    height=150
)

if st.button("🔍 Analyze Classroom Environment"):

    if not feedback.strip():
        st.warning("Please enter some feedback first.")

    else:
        with st.spinner("🤖 AI is analyzing your feedback..."):

            # Step 1: LangChain + LLM extracts classroom factors
            result, error = analyze_feedback(feedback)

        if error:
            st.error(error)

        else:
            try:
                cleaned_result = result.replace("```json", "").replace("```", "").strip()
                scores = json.loads(cleaned_result)

                # Step 2: Genuine Fuzzy Inference System
                overall_score = calculate_environment_score(
                    scores["communication"],
                    scores["teaching"],
                    scores["comfort"],
                    scores["participation"],
                    scores["atmosphere"]
                )

                st.success("✅ Analysis completed!")

                st.subheader("📊 Classroom Factors")

                col1, col2 = st.columns(2)

                with col1:
                    st.metric("Communication", f'{scores["communication"]}/10')
                    st.metric("Teaching Behaviour", f'{scores["teaching"]}/10')
                    st.metric("Student Comfort", f'{scores["comfort"]}/10')

                with col2:
                    st.metric("Participation", f'{scores["participation"]}/10')
                    st.metric("Classroom Atmosphere", f'{scores["atmosphere"]}/10')

                st.subheader("🎯 Overall Classroom Environment")

                st.metric(
                    "Environment Score",
                    f"{overall_score}/100"
                )

                if overall_score < 40:
                    category = "Poor"
                elif overall_score < 60:
                    category = "Moderate"
                elif overall_score < 80:
                    category = "Good"
                else:
                    category = "Excellent"

                st.info(f"Overall Environment Category: **{category}**")

                # Step 3: LangChain explains the result
                with st.spinner("💡 Generating constructive suggestions..."):

                    explanation, explanation_error = generate_explanation(
                        feedback,
                        scores,
                        overall_score
                    )

                if explanation_error:
                    st.warning(explanation_error)
                else:
                    st.subheader("💡 AI Insights & Suggestions")
                    st.write(explanation)

            except Exception as e:
                st.error(f"Could not process the AI response: {e}")