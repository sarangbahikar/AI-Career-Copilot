import streamlit as st

from utils.pdf_parser import extract_text
from utils.skill_extractor import extract_skills
from utils.resume_score import calculate_score

st.set_page_config(
    page_title="AI Career Copilot",
    page_icon="🚀"
)

st.title("🚀 AI Career Copilot")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    text = extract_text(uploaded_file)

    skills = extract_skills(text)

    score = calculate_score(skills)

    st.subheader("Resume Score")
    st.metric("ATS Score", f"{score}/100")

    st.subheader("Detected Skills")
    st.write(skills)

    st.subheader("Resume Content")
    st.text_area("", text, height=300)