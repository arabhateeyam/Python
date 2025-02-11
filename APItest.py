import streamlit as st
import json
import os
print(os.getcwd())

# Load quiz data from JSON file
with open('quiz.json', 'r', encoding='utf-8') as file:
    quiz_data = json.load(file)

st.title("स्वज्ञानपरीक्षार्थं प्रश्नाः - Interactive  Sanskrit Quiz for Beginners")

# Store user answers
user_answers = {}

# Loop through each question
#for i, q in enumerate(quiz_data):
 #   user_answers[q["question"]] = st.radio(q["question"], q["options"], key=i)
for i, q in enumerate(quiz_data):
    # Insert a placeholder at the beginning of the options list
    options = ["Select an answer"] + q["options"]
    user_choice = st.radio(q["question"], options, key=i)
    # Store the user's answer if they have selected an option
    if user_choice != "Select an answer":
        user_answers[q["question"]] = user_choice
    else:
        user_answers[q["question"]] = None

# Submit button
if st.button("Submit"):
    st.subheader("Results:")
    score = 0
    for q in quiz_data:
        correct = q["answer"]
        user_choice = user_answers[q["question"]]
        if user_choice == correct:
            score += 1
            st.success(f"✅ {q['question']} - Correct!")
        else:
            st.error(f"❌ {q['question']} - Incorrect! (Correct: {correct})")

    st.subheader(f"Your Score: {score}/{len(quiz_data)}")
