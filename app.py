import streamlit as st

st.set_page_config(
    page_title="FitBuddy AI",
    page_icon="💪",
    layout="centered"
)

st.title("💪 FitBuddy AI")
st.write("AI Fitness Plan Generator")

st.subheader("Enter Your Details")

age = st.number_input("Age", min_value=13, max_value=100, value=18)
height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0)
weight = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0)

goal = st.selectbox(
    "Your Goal",
    ["General Fitness", "Build Strength", "Improve Endurance"]
)

if st.button("Generate Fitness Plan"):
    st.success("Your fitness plan has been generated!")

    st.write("### Your Details")
    st.write(f"Age: {age}")
    st.write(f"Height: {height} cm")
    st.write(f"Weight: {weight} kg")
    st.write(f"Goal: {goal}")

    st.write("### Suggested Plan")
    st.write("- Warm-up: 5–10 minutes")
    st.write("- Main activity: 20–30 minutes")
    st.write("- Cool-down: 5–10 minutes")
    st.write("- Stay hydrated and get adequate rest.")
