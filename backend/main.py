from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS (frontend nundi backend ki allow cheyyadaniki)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # beginner ki safe
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend running successfully"}

@app.post("/recommend")
def recommend(data: dict):
    skills = data.get("user_skills", "")

    # simple dummy logic (testing kosam)
    if "python" in skills.lower():
        career = "AI Engineer"
    else:
        career = "Software Developer"

    return {
        "recommended_career": career
    }