from config import * 
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    """
    GUI for the Quiz Game.

    Attributes:
        quiz (QuizBrain): The QuizBrain object managing the quiz logic.
    """
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.main_window_setup()
        self.true_button_setup()
        self.false_button_setup()
        self.canvas_field()
        self.score_field()
        self.score_label()
        self.get_next_question()

    def score_label(self):
        """Set up the score label."""
        self.score_label_text = Label(width=5, height=2, text="Score", font=("Arial", 20, "italic"), bg=THEME_COLOR, fg="white")
        self.score_label_text.grid(row=0, column=1, sticky="E", columnspan=1)

    def score_field(self):
        """Set up the score field with an image and text."""
        self.score_img = PhotoImage(file=SCORE_IMG, width=150, height=150)
        self.score_canvas = Canvas(width=150, height=150, bg=THEME_COLOR, borderwidth=0, highlightthickness=0)
        self.score_canvas.create_image(75, 75, image=self.score_img)
        self.score_text = self.score_canvas.create_text(75, 75, text="0", font=("Arial", 20, "bold"), fill="white")
        self.score_canvas.grid(row=0, column=2, sticky="E", columnspan=1)

    def canvas_field(self):
        """Set up the canvas field with card images, title text, and question text."""
        self.canvas = Canvas(width=400, height=350, highlightthickness=0, bg="white")
        self.canvas.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

        self.question_text = self.canvas.create_text(200, 175, text="", font=("Arial", 15, "italic"), width=380)

    def false_button_setup(self):
        """Set up the False button with an image and command."""
        self.false_button_img = PhotoImage(file=FALSE_IMG, width=150, height=150)
        self.false_button = Button(image=self.false_button_img, width=150, height=150, bg=THEME_COLOR, highlightthickness=0, borderwidth=0, command=self.false_pressed)
        self.false_button.grid(column=2, row=2)

    def true_button_setup(self):
        """Set up the True button with an image and command."""
        self.true_button_img = PhotoImage(file=TRUE_IMG, width=150, height=150)
        self.true_button = Button(image=self.true_button_img, width=150, height=150, bg=THEME_COLOR, highlightthickness=0, borderwidth=0, command=self.true_pressed)
        self.true_button.grid(column=1, row=2, columnspan=1)

    def main_window_setup(self):
        """Configure the main application window."""
        self.main_window = Tk()
        self.main_window.title("Quizller")
        self.main_window.config(bg=THEME_COLOR, padx=30, pady=30)
        self.main_window.resizable(0, 0)

    def get_next_question(self):
        """Fetch and display the next question or show end message."""
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_canvas.itemconfig(self.score_text, text=f"{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz! :D")
            self.disable_buttons()

    def true_pressed(self):
        """Handle True button press and provide feedback."""
        self.disable_buttons()
        correct_answer = self.quiz.current_question.answer
        self.give_feedback(self.quiz.check_answer("True", correct_answer))  # Pass both answers
        self.main_window.after(1000, self.enable_buttons)  # Re-enable the buttons after 1 second

    def false_pressed(self):
        """Handle False button press and provide feedback."""
        self.disable_buttons()
        correct_answer = self.quiz.current_question.answer
        self.give_feedback(self.quiz.check_answer("False", correct_answer))  # Pass both answers
        self.main_window.after(1000, self.enable_buttons)  # Re-enable the buttons after 1 second

    def give_feedback(self, is_right):
        """Provide visual feedback on the answer correctness."""
        if is_right:
            self.canvas.config(bg=RIGHT_COLOR)
        else:
            self.canvas.config(bg=WRONG_COLOR)
        self.main_window.after(1000, self.get_next_question)

    def disable_buttons(self):
        """Disable the True and False buttons."""
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

    def enable_buttons(self):
        """Re-enable the True and False buttons."""
        self.true_button.config(state="normal")
        self.false_button.config(state="normal")

    def run(self):
        """Start the Tkinter main event loop."""
        self.main_window.mainloop()