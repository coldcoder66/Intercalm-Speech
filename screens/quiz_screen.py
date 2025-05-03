from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout

from intercalm.data.qa import QuestionAnswerSet

from kivy.logger import Logger
from random import choice

question_answer_sets   = [
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
            self.load_next_QuestionAnswerSet()

        def on_raindrop_select(self, instance):
            instance.md_bg_color = [0, 1, 0, 1]  # Glowing border effect

        def submit_answer(self, answer: int) -> None:
            """
            Submits an answer

            answer: int - The 0-based index of the answer
            """
            
            Logger.debug(f"Answer submitted: {answer}")
            
        def load_next_QuestionAnswerSet(self) -> None:
            """
            Load the next QuestionAnswerSet in the quiz.
            """
            Logger.debug("Loading next QuestionAnswerSet...")
            self.question_answer_set = choice(question_answer_sets)
            # Logic to load the next QuestionAnswerSet goes here

