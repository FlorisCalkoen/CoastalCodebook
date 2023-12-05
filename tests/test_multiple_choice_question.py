from coastal_dynamics.questions.multiple_choice import (
    MultipleChoiceQuestion,
)


def test_multiple_choice_question_correct_answer():
    question_data = {
        "question": "What is the capital of France?",
        "options": {"a": "Paris", "b": "London", "c": "Berlin", "d": "Madrid"},
        "answer": "a",
    }

    mcq = MultipleChoiceQuestion(question_data, "Capital Cities Quiz")
    # Simulate user selecting the correct option
    mcq.options_widget.value = "Paris"
    mcq._check_answer(None)  # Trigger check answer event
    assert mcq.feedback_widget.value == "Correct!"


def test_multiple_choice_question_incorrect_answer():
    question_data = {
        "question": "What is the capital of France?",
        "options": {"a": "Paris", "b": "London", "c": "Berlin", "d": "Madrid"},
        "answer": "a",
    }

    mcq = MultipleChoiceQuestion(question_data, "Capital Cities Quiz")
    # Simulate user selecting an incorrect option
    mcq.options_widget.value = "London"
    mcq._check_answer(None)  # Trigger check answer event
    assert mcq.feedback_widget.value == "Incorrect, try again."
