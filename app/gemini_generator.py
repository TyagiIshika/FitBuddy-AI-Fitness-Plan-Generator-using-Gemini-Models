import google.generativeai as genai

# configure API
genai.configure(api_key="AIzaSyCObh0viev_ZV94FbDJcEx9khl5biCUYSQ")

# model
model = genai.GenerativeModel("gemini-pro")


def generate_workout_gemini(user_input):

    goal = user_input["goal"]
    intensity = user_input["intensity"]

    prompt = f"""
You are a professional fitness trainer.

Create a structured 7 day workout plan.

Goal: {goal}
Intensity: {intensity}

Each day must include:
- Warmup
- Main workout
- Cooldown

Format:

Day 1
Warmup:
Main workout:
Cooldown:

Repeat until Day 7.
"""

    try:
        response = model.generate_content(prompt)

        if response and response.text:
            return response.text

        else:
            return default_plan()

    except Exception as e:
        print("Gemini Error:", e)
        return default_plan()


def default_plan():

    return """
Day 1: Cardio + Stretching
Day 2: Upper Body Strength
Day 3: Yoga + Mobility
Day 4: HIIT Training
Day 5: Lower Body Strength
Day 6: Full Body Workout
Day 7: Rest and Recovery
"""
