from typing import Literal

import panel as pn

import coastal_dynamics as cd
from coastal_dynamics.question import Question


class MultipleSelectionQuestion(Question):
    """A class to create and manage multiple selection questions using Panel widgets.

    This class creates a multiple selection question using Panel widgets.
    It supports question text, multiple options, and multiple correct answers.
    The correct answers are stored in an encrypted format for basic obfuscation.

    Attributes:
        options (Dict[str, str]): A dictionary of option keys and their text.
        correct_answers (List[str]): The encrypted correct answer keys.
        options_widget (pn.widgets.CheckBoxGroup): The widget for displaying options.
        options_inverse (Dict[str, str]): Inverse mapping of options for easy lookup.
    """

    def __init__(
        self,
        question_name: str,
        question_text: str,
        question_options: dict[str, str],
        question_answers: list[str],
        question_feedback: dict[Literal["correct", "incorrect"], str],
    ):
        self.options = question_options
        self.correct_answers = question_answers
        self.options_widget: pn.widgets.CheckBoxGroup
        self.options_inverse = {v: k for k, v in self.options.items()}

        super().__init__(question_name, question_text, question_feedback)

    def create_widgets(self) -> None:
        """Create and initialize the Panel widgets for the question."""
        super().create_widgets()
        self.options_widget = pn.widgets.CheckBoxGroup(
            name="Options", options=list(self.options.values())
        )
        self.submit_button.on_click(self._check_answers)

    def _check_answers(self, event: pn.widgets.Button) -> None:
        """Check the selected answers against the correct ones."""
        selected_options = [
            self.options_inverse[opt] for opt in self.options_widget.value
        ]

        if set(cd.hash_answer(selected_options, "multiple_selection")) == set(
            self.correct_answers
        ):
            self.feedback_widget.value = self.feedback["correct"]
        else:
            self.feedback_widget.value = self.feedback["incorrect"]

    def serve(self) -> pn.Column:
        """Serve the complete question widget."""
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
        "answer": ["a", "c"],  # Multiple correct answers
    }

    msq = MultipleSelectionQuestion(
        question_name="Q1: Coastline Features Quiz",
        question_text=question_data["question"],
        question_options=question_data["options"],
        question_answers=cd.hash_answer(question_data["answer"], "multiple_selection"),
        question_feedback={
            "correct": (
                "Correct! Beaches and estuaries are common features of coastlines."
            ),
            "incorrect": "Incorrect! Try again. Please consider..",
        },
    )
    print("done")
