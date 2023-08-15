import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root, questions):
        self.root = root
        self.questions = questions
        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", wraplength=400, font=("Arial", 12))
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(root, font=("Arial", 12))
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack()

        self.next_button = tk.Button(root, text="Next Question", command=self.next_question, state=tk.DISABLED)
        self.next_button.pack()

        self.update_question()

    def update_question(self):
        if self.current_question < len(self.questions):
            question = list(self.questions.keys())[self.current_question]
            self.question_label.config(text=question)
        else:
            self.show_score()

    def check_answer(self):
        user_answer = self.answer_entry.get().strip().lower()
        correct_answer = list(self.questions.values())[self.current_question].lower()

        if user_answer == correct_answer:
            self.score += 1

        self.submit_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.current_question += 1
        self.answer_entry.delete(0, tk.END)
        self.submit_button.config(state=tk.NORMAL)
        self.next_button.config(state=tk.DISABLED)
        self.update_question()

        if self.current_question == len(self.questions):
            self.next_button.config(state=tk.DISABLED)
            self.submit_button.config(state=tk.DISABLED)
            self.show_score()

    def show_score(self):
        messagebox.showinfo("Quiz Completed", f"Your score: {self.score}/{len(self.questions)}")
        self.root.destroy()

# Sample quiz questions
quiz_questions = {
    "What is the capital of France?": "Paris",
    "Which planet is known as the Red Planet?": "Mars",
    "What is the largest mammal?": "Blue Whale",
    "How many colours in rainbow ?":"7"
}

root = tk.Tk()
root.title("Quiz App")

quiz_app = QuizApp(root, quiz_questions)

root.mainloop()
