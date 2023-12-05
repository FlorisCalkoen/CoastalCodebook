from coastal_dynamics.questions.numeric import NumericQuestion


def test_numeric_question_correct_answer():
    question_data = {
        "question": "What is 2 + 2?",
        "answer": 4,  # Directly use the numeric answer
    }
    nq = NumericQuestion(question_data, "Test Question", precision=0)
    nq.answer_input.value = 4  # Simulate user input
    nq.check_answer(None)  # Trigger check answer event
    assert nq.feedback_widget.value == "Correct!"


def test_numeric_question_incorrect_answer():
    question_data = {
        "question": "What is 2 + 2?",
        "answer": 4,  # Directly use the numeric answer
    }
    nq = NumericQuestion(question_data, "Test Question", precision=0)
    nq.answer_input.value = 5  # Simulate user input
    nq.check_answer(None)  # Trigger check answer event
    assert nq.feedback_widget.value == "Incorrect, try again."
