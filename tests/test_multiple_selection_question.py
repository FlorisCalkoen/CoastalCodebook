from coastal_dynamics.multiple_selection import (
    MultipleSelectionQuestion,
)


def test_multiple_selection_question_correct_answer():
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
        question_answers=question_data["answer"],
    )
    # Simulate user selecting the correct options
    msq.options_widget.value = ["Beaches", "Estuaries"]
    msq._check_answers(None)  # Trigger check answers event
    assert msq.feedback_widget.value == "Correct!"


def test_multiple_selection_question_incorrect_answer():
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
        question_answers=question_data["answer"],
    )
    # Simulate user selecting the correct options
    msq.options_widget.value = ["Mountains", "Glaciers"]
    msq._check_answers(None)  # Trigger check answers event
    assert msq.feedback_widget.value == "Incorrect, try again."


def test_multiple_selection_question_partial_correct_answer():
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
        question_answers=question_data["answer"],
    )
    # Simulate user selecting the correct options
    msq.options_widget.value = ["Estuaries"]
    msq._check_answers(None)  # Trigger check answers event
    assert msq.feedback_widget.value == "Incorrect, try again."


if __name__ == "__main__":
    test_multiple_selection_question_correct_answer()
    print("dfone")
