# 🧠 ADHD Detection API

## 🚀 Project Objective
Deploy a machine learning model as a REST API to assess ADHD risk based on behavioral metrics, providing instant predictions with probability scores.

## 🔍 Process
FastAPI backend with automated Swagger UI documentation
Predictive analytics: Returns risk level (low/medium/high) + confidence score
Deployed on Render for public access
Easy integration: JSON input/output for developers

## 🛠️ Tools & Technologies
- **Python** (FastAPI, Scikit-learn, Joblib)
- **Git/GitHub** for version control
- **Render** for cloud hosting
- **Swagger UI** for interactive testing

## 🌐 How to Use the API
### Via Swagger UI (Recommended for Testing)
1. Visit the live docs: 🔗<a href="https://adhd-datascience-project.onrender.com/docs">LINK</a>
2.Expand the **POST /predict** endpoint
3.Click **"Try it out"**
4.Paste this sample input (or modify values):
{
  "age": 25,
  "attention_score": 3.2,
  "hyperactivity_score": 2.1,
  "academic_index": 0.85,
  "ball_total": 1,
  "sex_female": 1,
  "sex_male": 0
}
5. Click **"Execute"** to see the prediction!


## 📷 API Preview
  <img width="646" alt="API_image" src="(https://github.com/Arrayar/ADHD-API/tree/main/screenshots)" />


## 🛠️ Tools Used
- **Tableau** for data visualization
- **SQL/Excel** for data preprocessing
- **AdventureWorks Dataset** as the data source

## 🔗 Live Dashboard
<a href="https://public.tableau.com/views/Adventureworks_chinu/Dashboard1?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link">Dashboard Link</a> 

---
⭐ **If you found this project useful, consider giving it a star!** ⭐
