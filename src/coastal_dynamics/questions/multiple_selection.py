import base64

import panel as pn


class MultipleSelectionQuestion:
    """A class to create and manage multiple selection questions using Panel widgets.

    This class creates a multiple selection using Panel widgets.
    It supports question text, multiple options, and a multiple correct answers.
    The correct answers are stored in an encrypted format for basic obfuscation.

    Attributes:
        question_text (str): The text of the question.
        options (Dict[str, str]): A dictionary of option keys and their text.
        correct_answers (List[str]): A list of base64-encoded correct answer keys.
        name (str): The name of the question widget.
        question_widget (pn.widgets.StaticText): Panel widget for displaying the question.
        options_widget (pn.widgets.CheckBoxGroup): Panel widget for displaying options.
        submit_button (pn.widgets.Button): Button widget for submitting the answer.
        feedback_widget (pn.widgets.StaticText): Widget for showing feedback.
        options_inverse (Dict[str, str]): Inverse mapping of options for easy lookup.

    Args:
        question_name: (str): The name for the question widget.
        question_text: (str): The question.
        question_options: (str): The options for the question,
        question_answers: (str): The answer for the question,
    """

    def __init__(
        self,
        question_name: str,
        question_text: str,
        question_options: dict[str, str],
        question_answers: list[str],
        **kwargs,
    ):
        self.name: str = question_name
        self.question_text: str = question_text
        self.options: dict[str, str] = question_options
        self.correct_answers: list[str] = [
            self._encode_answer(ans) for ans in question_answers
        ]
        self.create_widgets()
        self.options_inverse: dict[str, str] = {v: k for k, v in self.options.items()}

    def create_widgets(self) -> None:
        """Creates the Panel widgets for the question."""
        self.question_widget = pn.widgets.StaticText(
            name=self.name, value=self.question_text
        )
        self.options_widget = pn.widgets.CheckBoxGroup(
            name="Options", options=list(self.options.values())
        )
        self.submit_button = pn.widgets.Button(name="Submit")
        self.feedback_widget = pn.widgets.StaticText()
        self.submit_button.on_click(self._check_answers)

    def _check_answers(self, event: pn.widgets.Button) -> None:
        """Checks the selected answers against the correct ones."""
        selected_options = [
            self.options_inverse[opt] for opt in self.options_widget.value
        ]
        decoded_answers = [
            self._decode_answer(enc_ans) for enc_ans in self.correct_answers
        ]
        if set(selected_options) == set(decoded_answers):
            self.feedback_widget.value = "Correct!"
        else:
            self.feedback_widget.value = "Incorrect, try again."

    def _encode_answer(self, plain_answer: str) -> str:
        """Encodes the answer using base64."""
        return base64.b64encode(plain_answer.encode()).decode()

    def _decode_answer(self, encoded_answer: str) -> str:
        """Decodes the answer from base64."""
        return base64.b64decode(encoded_answer.encode()).decode()

    def serve(self) -> pn.Column:
        """Serves the complete question widget."""
        return pn.Column(
            self.question_widget,
            self.options_widget,
            self.submit_button,
            self.feedback_widget,
        )


if __name__ == "__main__":
    question_data = {
        "question": "Select all features commonly found along a coastline",
        "options": {
            "a": "Beaches",
            "b": "Glaciers",
            "c": "Estuaries",
            "d": "Mountains",
        },
        "answers": ["a", "c"],  # Multiple correct answers
    }

    mcq = MultipleSelectionQuestion(
        question_name="Q1: Coastline Features Quiz",
        question_text=question_data["question"],
        question_options=question_data["options"],
        question_answers=question_data["answers"],
    )
    print("done")
