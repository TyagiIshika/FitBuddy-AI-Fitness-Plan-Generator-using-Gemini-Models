import google.generativeai as genai

genai.configure(api_key="AIzaSyCObh0viev_ZV94FbDJcEx9khl5biCUYSQ")

model = genai.GenerativeModel("gemini-1.5-flash")


def generate_nutrition_tip_with_flash(goal):

    prompt = f"""
You are a professional nutritionist.

Give 5 short nutrition tips for someone whose fitness goal is: {goal}

Keep tips practical and simple.
"""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Nutrition Tip Error: {e}"

