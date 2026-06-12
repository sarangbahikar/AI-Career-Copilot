import streamlit as st

from utils.pdf_parser import extract_text
from utils.skill_extractor import extract_skills
from utils.ats_score import calculate_ats_score
from utils.missing_skills import find_missing_skills

from utils.strengths import get_strengths
from utils.weaknesses import get_weaknesses
from utils.recommendations import get_recommendations


st.set_page_config(
    page_title="AI Career Copilot",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 AI Career Copilot")
st.markdown("### Resume Intelligence & Career Guidance Platform")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    # Extract Resume Text
    text = extract_text(uploaded_file)
    st.subheader("Debug Resume Text")
    st.text_area("Extracted Text", text, height=500)
    
    # Extract Skills
    skills = extract_skills(text)

    # ATS Score
    score = calculate_ats_score(text, skills)

    # Missing Skills
    missing_skills = find_missing_skills(skills)

    # Strengths
    strengths = get_strengths(text, skills)

    # Weaknesses
    weaknesses = get_weaknesses(text)

    # Recommendations
    recommendations = get_recommendations(
        weaknesses
    )

    # ATS Score Section
    st.subheader("📊 ATS Score")

    st.metric(
        "ATS Score",
        f"{score}/100"
    )

    # Resume Analysis
    st.subheader("📋 Resume Analysis")

    if score >= 80:
        st.success(
            "Excellent Resume"
        )

    elif score >= 60:
        st.warning(
            "Good Resume but can be improved"
        )

    else:
        st.error(
            "Resume needs improvement"
        )

    # Skills Section
    st.subheader("🛠 Detected Skills")

    for skill in skills:
        st.success(f"✓ {skill}")

    # Missing Skills Section
    st.subheader("❌ Missing Skills")

    if missing_skills:

        for skill in missing_skills:
            st.warning(f"⚠ {skill}")

    else:
        st.success(
            "No missing skills found"
        )

    # Strengths Section
    st.subheader("💪 Strengths")

    if strengths:

        for item in strengths:
            st.success(item)

    else:
        st.info(
            "No major strengths detected"
        )

    # Weaknesses Section
    st.subheader("⚠ Weaknesses")

    if weaknesses:

        for item in weaknesses:
            st.warning(item)

    else:
        st.success(
            "No major weaknesses found"
        )

    # Recommendations Section
    st.subheader("🚀 Recommendations")

    if recommendations:

        for item in recommendations:
            st.info(item)

    else:
        st.success(
            "No recommendations needed"
        )

    # Resume Content
    st.subheader("📄 Resume Content")

    st.text_area(
        "",
        text,
        height=300
    )