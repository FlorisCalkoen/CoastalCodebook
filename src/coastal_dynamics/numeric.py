from typing import Literal

import numpy as np
import panel as pn

import coastal_dynamics as cd
from coastal_dynamics.question import Question


class NumericQuestion(Question):
    """
    A class to create and manage a numeric answer question widget.

    This class creates a numeric question using Panel widgets.
    It supports a question text, numeric answer, and sig_figs for the answer.

    Attributes:
        correct_answer (float): The correct numeric answer.
        sig_figs (int): The number of significant figures of the numeric answer.
        answer_input (pn.widgets.FloatInput): The widget for inputting the answer.
    """

    def __init__(
        self,
        question_name: str,
        question_text: str,
        question_answer: str,
        question_feedback: dict[Literal["correct", "incorrect"], str],
        sig_figs: int | None = None,
    ):
        self.correct_answer = question_answer
        self.sig_figs = sig_figs
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
            user_answer = float(self.answer_input.value)

            if self.sig_figs:
                user_answer = np.format_float_positional(
                    user_answer,
                    precision=self.sig_figs,
                    unique=False,
                    fractional=False,
                    trim="k",
                )

            hashed_user_answer = self.hash_answer(
                user_answer, "numeric", sig_figs=self.sig_figs
            )

            if hashed_user_answer == self.correct_answer:
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
        "answer": 35,
        "sig_figs": 2,
    }

    nq = NumericQuestion(
        question_name="Q3: Simple numeric question",
        question_text=question_data["question"],
        question_answer=cd.hash_answer(
            np.format_float_positional(
                float(question_data["answer"]),
                precision=question_data["sig_figs"],
                unique=False,
                fractional=False,
                trim="k",
            ),
            "numeric",
        ),
        question_feedback={
            "correct": "Correct!...",
            "incorrect": "Incorrect, try again. Please consider that...",
        },
        sig_figs=question_data["sig_figs"],
    )
    nq.serve().show()
    print("done")
