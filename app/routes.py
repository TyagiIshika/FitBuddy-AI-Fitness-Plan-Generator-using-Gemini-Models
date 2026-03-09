from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .database import SessionLocal, User, WorkoutPlan
from .gemini_generator import generate_workout_gemini

# Router
router = APIRouter()

# Templates
templates = Jinja2Templates(directory="templates")


# Home Page
@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Generate Workout Plan
@router.post("/generate-workout", response_class=HTMLResponse)
def generate_workout(
    request: Request,
    username: str = Form(...),
    user_id: str = Form(...),
    age: int = Form(...),
    weight: float = Form(...),
    goal: str = Form(...),
    intensity: str = Form(...)
):

    db = SessionLocal()

    # Save User
    user = User(
        name=username,
        age=age,
        weight=weight,
        goal=goal,
        intensity=intensity
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    # Generate workout plan
    workout_plan = generate_workout_gemini({
        "goal": goal,
        "intensity": intensity
    })

    # Save workout plan
    plan = WorkoutPlan(
        user_id=user.id,
        original_plan=workout_plan,
        updated_plan=""
    )

    db.add(plan)
    db.commit()

    db.close()

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "username": username,
            "workout_plan": workout_plan
        }
    )


