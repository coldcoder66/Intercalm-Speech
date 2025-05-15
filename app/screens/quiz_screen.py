from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.logger import Logger
from random import choice

from data.qa import QuestionAnswerSet

question_answer_sets = [
    QuestionAnswerSet(
        question="What is the most important aspect of public speaking?",
        answers=["Speaking loudly", "Engaging the audience", "Using complex vocabulary", "Memorizing the speech"],
        correct_index=1
    ),
    QuestionAnswerSet(
        question="What should you do if you forget your next point during a speech?",
        answers=["Pause and take a deep breath", "Apologize to the audience", "End the speech immediately", "Skip to the conclusion"],
        correct_index=0
    ),
    QuestionAnswerSet(
        question="How can you make your speech more engaging?",
        answers=["Use stories and examples", "Speak as quickly as possible", "Avoid eye contact", "Focus on technical terms"],
        correct_index=0
    ),
    QuestionAnswerSet(
        question="What is the purpose of practicing your speech beforehand?",
        answers=["To memorize every word", "To improve confidence and delivery", "To avoid using notes", "To impress the audience"],
        correct_index=1
    ),
    QuestionAnswerSet(
        question="What is a good way to handle nervousness before speaking?",
        answers=["Take deep breaths and focus on your message", "Avoid preparing for the speech", "Drink a lot of coffee", "Ignore the audience"],
        correct_index=0
    )
]

class QuizScreen(Screen):

    class QuizScreenCanvas(FloatLayout):
        def on_kv_post(self, base_widget):
            super().on_kv_post(base_widget)
            self.load_next_question_answer_set()

        def submit_answer(self, answer: int) -> None:
            """
            Submits an answer

            answer: int - The 0-based index of the answer button clicked
            """
            Logger.info(f"Answer submitted: {answer}")
            if self.question_answer_set.is_correct(answer):
                Logger.info("Correct answer!")
                self.guess_label.text = "Correct!"
                self.guess_label.color = [0, 1, 0, 1]  # Green color for correct answer
                self.next_question_button.disabled = False
            else:
                Logger.info("Incorrect answer!")
                self.guess_label.text = f"Incorrect!"
                self.guess_label.color = [1, 0, 0, 1]  # Red color for incorrect answer

        def load_next_question_answer_set(self) -> None:
            """
            Load the next question and set of answers in the quiz.
            """
            Logger.info("Loading next QuestionAnswerSet...")

            # Pick a random QuestionAnswerSet from the list
            self.question_answer_set = choice(question_answer_sets)

            # Update the question_label with the new question
            self.question_label.text = self.question_answer_set.question

            # Update the answer buttons with the new answers
            for i, answer in enumerate(self.question_answer_set.answers):
                self.answer_buttons[i].text = answer

            # Reset the guess label
            self.guess_label.text = ""

            self.next_question_button.disabled = True

