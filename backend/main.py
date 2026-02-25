from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import os

app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load CSV data
CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "roles_skills.csv")
df = pd.read_csv(CSV_PATH)

class UserSkills(BaseModel):
    skills: list[str]

def calculate_match_score(user_skills: list[str], role_skills: str) -> tuple[int, int]:
    """Calculate matching skills and score"""
    role_skills_list = [s.strip() for s in role_skills.split(",")]
    user_skills_lower = [s.lower().strip() for s in user_skills]
    role_skills_lower = [s.lower() for s in role_skills_list]
    
    matched = sum(1 for skill in user_skills_lower if skill in role_skills_lower)
    score = (matched / len(role_skills_list)) * 100 if role_skills_list else 0
    
    return matched, score

def get_missing_skills(user_skills: list[str], role_skills: str) -> list[str]:
    """Get skills needed for a role"""
    role_skills_list = [s.strip() for s in role_skills.split(",")]
    user_skills_lower = [s.lower().strip() for s in user_skills]
    
    missing = [skill for skill in role_skills_list 
               if skill.lower() not in user_skills_lower]
    return missing

def get_tasks_for_role(role: str) -> list[str]:
    """Get tasks for a role"""
    row = df[df['role'].str.lower() == role.lower()]
    if not row.empty and 'tasks' in row.columns:
        tasks_str = row.iloc[0]['tasks']
        return [t.strip() for t in tasks_str.split("|")]
    return []

@app.get("/")
def home():
    return {
        "status": "Backend running",
        "message": "AI Career Guidance System API",
        "endpoints": {
            "GET /": "This endpoint",
            "POST /recommend": "Get career recommendation",
            "GET /roles": "List all available roles",
            "GET /roles/{role_name}": "Get details for a specific role"
        }
    }

@app.get("/roles")
def get_roles():
    """Get all available roles"""
    roles = df['role'].tolist()
    return {"roles": roles, "count": len(roles)}

@app.get("/roles/{role_name}")
def get_role_details(role_name: str):
    """Get detailed information about a role"""
    row = df[df['role'].str.lower() == role_name.lower()]
    if row.empty:
        return {"error": "Role not found"}
    
    row = row.iloc[0]
    tasks = get_tasks_for_role(role_name)
    
    return {
        "role": row['role'],
        "skills": [s.strip() for s in row['skills'].split(",")],
        "salary_range": row.get('salary_range', 'N/A'),
        "difficulty": row.get('difficulty', 'N/A'),
        "description": row.get('description', 'N/A'),
        "tasks": tasks
    }

@app.post("/recommend")
def recommend(data: UserSkills):
    """Get career recommendation based on user skills"""
    if not data.skills or all(not s.strip() for s in data.skills):
        return {
            "error": "Please provide at least one skill",
            "recommended_career": None,
            "match_percentage": 0,
            "missing_skills": [],
            "tasks": []
        }
    
    # Clean user input
    clean_skills = [s.strip() for s in data.skills if s.strip()]
    
    # Calculate scores for all roles
    results = []
    for _, row in df.iterrows():
        matched, score = calculate_match_score(clean_skills, row['skills'])
        results.append({
            'role': row['role'],
            'score': score,
            'matched': matched,
            'skills': row['skills']
        })
    
    # Get best match
    best_match = max(results, key=lambda x: x['score'])
    
    # Get missing skills
    missing_skills = get_missing_skills(clean_skills, best_match['skills'])
    
    # Get tasks for recommended role
    tasks = get_tasks_for_role(best_match['role'])
    
    return {
        "recommended_career": best_match['role'],
        "match_percentage": round(best_match['score'], 2),
        "matched_skills": clean_skills,
        "missing_skills": missing_skills,
        "tasks": tasks,
        "salary_range": df[df['role'] == best_match['role']].iloc[0].get('salary_range', 'N/A'),
        "difficulty": df[df['role'] == best_match['role']].iloc[0].get('difficulty', 'N/A')
    }
