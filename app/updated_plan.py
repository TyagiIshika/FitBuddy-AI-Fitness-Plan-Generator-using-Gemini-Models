def update_workout_plan(original_plan, feedback):

    prompt = f"""
User has given feedback on workout plan.

Original Plan:
{original_plan}

Feedback:
{feedback}

Create an improved 7 day workout plan.
"""

    return f"""
Updated Plan Based On Feedback

Day 1: Cardio + Core
Day 2: Upper Body Strength
Day 3: Yoga
Day 4: HIIT
Day 5: Lower Body
Day 6: Full Body
Day 7: Rest
"""