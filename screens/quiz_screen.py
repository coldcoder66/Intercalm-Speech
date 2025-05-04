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
            self.load_next_question_answer_set()

        # def on_raindrop_select(self, instance):
        #     instance.md_bg_color = [0, 1, 0, 1]  # Glowing border effect

        def submit_answer(self, answer: int) -> None:
            """
            Submits an answer

            answer: int - The 0-based index of the answer button clickedq
            """
            # TODO set level to debug
            Logger.info(f"Answer submitted: {answer}")
            
        def load_next_question_answer_set(self) -> None:
            """
            Load the next a question and set of answers in the quiz.
            """
            # TODO set level to debug
            Logger.info("Loading next QuestionAnswerSet...")
            # Pick a random QuestionAnswerSet from the list
            self.question_answer_set = choice(question_answer_sets)

            # TODO these lookups are aweful! try out namespace search
            answer_button_group = self.children[0].children[0].children[1].children
            question_label = self.children[0].children[0].children[2].children[0]

            # Update the question_label with the new question
            question_label.text = self.question_answer_set.question

            # Update the answer buttons with the new answers
            for i, answer in enumerate(self.question_answer_set.answers):
                answer_button_group[i].text = answer

