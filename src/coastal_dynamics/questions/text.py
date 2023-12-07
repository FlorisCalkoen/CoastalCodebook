from typing import Literal

import panel as pn


class TextQuestion:
    """
    A class to create and manage a numeric answer question widget.

    This class creates a numeric question using Panel widgets.
    It supports a question text, numeric answer, and precision for the answer.

    Attributes:
        question_text (str): The text of the question.
        correct_answer (float): The correct numeric answer.
        precision (int): The precision of the numeric answer.
        name (str): The name of the question widget.
        question_widget (pn.widgets.StaticText): The widget for displaying the question.
        answer_input (pn.widgets.FloatInput): The widget for inputting the answer.
        submit_button (pn.widgets.Button): The button to submit the answer.
        feedback_widget (pn.widgets.StaticText): The widget to display feedback.

    Args:
        question_name: (str): The name for the question widget.
        question_text: (str): The question.
        question_answer: (str): The answer for the question,
    """

    def __init__(
        self,
        question_name: str,
        question_text: str,
        question_answer: str,
        question_feedback: dict[Literal["correct", "incorrect"], str],
        **kwargs,
    ):
        self.name: str = question_name
        self.question_text: str = question_text
        self.correct_answer: str = str(question_answer).lower()
        self.feedback = question_feedback
        self.create_widgets()

    def create_widgets(self) -> None:
        """Create and initialize the Panel widgets for the question."""
        self.question_widget = pn.widgets.StaticText(
            name=self.name, value=self.question_text
        )
        self.answer_input = pn.widgets.TextInput(
            placeholder="Enter your answer here..."
        )
        self.submit_button = pn.widgets.Button(name="Submit")
        self.feedback_widget = pn.widgets.StaticText()
        self.submit_button.on_click(self.check_answer)

    def check_answer(self, event) -> None:
        """Check the submitted answer against the correct answer."""
        try:
            user_answer = str(self.answer_input.value).lower()

            if user_answer == self.correct_answer:
                self.feedback_widget.value = self.feedback["correct"]
            else:
                self.feedback_widget.value = self.feedback["incorrect"]
        except ValueError:
            self.feedback_widget.value = "Please enter valid text."

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
        question_answer=question_data["answer"],
        question_feedback={
            "correct": "Correct! Indeed, ...",
            "incorrect": "Incorrect. Please consider ...",
        },
    )
    print("done")
