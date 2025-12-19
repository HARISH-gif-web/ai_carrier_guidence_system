from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import pandas as pd

# -------------------- APP --------------------
app = FastAPI(title="AI Career Guidance System")

# -------------------- CORS --------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------- LOAD DATA --------------------
# IMPORTANT: run uvicorn from backend folder
data = pd.read_csv("../data/roles_skills.csv")

# -------------------- Pydantic Model --------------------
class UserSkills(BaseModel):
    skills: List[str]

# -------------------- ROUTES --------------------
@app.get("/")
def read_root():
    return {"message": "Backend is running successfully"}

@app.get("/careers")
def get_careers():
    return {
        "total_roles": len(data),
        "roles": data["role"].tolist()
    }

@app.post("/recommend")
def recommend_career(user: UserSkills):
    user_skills = set(skill.strip().lower() for skill in user.skills)

    best_role = None
    best_score = 0
    best_missing = []

    for _, row in data.iterrows():
        role_skills = set(s.strip().lower() for s in row["skills"].split(","))
        matched = user_skills & role_skills
        score = len(matched)

        if score > best_score:
            best_score = score
            best_role = row["role"]
            best_missing = list(role_skills - user_skills)

    return {
        "recommended_career": best_role,
        "matched_skills": list(user_skills),
        "missing_skills": best_missing
    }