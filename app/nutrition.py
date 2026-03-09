import google.generativeai as genai

genai.configure(api_key="AIzaSyCObh0viev_ZV94FbDJcEx9khl5biCUYSQ")

model = genai.GenerativeModel("gemini-1.5-flash")


def generate_nutrition_tip_with_flash(goal):

    prompt = f"""
You are a professional nutritionist.

Give 5 nutrition tips for someone whose goal is {goal}.
Keep tips short and practical.
"""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return """
1. Eat high protein foods
2. Drink enough water
3. Avoid processed sugar
4. Eat vegetables daily
5. Maintain calorie balance
"""