from typing import Literal

import panel as pn

import coastal_dynamics as cd
from coastal_dynamics.question import Question


class TextQuestion(Question):
    """
    A class to create and manage a text answer question widget.

    This class creates a text question using Panel widgets.
    It supports a question text and a text answer.

    Attributes:
        correct_answer (str): The correct text answer.
        answer_input (pn.widgets.TextInput): The widget for inputting the answer.
    """

    def __init__(
        self,
        question_name: str,
        question_text: str,
        question_answer: str,
        question_feedback: dict[Literal["correct", "incorrect"], str],
    ):
        self.correct_answer = question_answer
        self.answer_input: pn.widgets.TextInput

        super().__init__(question_name, question_text, question_feedback)

    def create_widgets(self) -> None:
        """Create and initialize the Panel widgets for the question."""
        super().create_widgets()
        self.answer_input = pn.widgets.TextInput(
            placeholder="Enter your answer here..."
        )
        self.submit_button.on_click(self.check_answer)

    def check_answer(self, event) -> None:
        """Check the submitted answer against the correct answer."""
        user_answer = self.hash_answer(str(self.answer_input.value).lower(), "text")
        if user_answer == self.correct_answer:
            self.feedback_widget.value = self.feedback["correct"]
        else:
            self.feedback_widget.value = self.feedback["incorrect"]

    def serve(self) -> pn.Column:
        """Serve the question as a Panel column."""
        return pn.Column(
            self.question_widget,
            self.answer_input,
            self.submit_button,
            self.feedback_widget,
        )


if __name__ == "__main__":
    question_data = {
        "question": "What is the relative importance of S2 vs M2?",
        "answer": "Some answer",
    }

    tq = TextQuestion(
        question_name="Q3: Simple textual question",
        question_text=question_data["question"],
        question_answer=cd.hash_answer(question_data["answer"], "text"),
        question_feedback={
            "correct": "Correct! Indeed, ...",
            "incorrect": "Incorrect. Please consider ...",
        },
    )
    tq.serve().show()
    print("done")
