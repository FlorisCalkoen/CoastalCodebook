import base64
from typing import Literal

import panel as pn


class Question:
    """Base class for different types of questions with encryption functionality.

    This class provides common functionalities for question widgets including encryption of answers.

    Attributes:
        name (str): The name of the question widget.
        question_text (str): The text of the question.
        feedback_widget (pn.widgets.StaticText): The widget to display feedback.
        submit_button (pn.widgets.Button): The button to submit the answer.
    """

    def __init__(
        self,
        question_name: str,
        question_text: str,
        question_feedback: dict[Literal["correct", "incorrect"], str],
    ):
        self.name = question_name
        self.question_text = question_text
        self.feedback = question_feedback
        self.create_widgets()

    def create_widgets(self) -> None:
        """Create and initialize the Panel widgets for the question."""
        self.question_widget = pn.widgets.StaticText(
            name=self.name, value=self.question_text
        )
        self.submit_button = pn.widgets.Button(name="Submit")
        self.feedback_widget = pn.widgets.StaticText()

    def serve(self) -> pn.Column:
        """Serve the question as a Panel column."""
        msg = "This method should be implemented by subclasses"
        raise NotImplementedError(msg)

    def check_answer(self, event) -> None:
        """Check the submitted answer against the correct answer."""
        msg = "This method should be implemented by subclasses"
        raise NotImplementedError(msg)

    def _encode_answer(self, plain_answer: str) -> str:
        """Encode the answer using base64."""
        return base64.b64encode(plain_answer.encode()).decode()

    def _decode_answer(self, encoded_answer: str) -> str:
        """Decode the encoded answer."""
        return base64.b64decode(encoded_answer.encode()).decode()
