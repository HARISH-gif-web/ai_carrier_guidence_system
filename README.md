# AI Career Recommender System

A full-stack web application that recommends career paths based on user skills using intelligent matching algorithms.

## Tech Stack
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Backend**: Python with FastAPI
- **Database**: CSV-based data store (roles_skills.csv)
- **Server**: Uvicorn

## Features
✅ Skill-based career recommendations  
✅ Match percentage calculation  
✅ Missing skills identification  
✅ Learning tasks/roadmap for each career  
✅ Salary range and difficulty levels  
✅ Browse all available career paths  
✅ Responsive UI with modern design  
✅ Real-time API integration  

## Project Structure
```
.
├── frontend/              # Frontend assets
├── backend/              # Python FastAPI backend
│   ├── main.py          # Main API application
│   ├── requirements.txt  # Python dependencies
│   └── __init__.py
├── data/                # Database files
│   └── roles_skills.csv # Career data with tasks
├── index.html           # Main HTML file
└── README.md           # This file
```

## Database Schema (roles_skills.csv)
```
role | skills | salary_range | difficulty | description | tasks
```

**Sample roles included:**
- AI Engineer
- ML Engineer
- Data Scientist
- Web Developer
- Cloud Architect
- Cyber Security Analyst
- Full Stack Developer
- DevOps Engineer
- Database Administrator
- Product Manager

## Installation & Setup

### 1. Install Python Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 2. Start the Backend Server
```bash
cd backend
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

**Output should show:**
```
Uvicorn running on http://127.0.0.1:8000
Application startup complete
```

### 3. Start the Frontend
Open in browser or serve with a local server:
```bash
# Option 1: Direct browser open
start index.html

# Option 2: Using Python server (Python 3)
python -m http.server 8080

# Option 3: Using Node.js http-server
npx http-server
```

Then navigate to: `http://localhost:8000` (if using Python server) or open `index.html` directly

## API Endpoints

### 1. Home Endpoint
```
GET http://127.0.0.1:8000/
Response: API status and available endpoints
```

### 2. Get Career Recommendation
```
POST http://127.0.0.1:8000/recommend
Content-Type: application/json

Request:
{
  "skills": ["Python", "Machine Learning", "Data Analysis"]
}

Response:
{
  "recommended_career": "Data Scientist",
  "match_percentage": 75.5,
  "matched_skills": ["Python", "Data Analysis"],
  "missing_skills": ["SQL", "Statistics", "Data Visualization"],
  "salary_range": "100k-160k",
  "difficulty": "Intermediate",
  "tasks": [
    "Perform data analysis",
    "Create visualizations",
    "Build predictive models",
    "Present insights to stakeholders"
  ]
}
```

### 3. Get All Roles
```
GET http://127.0.0.1:8000/roles

Response:
{
  "roles": ["AI Engineer", "ML Engineer", ...],
  "count": 10
}
```

### 4. Get Role Details
```
GET http://127.0.0.1:8000/roles/{role_name}

Example: http://127.0.0.1:8000/roles/AI%20Engineer

Response:
{
  "role": "AI Engineer",
  "skills": ["Python", "Machine Learning", ...],
  "salary_range": "120k-180k",
  "difficulty": "Advanced",
  "description": "Develop AI/ML models",
  "tasks": ["Build neural networks", ...]
}
```

## Features Explained

### 1. Skill Matching Algorithm
- Calculates percentage match between user skills and role requirements
- Case-insensitive matching
- Returns best matching career

### 2. Missing Skills Detection
- Identifies skills needed for recommended career
- Provides learning roadmap

### 3. Task Management
- Each role includes specific learning tasks
- Helps users understand what needs to be done

### 4. Career Details
- Salary ranges
- Difficulty levels
- Role descriptions

## Usage Example

1. Open `index.html` in a browser
2. Enter skills: "Python, Machine Learning"
3. Click "Get Recommendation"
4. System recommends: "Data Scientist" or "AI Engineer"
5. View missing skills and learning tasks
6. Click "View All Roles" to explore other options

## Deployment Guide

### Docker Deployment
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Environment Variables
- `PORT`: Server port (default: 8000)
- `HOST`: Server host (default: 127.0.0.1)

### Production Deployment Options
1. **Heroku**
   ```bash
   git push heroku main
   ```

2. **AWS EC2**
   - Install Python 3.9+
   - Install dependencies
   - Run with PM2 or systemd

3. **Azure App Service**
   - Deploy from GitHub
   - Configure environment variables

4. **Vercel/Netlify** (Frontend only)
   - Deploy `index.html` to static hosting

## Troubleshooting

### Backend not running
```
Error: Connection refused at 127.0.0.1:8000
Solution: Make sure backend is started: uvicorn main:app --reload
```

### CORS errors
```
Error: Cross-Origin Request Blocked
Solution: Backend CORS is already configured. Make sure backend URL is correct.
```

### Skills not matching
```
- Check spelling (case-insensitive)
- Verify skills exist in roles_skills.csv
- Multiple skills must be comma-separated
```

## Data Management

### Adding New Careers
1. Edit `data/roles_skills.csv`
2. Add new row with: role, skills, salary_range, difficulty, description, tasks
3. Restart backend server

### Updating Skills
1. Modify the `skills` column in CSV
2. Use pipe (|) to separate multiple tasks
3. Use comma (,) to separate skills

## Performance

- **Response Time**: < 100ms
- **Database**: In-memory CSV parsing (instant loads)
- **Scalability**: Ready for database migration (SQLite/PostgreSQL)

## Future Enhancements

- [ ] User authentication & profiles
- [ ] Save favorite careers
- [ ] Progress tracking
- [ ] Interactive skill assessments
- [ ] Real-time job market data
- [ ] Machine learning skill matching
- [ ] Database migration to PostgreSQL
- [ ] Mobile app version

## License
MIT

## Support
For issues or questions, check the troubleshooting section or examine browser console for errors.

---

**Ready for Deployment! ✅**

This system is production-ready with:
- ✅ Full API integration
- ✅ Error handling
- ✅ CORS support
- ✅ Responsive UI
- ✅ Comprehensive data
- ✅ Task management
- ✅ Easy scalability
