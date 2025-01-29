# Quizller - A Python Quiz Game

## Description

This is a Python-based quiz game that utilizes **Object-Oriented Programming (OOP)** principles and a **Graphical User Interface (GUI)** built with Tkinter. The game presents a series of True/False questions fetched dynamically from the [Open Trivia Database API](https://opentdb.com/api_config.php), tracks the player's score, and provides real-time feedback.

<details>
  <summary>Click to see more</summary>
  This project demonstrates:
  - API integration for real-time question retrieval
  - GUI interaction using Tkinter
  - OOP concepts such as class-based structure and modular design
  - Score tracking and dynamic UI updates
</details>


## Features

- **Dynamic Question Fetching**: Retrieves quiz questions from an online API.
- **Graphical User Interface (GUI)**: Interactive game interface built with Tkinter.
- **Real-time Score Tracking**: Displays score updates during gameplay.
- **Instant Feedback**: Provides visual feedback for correct and incorrect answers.
- **Smooth Game Flow**: The game continues until all questions are answered.

![Quizller](/images/Quizller.PNG)

## Requirements

- Python 3.x
- `requests` module (pip install requests)
- `tkinter` (included in standard Python installation)

## How to Play

1. **Start the Quiz**:
   - Run the `main.py` script to start the game.
   
2. **Answer Questions**:
   - Click on the **True** or **False** buttons to submit your answer.

3. **Track Your Score**:
   - The score updates dynamically in the GUI.

4. **Game Completion**:
   - The game ends when all questions have been answered, displaying the final score.

## Code Structure

<details>
  <summary>Click to see more</summary>

### Files:

- **`main.py`**: Initializes and runs the game.
- **`question_model.py`**: Defines the `Question` class.
- **`quiz_brain.py`**: Manages game logic, question tracking, and scorekeeping.
- **`ui.py`**: Handles the Tkinter-based GUI interface.
- **`config.py`**: Stores theme colors and image paths.
- **`data.py`**: Fetches questions from the Open Trivia Database API.

### Key Classes and Functions:

- **`Question` (in `question_model.py`)**:
  - Stores quiz question text and correct answers.

- **`QuizBrain` (in `quiz_brain.py`)**:
  - Manages quiz progression and scoring.
  - `still_has_questions()`: Checks for remaining questions.
  - `next_question()`: Retrieves and formats the next question.
  - `check_answer(user_answer, correct_answer)`: Validates user responses.

- **`QuizInterface` (in `ui.py`)**:
  - Handles GUI setup and user interactions.
  - Displays quiz questions and manages buttons.

</details>

## How to Run

1. Clone or download the project files.
2. Ensure Python 3.x is installed.
3. Open a terminal and navigate to the project directory.
4. Run the following command to start the game:

```
python main.py
```

## Future Improvements

- **Difficulty Levels**: Introduce easy, medium, and hard modes.
- **Category Selection**: Allow users to choose quiz categories.
- **Leaderboard**: Implement a high-score tracking system.
- **Sound Effects**: Add audio feedback for correct/incorrect answers.

## Version

**Current Version:** 1.1.0

## Changelog

### v1.1.0
- **Added GUI interface** using Tkinter
- **Integrated API fetching** for real-time questions
- **Improved feedback system** with visual indicators
- **Optimized button interactions** to prevent spamming

### v1.0.0
- Initial text-based quiz implementation

## Credits

This project was created as an educational exercise to demonstrate **Object-Oriented Programming (OOP)** concepts and **GUI development** in Python.

