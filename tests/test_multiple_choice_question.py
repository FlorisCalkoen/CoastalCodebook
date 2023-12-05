from coastal_dynamics.questions.multiple_choice import (
    MultipleChoiceQuestion,
)


def test_multiple_choice_question_correct_answer():
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
    )
    mcq.options_widget.value = "Mudflats"
    mcq._check_answer(None)  # Trigger check answer event
    assert mcq.feedback_widget.value == "Correct!"


def test_multiple_choice_question_incorrect_answer():
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
    )
    mcq.options_widget.value = "Open coasts"
    mcq._check_answer(None)  # Trigger check answer event
    assert mcq.feedback_widget.value == "Incorrect, try again."
