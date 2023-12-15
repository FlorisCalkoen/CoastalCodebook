import base64
from typing import Literal

import panel as pn


class MultipleChoiceQuestion:
    """A class to create and manage a multiple choice question widget.

    This class creates a multiple choice question using Panel widgets.
    It supports question text, multiple options, and a single correct answer.
    The correct answer is stored in an encrypted format for basic obfuscation.

    Attributes:
        question_text (str): The text of the question.
        options (Dict[str, str]): A dictionary of option keys and their text.
        correct_answer (str): The encrypted correct answer key.
        name (str): The name of the question widget.
        question_widget (pn.widgets.StaticText): The widget for displaying the question.
        options_widget (pn.widgets.RadioBoxGroup): The widget for displaying the options.
        submit_button (pn.widgets.Button): The button to submit the answer.
        feedback_widget (pn.widgets.StaticText): The widget to display feedback.

    Args:
        question_name: (str): The name for the question widget.
        question_text: (str): The question.
        question_options: (str): The options for the question,
        question_answerL: (str): The answer for the question,
    """

    def __init__(
        self,
        question_name: str,
        question_text: str,
        question_options: dict[str, str],
        question_answer: str,
        question_feedback: dict[Literal["correct", "incorrect"], str],
    ):
        self.name: str = question_name
        self.question_text: str = question_text
        self.options: dict[str, str] = question_options
        self.feedback = question_feedback
        self.correct_answer: str = self._encode_answer(question_answer)

        self.question_widget: pn.widgets.StaticText
        self.options_widget: pn.widgets.RadioBoxGroup
        self.submit_button: pn.widgets.Button
        self.feedback_widget: pn.widgets.StaticText
        self.options_inverse: dict[str, str] = {v: k for k, v in self.options.items()}
        self.create_widgets()

    def create_widgets(self) -> None:
        """Create and initialize the Panel widgets for the question."""
        self.question_widget = pn.widgets.StaticText(
            name=self.name, value=self.question_text
        )
        self.options_widget = pn.widgets.RadioBoxGroup(
            name="Options", options=list(self.options.values())
        )
        self.submit_button = pn.widgets.Button(name="Submit")
        self.feedback_widget = pn.widgets.StaticText()
        self.submit_button.on_click(self._check_answer)

    def _check_answer(self, event: pn.widgets.Button) -> None:
        """Check the selected answer against the correct answer.

        Args:
            event (pn.widgets.Button): The event triggered by the submit button.
        """
        selected_option = self.options_inverse[self.options_widget.value]
        decoded_answer = self._decode_answer(self.correct_answer)
        if selected_option == decoded_answer:
            self.feedback_widget.value = self.feedback["correct"]
        else:
            self.feedback_widget.value = self.feedback["incorrect"]

    def _encode_answer(self, plain_answer: str) -> str:
        """Encode the answer using base64.

        Args:
            plain_answer (str): The plain text answer to encode.

        Returns:
            str: The encoded answer.
        """
        return base64.b64encode(plain_answer.encode()).decode()

    def _decode_answer(self, encoded_answer: str) -> str:
        """Decode the encoded answer.

        Args:
            encoded_answer (str): The encoded answer to decode.

        Returns:
            str: The decoded answer.
        """
        return base64.b64decode(encoded_answer.encode()).decode()

    def serve(self) -> pn.Column:
        """Serve the question as a Panel column.

        Returns:
            pn.Column: The column containing the question and widgets.
        """
        return pn.Column(
            self.question_widget,
            self.options_widget,
            self.submit_button,
            self.feedback_widget,
        )


if __name__ == "__main__":
    question_data = {
        "question": (
            "Which coastal system do you typically find in tide-dominated coasts?"
        ),
        "options": {
            "a": "Mudflats",
            "b": "Open coasts",
            "c": "Cliffed coasts",
            "d": "Mixed sand and gravel beaches",
        },
        "answer": "a",  # Multiple correct answers
    }

    mcq = MultipleChoiceQuestion(
        question_name="Q1: Coastline Features Quiz",
        question_text=question_data["question"],
        question_options=question_data["options"],
        question_answer=question_data["answer"],
        question_feedback={
            "correct": "Well done, ...",
            "incorrect": "Unforunately that is not correct. Please consider...",
        },
    )
    print("done")
