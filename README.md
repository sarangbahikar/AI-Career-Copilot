# 🚀 AI Career Copilot

## Overview

AI Career Copilot is an AI-powered Resume Intelligence and Interview Preparation Platform built using Streamlit, Groq LLMs, and Python.

The platform helps students and job seekers analyze resumes, calculate ATS scores, identify skill gaps, match resumes against job descriptions, generate AI-powered interview questions, and receive personalized resume feedback.

---

## Features

### Resume Analysis

* PDF Resume Upload
* Resume Text Extraction
* ATS Score Calculation
* ATS Score Breakdown
* Skill Extraction
* Missing Skills Detection

### Career Guidance

* Recommended Career Roles
* Personalized Learning Roadmap
* Resume vs Job Description Matching
* Skill Gap Analysis

### AI Features

* AI Resume Feedback using Groq Llama 3.3 70B
* AI Technical Interview Questions
* AI Project-Based Interview Questions
* AI HR Interview Questions

### Reporting

* PDF Career Report Generation
* Interactive Dashboard
* Downloadable Analysis Report

---

## Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI / LLM

* Groq API
* Llama 3.3 70B Versatile

### Data Processing

* Pandas
* Plotly

### Resume Processing

* PyMuPDF

### Deployment

* Render

---

## Project Architecture

AI_Career_Copilot/

├── app.py

├── requirements.txt

├── README.md

│

├── utils/

│   ├── ats_score.py

│   ├── jd_matcher.py

│   ├── groq_feedback.py

│   ├── interview_generator_ai.py

│   ├── roadmap_generator.py

│   ├── pdf_parser.py

│   ├── skill_extractor.py

│   ├── job_recommender.py

│   └── pdf_report.py

---

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI_Career_Copilot.git

cd AI_Career_Copilot
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

### Run Application

```bash
streamlit run app.py
```

---

## Current Features Implemented

✅ ATS Score Calculation

✅ Skill Extraction

✅ Missing Skill Detection

✅ Resume Analysis Dashboard

✅ Resume vs Job Description Matching

✅ AI Resume Feedback

✅ AI Interview Question Generation

✅ Career Role Recommendations

✅ Learning Roadmap

✅ PDF Report Download

---

## Future Improvements

* AI Resume Rewriter
* AI Cover Letter Generator
* AI Learning Roadmap Generator
* Multi Resume Comparison
* Interview Answer Generator
* Resume Version Tracking

---

## Author

**Sarang Bahikar**

AI / Data Science Enthusiast

Built as a portfolio project to demonstrate:

* Python Development
* Generative AI Integration
* LLM Applications
* Streamlit Development
* Career Intelligence Systems
