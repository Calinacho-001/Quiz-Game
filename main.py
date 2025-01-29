from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

#---------- Initialize Question Bank -----------#
question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

#---------- Initialize Quiz -----------#
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

#---------- Start the GUI -----------#
quiz_ui.run()

# Note: The commented code below was part of the previous CLI version.
# while quiz.still_has_questions():
#     quiz.next_question()

# print("You've successfully finished the quiz!")
# print(f"Your final score is {quiz.score}/{quiz.question_number}")