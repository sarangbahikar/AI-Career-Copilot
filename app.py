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

st.set_page_config(
    page_title="AI Career Copilot",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 AI Career Copilot")
st.markdown(
    "### Resume Intelligence & Career Guidance Platform"
)

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    # ==================================
    # EXTRACT TEXT
    # ==================================

    text = extract_text(uploaded_file)

    # ==================================
    # SKILLS
    # ==================================

    skills = extract_skills(text)

    # ==================================
    # ATS SCORE
    # ==================================

    score_data = calculate_ats_score(
        text,
        skills
    )

    score = score_data["total"]

    # ==================================
    # ANALYSIS MODULES
    # ==================================

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

    # ==================================
    # ATS DASHBOARD
    # ==================================

    st.subheader("📊 ATS Dashboard")

    col1, col2 = st.columns(2)

    # ---------------------------
    # Gauge Meter
    # ---------------------------

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

    # ---------------------------
    # ATS Summary
    # ---------------------------

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

            st.success(item)

    else:

        st.info(
            "No major strengths detected"
        )

    # ==================================
    # WEAKNESSES
    # ==================================

    st.subheader(
        "⚠ Weaknesses"
    )

    if weaknesses:

        for item in weaknesses:

            st.warning(item)

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

            st.success(role)

    else:

        st.info(
            "No matching role found"
        )

    # ==================================
    # RECOMMENDATIONS
    # ==================================

    st.subheader(
        "🚀 Recommendations"
    )

    if recommendations:

        for item in recommendations:

            st.info(item)

    else:

        st.success(
            "No recommendations needed"
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