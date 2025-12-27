from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS fix (frontend nundi request allow cheyyadaniki)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend running"}

@app.post("/recommend")
def recommend(data: dict):
    skills = data.get("user_skills", "")

    if "python" in skills.lower():
        career = "AI Engineer"
    elif "sql" in skills.lower():
        career = "Data Analyst"
    else:
        career = "Software Developer"

    return {
        "recommended_career": career
    }
