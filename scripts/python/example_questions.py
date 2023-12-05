import panel as pn
import requests

from coastal_dynamics.questions.multiple_choice import MultipleChoiceQuestion
from coastal_dynamics.questions.multiple_selection import MultipleSelectionQuestion
from coastal_dynamics.questions.numeric import NumericQuestion


def fetch_questions(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def create_question_widget(question_data, name):
    question_type = question_data.get("type")

    if question_type == "multiple_choice":
        kwargs = question_data.get("kwargs", {})
        return MultipleChoiceQuestion(question_data, name, **kwargs)
    elif question_type == "multiple_selection":
        kwargs = question_data.get("kwargs", {})
        return MultipleSelectionQuestion(question_data, name, **kwargs)
    elif question_type == "numeric":
        kwargs = question_data.get("kwargs", {})
        return NumericQuestion(question_data, name, **kwargs)
    else:
        msg = f"Unknown question type: {question_type}"
        raise ValueError(msg)


def main():
    url = "https://coclico.blob.core.windows.net/coastal-dynamics/questions/01_coastal_classification_questions.json"
    questions = fetch_questions(url)

    # Create a Panel column to hold all question widgets
    all_questions_panel = pn.Column(sizing_mode="stretch_width")

    # Add each question's panel to the main Panel column
    for key, question_data in questions.items():
        question_widget = create_question_widget(question_data, key)
        question_panel = question_widget.serve()
        all_questions_panel.append(question_panel)

    # Serve the complete set of questions
    all_questions_panel.show()


if __name__ == "__main__":
    main()
