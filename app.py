import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from utils.pdf_parser import extract_text
from utils.skill_extractor import extract_skills
from utils.ats_score import calculate_ats_score
from utils.missing_skills import find_missing_skills

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
    # QUICK STATS
    # ==================================

    jd_score = 0

    if jd_result:
        jd_score = jd_result["score"]

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "ATS Score",
            f"{score}%"
        )

    with col2:
        st.metric(
            "JD Match",
            f"{jd_score}%"
        )

    with col3:
        st.metric(
            "Skills Found",
            len(skills)
        )

    with col4:
        st.metric(
            "Recommended Roles",
            len(recommended_roles)
        )
        
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

    skills_text = " | ".join(
        sorted(skills)
    )

    st.info(
        skills_text
    )

    # ==================================
    # MISSING SKILLS
    # ==================================

    st.subheader(
        "❌ Missing Skills"
    )

    if missing_skills:

        missing_text = " | ".join(
            jd_result["missing"]
        )

        st.warning(
            missing_text
        )

    else:

        st.success(
            "No missing skills found"
        )



    # ==================================
    # AI INTERVIEW PREPARATION
    # ==================================

    st.subheader(
        "🎤 AI Interview Preparation"
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
        # TECHNICAL QUESTIONS
        # -------------------------

        with st.expander(
            "💻 Technical Questions",
            expanded=True
        ):

            for line in technical_part.split("\n"):

                if "-" in line:

                    question = (
                        line.replace("-", "")
                        .replace("*", "")
                        .strip()
                    )

                    if question:

                        st.info(
                            question
                        )

        # -------------------------
        # PROJECT QUESTIONS
        # -------------------------

        with st.expander(
            "🚀 Project Questions",
            expanded=False
        ):

            for line in project_part.split("\n"):

                if "-" in line:

                    question = (
                        line.replace("-", "")
                        .replace("*", "")
                        .strip()
                    )

                    if question:

                        st.success(
                            question
                        )

        # -------------------------
        # HR QUESTIONS
        # -------------------------

        with st.expander(
            "👨‍💼 HR Questions",
            expanded=False
        ):

            for line in hr_part.split("\n"):

                if "-" in line:

                    question = (
                        line.replace("-", "")
                        .replace("*", "")
                        .strip()
                    )

                    if question:

                        st.warning(
                            question
                        )

    except Exception:

        with st.expander(
            "🤖 Raw AI Interview Output",
            expanded=False
        ):

            st.markdown(
                interview_questions_ai
            )
            
    # ==================================
    # LEARNING ROADMAP
    # ==================================

    with st.expander(
        "🗺️ Learning Roadmap",
        expanded=False
    ):

        for step in roadmap:

            st.success(
                step
            )
    
    # ==================================
    # RESUME VS JD MATCHING
    # ==================================

    if jd_result:

        with st.expander(
            "🎯 Resume vs Job Description Match",
            expanded=True
        ):

            st.metric(
                "Match Score",
                f"{jd_result['score']}%"
            )

            if jd_result["score"] >= 80:

                st.success(
                    "Excellent Match"
                )

            elif jd_result["score"] >= 60:

                st.warning(
                    "Good Match"
                )

            else:

                st.error(
                    "Low Match"
                )

            # -------------------------
            # MATCHING SKILLS
            # -------------------------

            st.markdown(
                "### ✅ Matching Skills"
            )

            if jd_result["matched"]:

                matched_text = " | ".join(
                    jd_result["matched"]
                )

                st.success(
                    matched_text
                )

            else:

                st.info(
                    "No matching skills found"
                )

            # -------------------------
            # MISSING SKILLS
            # -------------------------

            st.markdown(
                "### ❌ Missing Skills"
            )

            if missing_skills:

                missing_text = " | ".join(
                    missing_skills
                )

                st.warning(
                    missing_text
                )

            else:

                st.success(
                    "No missing skills detected"
                )
                
            # -------------------------
            # SUGGESTIONS
            # -------------------------

            st.markdown(
                "### 💡 Suggestions"
            )

            if jd_result["suggestions"]:

                for suggestion in jd_result["suggestions"]:

                    st.info(
                        suggestion
                    )

            else:

                st.success(
                    "Your resume already matches the JD very well."
                )
                
    # ==================================
    # AI RESUME INSIGHTS
    # ==================================

    with st.expander(
        "🤖 AI Resume Insights",
        expanded=True
    ):

        st.markdown(
            ai_feedback
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