from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ VERY IMPORTANT: CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow frontend
    allow_credentials=True,
    allow_methods=["*"],   # POST, GET, OPTIONS
    allow_headers=["*"],
)

class UserSkills(BaseModel):
    skills: list[str]

@app.get("/")
def home():
    return {"status": "Backend running"}

@app.post("/recommend")
def recommend(data: UserSkills):
    return {
        "recommended_career": "Software Engineer"
    }
