class QuestionAnswerSet:
    def __init__(self, question: str, answers: list[str], correct_index: int):
        """
        Initialize a QuestionAnswerSet object.

        text: str - The question text.
        answers: list[str] - A list of 4 possible answers.
        correct_index: int - The index of the correct answer (0-3).
        """
        self.question = question
        self.answers = answers
        self.correct_index = correct_index

    def is_correct(self, answer_index: int) -> bool:
        """
        Check if the given answer index is correct.

        answer_index: int - The index of the selected answer.
        """
        return answer_index == self.correct_index

    def get_correct_answer(self) -> str:
        """
        Retrieve the correct answer text.
        """
        return self.answers[self.correct_index]