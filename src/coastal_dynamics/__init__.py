"""Tools for interactive teaching and learning with Jupyter notebooks."""

__author__ = """Floris Calkoen"""
__email__ = "floris@calkoen.nl"
__version__ = "0.0.7"

from .factory import QuestionFactory
from .io import read_questions, write_questions
from .multiple_choice import MultipleChoiceQuestion
from .multiple_selection import MultipleSelectionQuestion
from .numeric import NumericQuestion
from .question import Question
from .text import TextQuestion
from .utils import hash_answer

__all__ = [
    "MultipleChoiceQuestion",
    "MultipleSelectionQuestion",
    "TextQuestion",
    "NumericQuestion",
    "QuestionFactory",
    "Question",
    "hash_answer",
    "read_questions",
    "write_questions",
]
