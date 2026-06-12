import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from utils.pdf_parser import extract_text
from utils.skill_extractor import extract_skills
from utils.ats_score import calculate_ats_score
from utils.missing_skills import find_missing_skills

from utils.strengths import get_strengths
from utils.weaknesses import get_weaknesses
from utils.recommendations import get_recommendations
from utils.job_recommender import recommend_roles
from utils.roadmap_generator import generate_roadmap
from utils.pdf_report import create_report
from utils.jd_matcher import calculate_jd_match
from utils.groq_feedback import generate_feedback
from utils.interview_generator_ai import generate_interview_questions_ai
# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(
    page_title="AI Career Copilot",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 AI Career Copilot")
st.markdown(
    "### Resume Intelligence & Interview Preparation Platform"
)

# ==================================
# FILE UPLOAD
# ==================================

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

job_description = st.text_area(
    "📄 Paste Job Description Here",
    height=200
)

# ==================================
# MAIN APP
# ==================================

if uploaded_file:

    # Resume Text

    text = extract_text(uploaded_file)

    # Skills

    skills = extract_skills(text)

    # ATS Score

    score_data = calculate_ats_score(
        text,
        skills
    )

    score = score_data["total"]

    # Analysis

    missing_skills = find_missing_skills(
        skills
    )

    strengths = get_strengths(
        text,
        skills
    )

    weaknesses = get_weaknesses(
        text
    )

    recommendations = get_recommendations(
        weaknesses
    )

    recommended_roles = recommend_roles(
        skills
    )


    try:

        interview_questions_ai = (
            generate_interview_questions_ai(
                text
            )
        )

    except Exception as e:

        interview_questions_ai = (
            f"Error: {str(e)}"
        )
    
    roadmap = generate_roadmap(
    recommended_roles
    )
    
    jd_result = None

    if job_description:

        jd_result = calculate_jd_match(
            skills,
            job_description
        )
    
    create_report(
    "career_report.pdf",
    score,
    skills,
    recommended_roles,
    roadmap
    )

    # ==================================
    # AI FEEDBACK PLACEHOLDER
    # ==================================

    try:

        ai_feedback = generate_feedback(
            text
        )

    except Exception as e:

        ai_feedback = f"""
    AI Feedback Unavailable

    Error:
    {str(e)}
    """

    # ==================================
    # ATS DASHBOARD
    # ==================================

    st.subheader("📊 ATS Dashboard")

    col1, col2 = st.columns(2)

    with col1:

        gauge = go.Figure(

            go.Indicator(

                mode="gauge+number",

                value=score,

                title={
                    "text": "ATS Score"
                },

                gauge={

                    "axis": {
                        "range": [0, 100]
                    },

                    "bar": {
                        "thickness": 0.4
                    },

                    "steps": [

                        {
                            "range": [0, 50],
                            "color": "lightgray"
                        },

                        {
                            "range": [50, 80],
                            "color": "gray"
                        },

                        {
                            "range": [80, 100],
                            "color": "darkgreen"
                        }

                    ]
                }
            )
        )

        st.plotly_chart(
            gauge,
            use_container_width=True
        )

    with col2:

        st.metric(
            "ATS Score",
            f"{score}/100"
        )

        if score >= 80:

            st.success(
                "Excellent Resume"
            )

        elif score >= 60:

            st.warning(
                "Good Resume"
            )

        else:

            st.error(
                "Needs Improvement"
            )

    # ==================================
    # SCORE BREAKDOWN
    # ==================================

    st.subheader(
        "📈 Score Breakdown"
    )

    breakdown_df = pd.DataFrame({

        "Category": [

            "Skills",
            "Education",
            "Projects",
            "Experience",
            "Certifications"

        ],

        "Score": [

            score_data["skills"],
            score_data["education"],
            score_data["projects"],
            score_data["experience"],
            score_data["certifications"]

        ]

    })

    fig = px.bar(

        breakdown_df,

        x="Category",
        y="Score",

        text="Score",

        title="ATS Score Breakdown"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ==================================
    # RESUME ANALYSIS
    # ==================================

    st.subheader(
        "📋 Resume Analysis"
    )

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

    # ==================================
    # DETECTED SKILLS
    # ==================================

    st.subheader(
        "🛠 Detected Skills"
    )

    for skill in skills:

        st.success(
            f"✓ {skill}"
        )

    # ==================================
    # MISSING SKILLS
    # ==================================

    st.subheader(
        "❌ Missing Skills"
    )

    if missing_skills:

        for skill in missing_skills:

            st.warning(
                f"⚠ {skill}"
            )

    else:

        st.success(
            "No missing skills found"
        )

    # ==================================
    # STRENGTHS
    # ==================================

    st.subheader(
        "💪 Strengths"
    )

    if strengths:

        for item in strengths:

            st.success(
                item
            )

    # ==================================
    # WEAKNESSES
    # ==================================

    st.subheader(
        "⚠ Weaknesses"
    )

    if weaknesses:

        for item in weaknesses:

            st.warning(
                item
            )

    else:

        st.success(
            "No major weaknesses found"
        )

    # ==================================
    # JOB RECOMMENDATIONS
    # ==================================

    st.subheader(
        "🎯 Recommended Roles"
    )

    if recommended_roles:

        for role in recommended_roles:

            st.success(
                role
            )

    else:

        st.info(
            "No matching role found"
        )


    # ==================================
    # AI INTERVIEW PREPARATION
    # ==================================

    st.subheader(
        "🤖 AI Interview Preparation"
    )

    try:

        sections = interview_questions_ai.split(
            "PROJECT:"
        )

        technical_part = sections[0]

        project_hr = ""

        if len(sections) > 1:

            project_hr = sections[1]

        project_sections = project_hr.split(
            "HR:"
        )

        project_part = project_sections[0]

        hr_part = ""

        if len(project_sections) > 1:

            hr_part = project_sections[1]

        # -------------------------
        # TECHNICAL
        # -------------------------

        st.markdown(
            "### 💻 Technical Questions"
        )

        for line in technical_part.split("\n"):

            if "-" in line:

                question = (
                    line.replace("-", "")
                    .strip()
                )

                st.info(question)

        # -------------------------
        # PROJECT
        # -------------------------

        st.markdown(
            "### 🚀 Project Questions"
        )

        for line in project_part.split("\n"):

            if "-" in line:

                question = (
                    line.replace("-", "")
                    .strip()
                )

                st.success(question)

        # -------------------------
        # HR
        # -------------------------

        st.markdown(
            "### 👨‍💼 HR Questions"
        )

        for line in hr_part.split("\n"):

            if "-" in line:

                question = (
                    line.replace("-", "")
                    .strip()
                )

                st.warning(question)

    except Exception:

        st.markdown(
            interview_questions_ai
        )
    # ==================================
    # LEARNING ROADMAP
    # ==================================

    st.subheader(
            "🗺️ Learning Roadmap"
        )

    for step in roadmap:

            st.success(step)
    
    # ==================================
    # RESUME VS JD MATCHING
    # ==================================

    if jd_result:

        st.subheader(
            "🎯 Resume vs Job Match"
        )

        st.metric(
            "Match Score",
            f"{jd_result['score']}%"
        )

        st.markdown(
            "### ✅ Matching Skills"
        )

        for skill in jd_result["matched"]:

            st.success(
                skill
            )

        st.markdown(
            "### ❌ Missing Skills"
        )

        for skill in jd_result["missing"]:

            st.warning(
                skill
            )
                
    # ==================================
    # AI FEEDBACK
    # ==================================

    st.subheader(
        "🤖 AI Resume Feedback"
    )

    st.markdown(
        ai_feedback
    )

    # ==================================
    # RECOMMENDATIONS
    # ==================================

    st.subheader(
        "🚀 Recommendations"
    )

    if recommendations:

        for item in recommendations:

            st.info(
                item
            )

    else:

        st.success(
            "No recommendations needed"
        )
        
    # ==================================
    # DOWNLOAD REPORT
    # ==================================

    st.subheader(
        "📥 Download Report"
    )

    with open(
        "career_report.pdf",
        "rb"
    ) as file:

        st.download_button(
            label="Download Career Report",
            data=file,
            file_name="career_report.pdf",
            mime="application/pdf",
            key="career_report_download"
        )


    # ==================================
    # RESUME CONTENT
    # ==================================

    with st.expander(
        "📄 View Resume Content"
    ):

        st.text_area(
            "",
            text,
            height=300
        )