from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

print("🎯 Welcome to the Quiz Game!")
print("Categories available:")
for index, category in enumerate(question_data.keys(), start=1):
    print(f"{index}. {category}")

choice = int(input("👉 Select a category by entering the number: "))
category_name = list(question_data.keys())[choice - 1]
print(f"\nYou selected: {category_name}\n")

question_bank = []
for question in question_data[category_name]:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("🥳 You've completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
