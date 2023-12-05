from typing import Any

from coastal_dynamics.questions.multiple_choice import MultipleChoiceQuestion
from coastal_dynamics.questions.multiple_selection import MultipleSelectionQuestion
from coastal_dynamics.questions.numeric import NumericQuestion


class QuestionWidgetFactory:
    """
    A factory class for creating question widgets based on question data.

    Attributes:
        question_data (Dict[str, Any]): Dictionary containing data for the question.

    Methods:
        create_question_widget(): Creates a question widget based on the question data.
    """

    def __init__(self, question_data: dict[str, Any]):
        self.question_data = question_data

    def create_question_widget(self):
        """Creates a question widget based on the question data."""
        question_type = self.question_data.get("type")
        valid_types = ["multiple_choice", "multiple_selection", "numeric"]

        if question_type not in valid_types:
            raise ValueError(f"Unknown question type: {question_type}")

        if question_type == "multiple_choice":
            return self._create_multiple_choice_question()
        elif question_type == "multiple_selection":
            return self._create_multiple_selection_question()
        elif question_type == "numeric":
            return self._create_numeric_question()

    def _create_multiple_choice_question(self):
        return MultipleChoiceQuestion(
            question_name=self.question_data.get("name", ""),
            question_text=self.question_data.get("question", ""),
            question_options=self.question_data.get("options", {}),
            question_answer=self.question_data.get("answer", ""),
            **self.question_data.get("kwargs", {}),
        )

    def _create_multiple_selection_question(self):
        return MultipleSelectionQuestion(
            question_name=self.question_data.get("name", ""),
            question_text=self.question_data.get("question", ""),
            question_options=self.question_data.get("options", {}),
            question_answers=self.question_data.get("answers", []),
            **self.question_data.get("kwargs", {}),
        )

    def _create_numeric_question(self):
        return NumericQuestion(
            question_name=self.question_data.get("name", ""),
            question_text=self.question_data.get("question", ""),
            question_answer=self.question_data.get("answer", 0),
            **self.question_data.get("kwargs", {}),
        )


if __name__ == "__main__":

    def example():
        question_data = {
            "type": "multiple_choice",
            "name": "q1",
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
            "feedback": "...",
            "hint": "...",
        }
        factory = QuestionWidgetFactory(question_data)
        return factory.create_question_widget()

    widget = example()
