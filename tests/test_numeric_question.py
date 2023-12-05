from coastal_dynamics.questions.numeric import NumericQuestion


def test_numeric_question_correct_answer():
    question_data = {
        "question": "What is the relative importance of S2 vs M2?",
        "answer": 0.33,
        "kwargs": {"precision": 2},
    }

    nq = NumericQuestion(
        question_name="Q3: Simple numeric question",
        question_text=question_data["question"],
        question_answer=question_data["answer"],
        **question_data["kwargs"],
    )

    nq.answer_input.value = question_data["answer"]  # Simulate user input
    nq.check_answer(None)  # Trigger check answer event
    assert nq.feedback_widget.value == "Correct!"


def test_numeric_question_incorrect_answer():
    question_data = {
        "question": "What is the relative importance of S2 vs M2?",
        "answer": 0.33,
        "kwargs": {"precision": 2},
    }

    nq = NumericQuestion(
        question_name="Q3: Simple numeric question",
        question_text=question_data["question"],
        question_answer=4,
        **question_data["kwargs"],
    )

    nq.answer_input.value = 5
    nq.check_answer(None)  # Trigger check answer event
    assert nq.feedback_widget.value == "Incorrect, try again."
