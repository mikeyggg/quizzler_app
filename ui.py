THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain



class QuizInterface:



    def __init__(self, quiz_brain : QuizBrain ):


        self.answer = ""
        self.quiz = quiz_brain
        self.font = ("Arial",20,"italic")
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.window.geometry("350x500")

        self.canvas = Canvas(self.window,bg=THEME_COLOR,height=250,width=300,background="white",highlightthickness=0,bd =0)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=40)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text = "grr",
            fill = THEME_COLOR,
            font=("Arial",20,"italic"),
            width= 270
        )

        self.top_text = Label(self.window,text=f'Score: {self.score}',bg=THEME_COLOR,fg="white",font=("Arial",15),justify="right")
        self.top_text.grid(row=0,column=1)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image= true_image,background=THEME_COLOR,highlightthickness=0,bd = 0,command=self.true_answer)
        self.true_button.grid(row=2,column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image= false_image,background=THEME_COLOR,highlightthickness=0,bd = 0,command=self.false_answer)
        self.false_button.grid(row=2,column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f'You have finished the quiz.\nFinal score: {self.score}')
            self.true_button.config(state=DISABLED)
            self.false_button.config(state=DISABLED)

    def true_answer(self):
        self.answer = "True"
        self.check_answer()

    def false_answer(self):

        self.answer = "False"
        self.check_answer()

    def reset_color(self):

        self.top_text.config(bg=THEME_COLOR)
        self.window.config(bg=THEME_COLOR)

    def check_answer(self):

        correct_answer = self.quiz.check_answer(self.answer)

        if correct_answer == self.answer:

            self.score += 1
            self.top_text.config(text=f'Score: {self.score}')
            self.get_next_question()
            self.window.config(bg="green")
            self.top_text.config(bg="green")
            self.window.after(500,self.reset_color)


        else:

            self.get_next_question()
            self.window.config(bg="red")
            self.top_text.config(bg="red")
            self.window.after(500, self.reset_color)


