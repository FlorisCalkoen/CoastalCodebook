from typing import Any

from coastal_dynamics.multiple_choice import MultipleChoiceQuestion
from coastal_dynamics.multiple_selection import MultipleSelectionQuestion
from coastal_dynamics.numeric import NumericQuestion
from coastal_dynamics.text import TextQuestion


class QuestionFactory:
    """
    A factory class for creating question widgets based on question data.

    Attributes:
        question_data (Dict[str, Any]): Dictionary containing data for the question.

    Methods:
        create_question_widget(): Creates a question widget based on the question data.
    """

    def __init__(self, question_data: dict[str, Any], serve=True):
        self.question_data = question_data
        self.question_widget = self.create_question_widget()

        if serve:
            self.question_widget.serve()

    def create_question_widget(self):
        question_type = self.question_data.get("type")
        valid_types = {
            "multiple_choice": self._create_multiple_choice_question,
            "multiple_selection": self._create_multiple_selection_question,
            "numeric": self._create_numeric_question,
            "text": self._create_text_question,
        }

        create_func = valid_types.get(question_type)
        if not create_func:
            msg = f"Unknown question type: {question_type}"
            raise ValueError(msg)

        return create_func()

    def _create_multiple_choice_question(self):
        required_fields = ["name", "question", "options", "answer", "feedback"]
        self._validate_required_fields(required_fields)

        return MultipleChoiceQuestion(
            question_name=self.question_data["name"],
            question_text=self.question_data["question"],
            question_options=self.question_data["options"],
            question_answer=self.question_data["answer"],
            question_feedback=self.question_data["feedback"],
        )

    def _create_multiple_selection_question(self):
        required_fields = ["name", "question", "options", "answer", "feedback"]
        self._validate_required_fields(required_fields)

        return MultipleSelectionQuestion(
            question_name=self.question_data["name"],
            question_text=self.question_data["question"],
            question_options=self.question_data["options"],
            question_answers=self.question_data["answer"],
            question_feedback=self.question_data["feedback"],
        )

    def _create_numeric_question(self):
        required_fields = ["name", "question", "answer", "feedback"]
        self._validate_required_fields(required_fields)

        return NumericQuestion(
            question_name=self.question_data["name"],
            question_text=self.question_data["question"],
            question_answer=self.question_data["answer"],
            question_feedback=self.question_data["feedback"],
            precision=self.question_data.get(
                "precision", 0
            ),  # Handle precision as optional
        )

    def _create_text_question(self):
        required_fields = ["name", "question", "answer", "feedback"]
        self._validate_required_fields(required_fields)

        return TextQuestion(
            question_name=self.question_data["name"],
            question_text=self.question_data["question"],
            question_answer=self.question_data["answer"],
            question_feedback=self.question_data["feedback"],
        )

    def _validate_required_fields(self, required_fields):
        for field in required_fields:
            if field not in self.question_data:
                raise ValueError(f"Missing required field: {field} in question data")

    def serve(self):
        return self.question_widget.serve()


if __name__ == "__main__":

    def example():
        question_data = {
            "name": "Q1-1",
            "type": "multiple_choice",
            "question": (
                "Which of the following is a common along the coast in the middle"
                " latitudes?"
            ),
            "options": {
                "a": "Salt marshes",
                "b": "Coral reefs",
                "c": "Tropical rainforests",
                "d": "Mangrove swamps",
            },
            "answer": "a",
            "feedback": {
                "correct": "Well done, ...",
                "incorrect": "Unforunately that is not correct. Please consider...",
            },
        }

        factory = QuestionFactory(question_data)
        return factory.create_question_widget()

    widget = example()
    print("Done")
