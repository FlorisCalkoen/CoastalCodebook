from typing import Literal

import panel as pn

from coastal_dynamics.question import Question


class NumericQuestion(Question):
    """
    A class to create and manage a numeric answer question widget.

    This class creates a numeric question using Panel widgets.
    It supports a question text, numeric answer, and precision for the answer.

    Attributes:
        correct_answer (float): The correct numeric answer.
        precision (int): The precision of the numeric answer.
        answer_input (pn.widgets.FloatInput): The widget for inputting the answer.
    """

    def __init__(
        self,
        question_name: str,
        question_text: str,
        question_answer: float,
        question_feedback: dict[Literal["correct", "incorrect"], str],
        precision: int = 0,
    ):
        self.correct_answer = round(float(question_answer), precision)
        self.precision = precision
        self.answer_input: pn.widgets.FloatInput

        super().__init__(question_name, question_text, question_feedback)

    def create_widgets(self) -> None:
        """Create and initialize the Panel widgets for the question."""
        super().create_widgets()
        self.answer_input = pn.widgets.FloatInput(name="Your Answer")
        self.submit_button.on_click(self.check_answer)

    def check_answer(self, event) -> None:
        """Check the submitted answer against the correct answer."""
        try:
            user_answer = round(float(self.answer_input.value), self.precision)
            if user_answer == self.correct_answer:
                self.feedback_widget.value = self.feedback["correct"]
            else:
                self.feedback_widget.value = self.feedback["incorrect"]
        except ValueError:
            self.feedback_widget.value = "Please enter a valid number."

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
        "answer": 0.33,
        "kwargs": {"precision": 2},
    }

    nq = NumericQuestion(
        question_name="Q3: Simple numeric question",
        question_text=question_data["question"],
        question_answer=question_data["answer"],
        question_feedback={
            "correct": "Correct!...",
            "incorrect": "Incorrect, try again. Please consider that...",
        },
        **question_data["kwargs"],
    )
    print("done")
