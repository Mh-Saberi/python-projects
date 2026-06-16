# 🎯 Number Guesser Game

A simple command-line game where the user guesses a randomly generated number, with helpful hints and scoring logic.

## 📁 Project Structure
```
number_guesser/
│
├── src/
│ ├── game_logic/
│ │ ├── init.py
│ │ ├── hint_generator.py # Generates hints for the player
│ │ ├── number_generator.py # Handles number generation
│ │ ├── quit.py # Quit logic
│ │ ├── scorer.py # Scoring system
│ │
│ ├── utils/
│ │ ├── init.py
│ │ └── input_validator.py # Validates user input
│ │
│ └── main.py # Entry point of the game
│
├── README.md
└── requirements.txt
```

## 🚀 How to Run
```bash
python src/main.py
```


## ✅ Features

    🎲 Random number generation

    🔢 User input validation

    💡 Hint system to guide the player

    🧮 Scoring and replay logic

    ❌ Quit option available

## 🐍 Requirements

    Python 3.7 or higher

🔧 Future Improvements

    Add difficulty levels (easy/medium/hard)

    Track high scores

    Add logging or save user progress

    Make a GUI version using tkinter or PyQt

