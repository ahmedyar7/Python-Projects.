from tkinter import *

THEME_COLOR = "#375362"
QNA_COORDINATES = (150, 125)
QNA_FONT = ("Ariel", 17, "italic")


class QuizInterface:

    def __init__(self) -> None:

        # * Window Setup:
        self.window = Tk()
        self.window.title("Quizzy App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0")
        self.score_label.config(bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        # * Canvas setup:
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            QNA_COORDINATES, text="Random", font=QNA_FONT
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        # * Buttons:

        true_img = PhotoImage(file="Quzziy App/images/true.png")
        false_img = PhotoImage(file="Quzziy App/images/false.png")

        self.true_button = Button(
            image=true_img, highlightthickness=0, padx=20, pady=20
        )
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(
            image=false_img, highlightthickness=0, padx=20, pady=20
        )
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()
