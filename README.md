# 🧠 True/False Quiz Game  

A simple Python-based interactive **True/False Quiz Game** built using **OOP principles**.  
The quiz pulls questions from multiple categories like **Science, History, Geography, Sports, and General Knowledge**.  

---

## 🚀 Features  
- Multiple categories of questions  
- Case-insensitive answer checking (`True` or `False`)  
- Score tracking after every question  
- User-friendly error handling (only accepts `True` or `False`)  
- Final score summary after completion  

---

## 📂 Project Structure  
```
📦 quiz-game
 ┣ 📜 main.py          # Entry point for the quiz  
 ┣ 📜 quiz_brain.py    # Quiz logic (engine)  
 ┣ 📜 question_model.py# Question class  
 ┣ 📜 data.py          # Contains the questions dataset  
 ┗ 📜 README.md        # Documentation  
```

---

## ▶️ How to Run  
1. Clone this repo:  
   ```bash
   git clone https://github.com/your-username/quiz-game.git
   cd quiz-game
   ```  

2. Run the game:  
   ```bash
   python main.py
   ```  

---

## 🎮 Example Gameplay  

```
Q.1: The chemical symbol for gold is 'Au'. (True/False): true
✅ You got it right!
The correct answer was True
The current score is 1/1

Q.2: The Great Wall of China is visible from the Moon. (True/False): false
✅ You got it right!
The correct answer was False
The current score is 2/2

Q.3: Cricket originated in India. (True/False): false
✅ You got it right!
The correct answer was False
The current score is 3/3

Q.4: The Earth revolves around the Sun. (True/False): true
✅ You got it right!
The correct answer was True
The current score is 4/4
```

---

## 📊 Categories Covered  
- 🌍 Geography  
- 🔬 Science  
- 📜 History  
- 🏏 Sports  
- 🧠 General Knowledge  

---

## 📝 How to Add More Questions  
You can easily add new questions to the quiz by editing **`data.py`**.  

Each question follows this format:  

```python
{
    "category": "Science",
    "question": "Water boils at 100°C at sea level.",
    "correct_answer": "True"
}
```

### Steps:  
1. Open **`data.py`**  
2. Find the `question_data` list  
3. Add your new question dictionary to the list  
4. Make sure the `correct_answer` is either `"True"` or `"False"` (case-sensitive)  

Example of adding a new question:  

```python
question_data.append({
    "category": "Geography",
    "question": "Mount Kilimanjaro is located in Kenya.",
    "correct_answer": "False"
})
```

Now when you run `main.py`, the new question will appear in the quiz 🚀  

---

## 🏆 Final Note  
This is a beginner-friendly but challenging project to practice **Python OOP, input handling, and modular code structure**.  
Perfect for portfolio or resume projects 🚀  
