from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.logger import Logger
from random import choice

from data.qa import QuestionAnswerSet

quizzes = {
    "Quiz 1": [
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
    ],
    "Quiz 2": [
        QuestionAnswerSet(
            question="What is the primary goal of a persuasive speech?",
            answers=["To inform the audience", "To entertain the audience", "To convince the audience", "To confuse the audience"],
            correct_index=2
        ),
        QuestionAnswerSet(
            question="What is the best way to start a speech?",
            answers=["With a joke", "With a strong opening statement", "By apologizing", "By reading from your notes"],
            correct_index=1
        ),
        QuestionAnswerSet(
            question="What is the role of body language in public speaking?",
            answers=["To distract the audience", "To reinforce your message", "To replace verbal communication", "To confuse the audience"],
            correct_index=1
        ),
        QuestionAnswerSet(
            question="What should you do if the audience looks bored?",
            answers=["Speak louder", "Engage them with a question", "End the speech early", "Ignore them"],
            correct_index=1
        ),
        QuestionAnswerSet(
            question="What is the benefit of using visual aids in a speech?",
            answers=["To make the speech longer", "To clarify complex ideas", "To distract the audience", "To avoid speaking"],
            correct_index=1
        )
    ]
}

class QuizScreen(Screen):

    class QuizScreenCanvas(FloatLayout):
        def on_kv_post(self, base_widget):
            super().on_kv_post(base_widget)
            self.score = 0  # Initialize score
            self.current_question_index = 0  # Track the current question
            self.current_quiz = None  # Track the current quiz
            self.total_questions = 0  # Total number of questions in the selected quiz

        def load_next_question_answer_set(self) -> None:
            """
            Load the next question and set of answers in the quiz.
            """
            if self.current_question_index < self.total_questions:
                Logger.info("Loading next QuestionAnswerSet...")
                self.question_answer_set = self.current_quiz[self.current_question_index]
                self.ids.question_label.text = self.question_answer_set.question

                # Update the answer buttons with the new answers
                for i, answer in enumerate(self.question_answer_set.answers):
                    self.answer_buttons[i].text = answer
                    self.answer_buttons[i].disabled = False

                self.current_question_index += 1
            else:
                self.show_final_score()

        def select_quiz(self, quiz_name: str) -> None:
            """
            Select a quiz and load its questions.
            """
            Logger.info(f"Quiz selected: {quiz_name}")
            self.current_quiz = quizzes[quiz_name]
            self.total_questions = len(self.current_quiz)
            self.current_question_index = 0
            self.score = 0
            self.load_next_question_answer_set()

        def show_final_score(self) -> None:
            """
            Display the final score at the end of the quiz.
            """
            Logger.info(f"Quiz completed! Final score: {self.score}/{self.total_questions}")
            self.ids.question_label.text = f"Quiz Completed!\nYour Score: {self.score}/{self.total_questions}"

            # Disable the answer buttons
            for button in self.answer_buttons:
                button.disabled = True

