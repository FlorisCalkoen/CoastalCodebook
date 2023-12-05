from coastal_dynamics.questions.multiple_selection import (
    MultipleSelectionQuestion,
)


def test_multiple_selection_question_correct_answer():
    question_data = {
        "question": "Which of the following are fruits?",
        "options": {"a": "Apple", "b": "Carrot", "c": "Banana", "d": "Potato"},
        "answers": ["a", "c"],
    }

    msq = MultipleSelectionQuestion(question_data, "Fruits Quiz")
    # Simulate user selecting the correct options
    msq.options_widget.value = ["Apple", "Banana"]
    msq._check_answers(None)  # Trigger check answers event
    assert msq.feedback_widget.value == "Correct!"


def test_multiple_selection_question_incorrect_answer():
    question_data = {
        "question": "Which of the following are fruits?",
        "options": {"a": "Apple", "b": "Carrot", "c": "Banana", "d": "Potato"},
        "answers": ["a", "c"],
    }

    msq = MultipleSelectionQuestion(question_data, "Fruits Quiz")
    # Simulate user selecting incorrect options
    msq.options_widget.value = ["Carrot", "Potato"]
    msq._check_answers(None)  # Trigger check answers event
    assert msq.feedback_widget.value == "Incorrect, try again."


def test_multiple_selection_question_partial_correct_answer():
    question_data = {
        "question": "Which of the following are fruits?",
        "options": {"a": "Apple", "b": "Carrot", "c": "Banana", "d": "Potato"},
        "answers": ["a", "c"],
    }

    msq = MultipleSelectionQuestion(question_data, "Fruits Quiz")
    # Simulate user selecting partially correct options
    msq.options_widget.value = ["Apple"]
    msq._check_answers(None)  # Trigger check answers event
    assert msq.feedback_widget.value == "Incorrect, try again."


if __name__ == "__main__":
    test_multiple_selection_question_correct_answer()
    print("dfone")
