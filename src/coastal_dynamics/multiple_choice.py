from typing import Literal

import panel as pn

import coastal_dynamics as cd
from coastal_dynamics.question import Question


class MultipleChoiceQuestion(Question):
    """A class to create and manage a multiple choice question widget.

    This class creates a multiple choice question using Panel widgets.
    It supports question text, multiple options, and a single correct answer.
    The correct answer is stored in an encrypted format for basic obfuscation.

    Attributes:
        options (Dict[str, str]): A dictionary of option keys and their text.
        correct_answer (str): The encrypted correct answer key.
        options_widget (pn.widgets.RadioBoxGroup): The widget for displaying the options.
        options_inverse (Dict[str, str]): Inverse mapping of options for easy lookup.
    """

    def __init__(
        self,
        question_name: str,
        question_text: str,
        question_options: dict[str, str],
        question_answer: str,
        question_feedback: dict[Literal["correct", "incorrect"], str],
    ):
        self.options = question_options
        self.correct_answer = question_answer
        self.options_widget: pn.widgets.RadioBoxGroup
        self.options_inverse = {v: k for k, v in self.options.items()}

        super().__init__(question_name, question_text, question_feedback)

    def create_widgets(self) -> None:
        """Create and initialize the Panel widgets for the question."""
        super().create_widgets()
        self.options_widget = pn.widgets.RadioBoxGroup(
            name="Options", options=list(self.options.values())
        )
        self.submit_button.on_click(self._check_answer)

    def _check_answer(self, event: pn.widgets.Button) -> None:
        """Check the selected answer against the correct answer."""
        selected_option = self.options_inverse[self.options_widget.value]
        if (
            self.hash_answer(selected_option, question_type="multiple_choice")
            == self.correct_answer
        ):
            self.feedback_widget.value = self.feedback["correct"]
        else:
            self.feedback_widget.value = self.feedback["incorrect"]

    def serve(self) -> pn.Column:
        """Serve the question as a Panel column."""
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
        "answer": cd.hash_answer("a", "multiple_choice"),  # Multiple correct answers
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
    mcq.serve().show()
    print("done")
