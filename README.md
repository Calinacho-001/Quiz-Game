# Simple Python Quiz Game

## Description

This is a simple Python quiz game that demonstrates the use of **Object-Oriented Programming (OOP)** principles. The game presents a series of True/False questions, tracks the player's score, and provides feedback on each answer. The project is designed to showcase the basics of Python classes and their interaction, making it a great starting point for those learning OOP.

This is the first version of the quiz game, and future versions will include more complexity, additional question categories, and even a GUI interface.

## Features

- **True/False Quiz**: Players answer True/False questions.
- **Score Tracking**: The game keeps track of the player's score throughout the quiz.
- **Feedback**: Provides feedback after each answer, including the correct answer.
- **Game Flow**: The game continues asking questions until all are answered.

## Requirements

- Python 3.x

## How to Play

1. **Start the Quiz**:
   - Run the `main.py` script to start the quiz.
   
2. **Answer Questions**:
   - The quiz will ask a series of True/False questions. Respond by typing "True" or "False" and press Enter.

3. **Track Your Score**:
   - After each question, the game will inform you if your answer is correct and show your current score.

4. **End of Quiz**:
   - Once all the questions have been answered, your final score will be displayed.

## Code Structure

### Files:

- **`data.py`**: Contains the list of quiz questions and answers.
- **`question_model.py`**: Defines the `Question` class, which holds the question text and the correct answer.
- **`quiz_brain.py`**: Manages the quiz logic, checks answers, and keeps track of the score.
- **`main.py`**: The entry point of the program, which initializes the quiz and runs the game.

### Key Classes and Functions:

- **`Question` (in `question_model.py`)**:
  - Stores the text and correct answer for each question.
  
- **`QuizBrain` (in `quiz_brain.py`)**:
  - `__init__(self, q_list)`: Initializes the quiz with a list of questions.
  - `still_has_questions()`: Checks if there are more questions to ask.
  - `next_question()`: Asks the next question and checks the player's answer.
  - `check_answer(user_answer, correct_answer)`: Compares the player's answer with the correct answer and updates the score.

- **`main.py`**:
  - Initializes the quiz by creating `Question` objects from `data.py` and starts the game loop, asking questions one by one.

## How to Run

1. Clone or download the project files.
2. Make sure Python 3.x is installed on your computer.
3. Open a terminal and navigate to the project directory.
4. Run the following command to start the quiz:



```bash
python main.py
```
## Future Improvements

- **More Question Categories**: The next version will include different categories, such as general knowledge, science, history, etc.
- **Graphical User Interface (GUI)**: Plans to implement a GUI using a library like `Tkinter` or `Pygame` for a more interactive experience.
- **Difficulty Levels**: Introduce different difficulty levels with more challenging questions.
- **Leaderboard**: Track and display high scores for multiple players.

## Credits

This project was created as a simple exercise to demonstrate Object-Oriented Programming concepts in Python. Future versions will expand on these concepts and add more features.