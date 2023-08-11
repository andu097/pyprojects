from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
SCORE = 0

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        #canvas
        self.canvas = Canvas(height=250, width=300)
        self.canvas.config(background='white', highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125, text='some text', font=('Arial', 10, 'italic'), width=280)

        #buttons
        self.check_image = PhotoImage(file='images/true.png')
        self.check_button = Button(image=self.check_image, highlightthickness=0, padx=50, pady=50, command=self.check_pressed)
        self.check_button.grid(row=2, column=0)
        self.cross_image = PhotoImage(file='images/false.png')
        self.cross_button = Button(image=self.cross_image, highlightthickness=0, padx=50, pady=50, command=self.false_pressed)
        self.cross_button.grid(row=2, column=1)

        # label
        self.label = Label(text=f"Score: {SCORE}", bg=THEME_COLOR, font=('Arial', 20, 'bold'))
        self.label.config(padx=20, pady=20)
        self.label.grid(row=0, column=1)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've run out of questions!")
            self.check_button.config(state="disabled")
            self.cross_button.config(state="disabled")

    def check_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
