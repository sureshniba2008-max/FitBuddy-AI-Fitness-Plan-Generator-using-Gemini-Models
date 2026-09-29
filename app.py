import streamlit as st
from google import genai

st.set_page_config(
    page_title="FitBuddy AI",
    page_icon="💪",
    layout="centered"
)

st.title("💪 FitBuddy AI")
st.subheader("AI Fitness Plan Generator")

goal = st.selectbox(
    "Choose your goal",
    [
        "General Fitness",
        "Improve Strength",
        "Improve Endurance",
        "Improve Flexibility"
    ]
)

activity_level = st.selectbox(
    "Current activity level",
    ["Beginner", "Intermediate"]
)

days = st.slider(
    "How many days per week?",
    min_value=2,
    max_value=5,
    value=3
)

minutes = st.slider(
    "Minutes available per session",
    min_value=15,
    max_value=60,
    value=30,
    step=5
)

if st.button("✨ Generate Fitness Plan"):

    prompt = f"""
    Create a safe, beginner-friendly general fitness plan.

    Goal: {goal}
    Activity level: {activity_level}
    Days per week: {days}
    Time per session: {minutes} minutes

    Give:
    1. Warm-up
    2. Main activities
    3. Cool-down
    4. Rest and recovery advice

    Do not recommend extreme exercise, dieting, weight loss,
    calorie restriction, supplements, or body-shape targets.
    Keep the advice general and age-appropriate.
    """

    try:
        client = genai.Client(
            api_key=st.secrets["GEMINI_API_KEY"]
        )

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        st.success("Your fitness plan is ready! 🎉")
        st.markdown(response.text)

    except Exception as e:
        st.error("Unable to generate the plan.")
        st.write("Please check your Gemini API key and app settings.")
