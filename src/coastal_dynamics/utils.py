import hashlib
import numpy as np


def hash_answer(answer, question_type, sig_figs=None):
    """Hash a single answer or a list of answers based on the question type."""
    if question_type == "multiple_selection":
        # For multiple_selection, directly hash each answer in the list
        return [hashlib.sha256(ans.encode()).hexdigest() for ans in answer]
    elif question_type == "text":
        # For text questions, normalize to lower case before hashing
        return hashlib.sha256(answer.lower().encode()).hexdigest()
    elif question_type == "multiple_choice":
        # For multiple_choice and numeric, directly hash the answer
        return hashlib.sha256(str(answer).encode()).hexdigest()
    elif question_type == "numeric":
        if sig_figs:
            answer = np.format_float_positional(
                float(answer),
                precision=sig_figs,
                unique=False,
                fractional=False,
                trim="k",
            )
        return hashlib.sha256(str(answer).encode()).hexdigest()
    else:
        msg = f"Unsupported question type: {question_type}"
        raise ValueError(msg)
