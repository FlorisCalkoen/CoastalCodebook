import base64

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
        question_data (Dict[str, any]): The data for the question, including text, options, and the answer.
        name (str): The name for the question widget.
    """

    def __init__(self, question_data: dict[str, any], name: str, **kwargs):
        self.question_text: str = question_data["question"]
        self.options: dict[str, str] = question_data["options"]
        self.correct_answer: str = self._encode_answer(question_data["answer"])
        self.name: str = name
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
            self.feedback_widget.value = "Correct!"
        else:
            self.feedback_widget.value = "Incorrect, try again."

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
