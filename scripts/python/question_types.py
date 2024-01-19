import geoviews.tile_sources as gvts
import hvplot.pandas  # noqa: F401
import panel as pn
import requests

from coastal_dynamics.multiple_choice import MultipleChoiceQuestion
from coastal_dynamics.multiple_selection import MultipleSelectionQuestion
from coastal_dynamics.numeric import NumericQuestion
from coastal_dynamics.visualization import DynamicWavePlot


def fetch_questions(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def create_question_widget(question_data, name):
    question_type = question_data.get("type")

    if question_type == "multiple_choice":
        question_name = question_data.get("name", "")
        question_text = question_data.get("question", "")
        question_answer = question_data.get("answer", "")
        question_options = question_data.get("options")
        kwargs = question_data.get("kwargs", {})
        return MultipleChoiceQuestion(
            question_name=question_name,
            question_text=question_text,
            question_options=question_options,
            question_answer=question_answer,
            **kwargs,
        )
    elif question_type == "multiple_selection":
        question_name = question_data.get("name", "")
        question_text = question_data.get("question", "")
        question_answers = question_data.get("answers", "")
        question_options = question_data.get("options")
        kwargs = question_data.get("kwargs", {})
        return MultipleSelectionQuestion(
            question_name=question_name,
            question_text=question_text,
            question_options=question_options,
            question_answers=question_answers,
            **kwargs,
        )
    elif question_type == "numeric":
        question_name = question_data.get("name", "")
        question_text = question_data.get("question", "")
        question_answer = question_data.get("answer", "")
        kwargs = question_data.get("kwargs", {})
        return NumericQuestion(
            question_name=question_name,
            question_text=question_text,
            question_answer=question_answer,
            **kwargs,
        )
    else:
        msg = f"Unknown question type: {question_type}"
        raise ValueError(msg)


def main():
    import warnings

    warnings.filterwarnings(
        "ignore", category=FutureWarning, module="holoviews.core.data"
    )
    url = (
        "https://coclico.blob.core.windows.net/coastal-dynamics/questions/template.json"
    )
    questions = fetch_questions(url)

    # Create a Panel column to hold all question widgets
    all_questions_panel = pn.Column(sizing_mode="stretch_width")

    # Add each question's panel to the main Panel column
    for key, question_data in questions.items():
        question_widget = create_question_widget(question_data, key)
        question_panel = question_widget.serve()
        all_questions_panel.append(question_panel)

    # Create a wave plot and a base plot
    wave_plot = DynamicWavePlot(
        amplitude_range=(1, 3, 0.5), wavelength_range=(5, 20, 0.1)
    )
    base_plot = gvts.EsriImagery(width=900, height=500)

    # Combine all components into a single dashboard
    dashboard = pn.Column(
        pn.pane.Markdown("# Questions"),
        all_questions_panel,
        pn.pane.Markdown("# Coastal Dynamics Interactive Dashboard"),
        base_plot,
        wave_plot.__panel__(),  # Assuming DynamicWavePlot has a __panel__ method
        sizing_mode="stretch_width",
    )

    # Serve the complete dashboard
    dashboard.show()
    # # Create a Panel column to hold all question widgets
    # all_questions_panel = pn.Column(sizing_mode="stretch_width")

    # # Add each question's panel to the main Panel column
    # for key, question_data in questions.items():
    #     question_widget = create_question_widget(question_data, key)
    #     question_panel = question_widget.serve()
    #     all_questions_panel.append(question_panel)
    # wave_plot = DynamicWavePlot(
    #     amplitude_range=(1, 3, 0.5), wavelength_range=(5, 20, 0.1)
    # )
    # base_plot = gvts.EsriImagery(width=900, height=500)

    # # Serve the complete set of questions
    # all_questions_panel.show()


if __name__ == "__main__":
    main()
