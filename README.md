# 📝 Python Quiz Game

A simple **True/False Quiz Game** built in Python.  
This is a beginner project that asks the user multiple questions, validates input, and keeps track of the score.  

---

## 🚀 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/quiz-game.git
   cd quiz-game
   ```

2. Run the game:
   ```bash
   python main.py
   ```

---

## 📂 Project Structure

```
quiz-game/
├── data.py             # Question data (list of dictionaries)
├── main.py             # Entry point of the program
├── question_model.py   # Defines the Question class
├── quiz_brain.py       # QuizBrain class: logic of the quiz
└── README.md           # Documentation
```

---

## ✨ Features
- Input validation (`True`/`False` only, case-insensitive)
- Keeps track of score
- Final summary at the end of the quiz

---

## 🖥️ Example Run

```
Q.1: A slug's blood is green. (True/False): True
✅ You got it right!
The correct answer was: True
Your current score is: 1/1

Q.2: The loudest animal is the African Elephant. (True/False): false
✅ You got it right!
The correct answer was: False
Your current score is: 2/2

Q.3: Approximately one quarter of human bones are in the feet. (True/False): maybe
⚠️ Kindly type only 'True' or 'False'.
Q.3: Approximately one quarter of human bones are in the feet. (True/False): True
✅ You got it right!
The correct answer was: True
Your current score is: 3/3

🥳 You've completed the quiz!
Your final score is 3/3
```

---

## 📌 Future Improvements
- Randomize question order
- Load questions from an external JSON or API
- Add a GUI version using Tkinter or PyQt
- Add multiple-choice questions

---

## 🙌 Acknowledgements
This project was created as a practice exercise while learning Python.  
Inspired by beginner-friendly coding exercises and quiz apps.
