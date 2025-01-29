import html

class QuizBrain:
    """
    Manages the logic for the quiz game.

    Attributes:
        question_number (int): The current question index.
        question_list (list): List of Question objects.
        score (int): Player's score.
    """
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        """Check if there are more questions in the quiz."""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Retrieve the next question from the list."""
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer, correct_answer):
        """Check if the player's answer is correct."""
        self.correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False