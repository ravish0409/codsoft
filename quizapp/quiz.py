import requests
import tkinter as tk
from tkinter import messagebox
import random
import re
from PIL import Image, ImageTk
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")

        self.category = 18  # Computer Science category
        self.difficulty = "easy"
        self.num_questions = 10
        self.quiz_questions = []
        self.current_question_index = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", wraplength=400, justify="center", font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.answer_buttons = []

        self.next_button = tk.Button(root, text="Next Question", font=("Arial", 12), state=tk.DISABLED, command=self.next_question)
        self.next_button.pack(pady=10)

        self.wrong_answers = 0
        self.max_wrong_attempts = 4

        self.get_quiz_questions()
        self.ask_current_question(self.current_question_index + 1)

    def get_quiz_questions(self):
        url = f"https://opentdb.com/api.php?amount={self.num_questions}&category={self.category}&difficulty={self.difficulty}&type=multiple"
        response = requests.get(url)
        data = response.json()
        self.quiz_questions = data['results']
        random.shuffle(self.quiz_questions)

    def ask_current_question(self, tr):
        if self.current_question_index < self.num_questions:
            question_data = self.quiz_questions[self.current_question_index]
            question = self.clean_text(question_data['question'])
            answers = [self.clean_text(answer) for answer in question_data['incorrect_answers'] + [question_data['correct_answer']]]
            random.shuffle(answers)

            self.question_label.config(text=f"{tr}. {question}")

            for button in self.answer_buttons:
                button.destroy()
            self.answer_buttons = []

            if hasattr(self, "button_frame"):
                self.button_frame.destroy()

            max_button_width = max(len(answer) for answer in answers)

            self.button_frame = tk.Frame(self.root)
            self.button_frame.pack()

            for i, answer in enumerate(answers):
                button = tk.Button(self.button_frame, text=answer, font=("Arial", 12), command=lambda ans=answer: self.check_answer(ans), anchor="w", padx=10, width=max_button_width + 4)
                button.pack(fill="x",padx=3, pady=3)  # Using fill="x" to ensure buttons stretch horizontally
                self.answer_buttons.append(button)

            self.next_button.config(state=tk.DISABLED)


    def clean_text(self, text):
        return re.sub(r'[^a-zA-Z0-9\s]', '', text)

    def check_answer(self, selected_answer):
        correct_answer = self.quiz_questions[self.current_question_index]['correct_answer']

        if selected_answer == correct_answer:
            self.score += 1
            messagebox.showinfo("Result", "Correct!")
        else:
            self.wrong_answers += 1
            remaining_attempts = self.max_wrong_attempts - self.wrong_answers
            messagebox.showinfo("Result", f"Incorrect. The correct answer is {correct_answer}. You have {remaining_attempts} attempts left.")

        self.current_question_index += 1
        if self.wrong_answers >= self.max_wrong_attempts or self.current_question_index >= self.num_questions:
            self.finish_quiz()
        else:
            self.next_button.config(state=tk.NORMAL)

        for button in self.answer_buttons:
            button.config(state=tk.DISABLED)

    def next_question(self):
        self.ask_current_question(self.current_question_index + 1)
        self.next_button.config(state=tk.DISABLED)

    def finish_quiz(self):
        if self.score == self.num_questions:
            congrats_message = "Congratulations! 🎉🎉 You scored a perfect score in the quiz!"
            messagebox.showinfo("Quiz Finished", congrats_message)
        else:
            messagebox.showinfo("Quiz Finished", f"You scored {self.score} out of {self.num_questions}.")
        self.root.quit()



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quiz App")
    root.minsize(width=500, height=320)  # Set maximum window size

    # Load the background image using Pillow
    background_image = Image.open("background.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # Create a label to display the background image
    background_label = tk.Label(root, image=background_photo)
    background_label.place(relwidth=1, relheight=1)  # Cover the entire window

    app = QuizApp(root)
    root.mainloop()

