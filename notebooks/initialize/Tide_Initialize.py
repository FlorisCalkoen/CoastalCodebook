# %% plot_tide_diagram - from 2c
def plot_tide_diagram(angle_sun, angle_moon):
    fig, ax = plt.subplots()

    dm = 2  # diameter of Earth patch in the figure

    earth = mpatches.Circle((0, 0), dm / 2, fill=True, color="C2")
    lunar_tide = mpatches.Ellipse(
        (0, 0),
        width=dm + 0.75,
        height=dm + 0.15,
        angle=angle_moon,
        fill=False,
        color="k",
        linestyle="dashed",
        label="Lunar tide",
    )
    solar_tide = mpatches.Ellipse(
        (0, 0),
        width=dm + 0.3,
        height=dm + 0.05,
        angle=angle_sun,
        fill=False,
        color="C1",
        linestyle="dashed",
        label="Solar tide",
    )
    if (angle_moon - angle_sun) % 180:
        title = "Neap tide (Moon and Sun perpendicular)"
        total_tide = mpatches.Ellipse(
            (0, 0),
            width=dm + 0.8,
            height=dm + 0.45,
            angle=angle_moon,
            fill=True,
            color="C0",
            label="Total tide",
        )
    else:
        title = "Spring tide (Moon and Sun in line with Earth)"
        total_tide = mpatches.Ellipse(
            (0, 0),
            width=dm + 1.05,
            height=dm + 0.2,
            angle=angle_moon,
            fill=True,
            color="C0",
            label="Total tide",
        )

    ax.add_patch(total_tide)
    ax.add_patch(lunar_tide)
    ax.add_patch(solar_tide)
    ax.add_patch(earth)
    ax.text(0, 0, "Earth", ha="center", va="center", fontsize=12)
    ax.set_title(title, fontsize=10)
    ax.legend(loc="center left", bbox_to_anchor=(1, 0.5), fontsize=12)
    plt.axis("equal")
    plt.axis("off")
    plt.tight_layout()


# %% plot_grav_pull - from 2c
import matplotlib.patches as mpatches
import numpy as np


def plot_grav_pull():
    fig, axs = plt.subplots(1, 2, figsize=(12, 4))

    # Adding outer and inner circles
    circ_out = mpatches.Circle((0, 0), 0.3, fill=True, color="grey", linewidth=2)
    circ_in = mpatches.Circle((0, 0), 0.275, fill=True, color="lightgrey")
    circ_c = mpatches.Circle((0, 0), 0.005, fill=True, color="black")
    axs[0].add_patch(circ_out)
    axs[0].add_patch(circ_in)
    axs[1].add_patch(mpatches.Circle((0, 0), 0.3, fill=True, color="grey", linewidth=2))
    axs[1].add_patch(mpatches.Circle((0, 0), 0.275, fill=True, color="lightgrey"))
    axs[1].add_patch(circ_c)

    # Coordinates and force components. The first two values are the coordinates of the position.
    # The 3rd and 4th value are the x/y components of the GP at each location (not to scale)
    positions = {
        "X": [0, 0, 0.2, 0],
        "A": [0, 0.3, 0.2, -0.025],
        "B": [
            0.3 * np.cos(45 * np.pi / 180),
            0.3 * np.cos(45 * np.pi / 180),
            0.25,
            -0.015,
        ],
        "C": [0.3, 0, 0.25, 0],
        "D": [
            0.3 * np.cos(45 * np.pi / 180),
            -0.3 * np.cos(45 * np.pi / 180),
            0.25,
            0.015,
        ],
        "E": [0, -0.3, 0.2, 0.025],
        "F": [
            -0.3 * np.cos(45 * np.pi / 180),
            -0.3 * np.cos(45 * np.pi / 180),
            0.15,
            0.01,
        ],
        "G": [-0.3, 0, 0.15, 0],
        "H": [
            -0.3 * np.cos(45 * np.pi / 180),
            0.3 * np.cos(45 * np.pi / 180),
            0.15,
            -0.01,
        ],
    }

    # Loop through each position
    for pos in positions:
        # Center of the Earth
        if pos == "X":
            axs[0].add_patch(mpatches.Arrow(*positions[pos], width=0.025, color="k"))

        # Other positions
        else:
            # Gravitational pull (GP)
            axs[0].add_patch(
                mpatches.Arrow(
                    *positions[pos][0:2],
                    0.2,
                    0,
                    width=0.025,
                    edgecolor="k",
                    facecolor="None",
                )
            )  # GP at center of Earth
            axs[0].add_patch(
                mpatches.Arrow(*positions[pos], width=0.025, color="C3")
            )  # GP at each individual location

            # Differential pull
            diffpull = list(
                2 * (np.array(positions[pos][2:]) - np.array(positions["X"][2:]))
            )  # Subtract th GP at the center from the other locations
            axs[1].add_patch(
                mpatches.Arrow(*positions[pos][0:2], *diffpull, width=0.025, color="C2")
            )

    # Adding center and text
    titles = ["Gravitational pull", "Differential pull"]
    for i in range(len(axs)):
        for pos in positions:
            coords = [x + 0.025 for x in positions[pos][0:2]]
            axs[i].text(*coords, pos, fontsize=12, ha="center", va="center")
        axs[i].axis("equal")
        axs[i].axis("off")
        axs[i].set_xlim(-0.6, 0.7)
        axs[i].set_ylim(-0.4, 0.4)
        axs[i].set_title(titles[i])


# %% plot_timeseries_with_interactive_controls - from 2d

import matplotlib.pyplot as plt
import ipywidgets as widgets
import pickle
from datetime import datetime, timedelta


def plot_timeseries_with_interactive_controls(tide_gauge, eta_df, scheveningen):
    # Define a list of checkboxes for component selection and put them in one row

    dates = np.array(
        [
            datetime(2000, 1, 1, 0, 0, 0) + timedelta(seconds=item * 3600)
            for item in range(24 * 365)  # 1 year
        ]
    )

    comps = ["M2", "S2", "N2", "K2", "K1", "O1", "P1", "Q1", "MM", "MF", "SSA"]
    checkboxes = [
        widgets.Checkbox(
            value=(comp == "M2"), description=comp, layout=widgets.Layout(width="auto")
        )
        for comp in comps
    ]
    checkbox_row = widgets.HBox(
        checkboxes, layout=widgets.Layout(display="flex", flex_flow="row wrap")
    )

    # Plot with interactive slider and checkboxes
    date_range_selector = widgets.SelectionRangeSlider(
        options=[(date.strftime("%d/%m %Hh"), date) for date in dates],
        index=(0, len(dates) - 1),
        description="Dates",
        orientation="horizontal",
        layout={"width": "700px"},
        continuous_update=False,
        readout=True,
    )

    def plot_timeseries(date_range, **kwargs):
        start_date, end_date = date_range

        # Filter selected components
        selected_components = [comp for comp, value in kwargs.items() if value]

        # Plot selected components on axes[0]
        fig, axes = plt.subplots(
            nrows=4, figsize=(10, 8), sharex=True, constrained_layout=False
        )
        for comp in selected_components:
            axes[0].plot(
                scheveningen[comp.lower()][start_date:end_date] / 100,
                label=comp,
                linewidth=0.5,
            )
            l = axes[0].legend(
                fontsize="small", loc="upper right", bbox_to_anchor=(1, 1.2), ncol=11
            )
            for line in l.get_lines():
                line.set_linewidth(3)

        # Calculate and plot the sum on axes[1]
        sum_values = sum(
            scheveningen[comp.lower()][start_date:end_date]
            for comp in selected_components
        )
        axes[1].plot(
            sum_values.index,
            sum_values / 100,
            color="darkblue",
            label="Sum of selected components",
            linewidth=0.5,
        )
        l = axes[1].legend(
            fontsize="small", loc="upper right", bbox_to_anchor=(1, 1.2), ncol=1
        )
        for line in l.get_lines():
            line.set_linewidth(3)

        # Plot total tidal signal and the obtained sum on axes [2]

        axes[2].plot(
            eta_df[start_date:end_date] / 100,
            color="darkorange",
            label="Total tidal signal",
            linewidth=0.5,
        )
        axes[2].plot(
            sum_values.index,
            sum_values / 100,
            color="darkblue",
            label="Sum of selected components",
            linewidth=0.5,
        )
        l = axes[2].legend(
            fontsize="small", loc="upper right", bbox_to_anchor=(1, 1.2), ncol=2
        )
        for line in l.get_lines():
            line.set_linewidth(3)

        # Plot total tidal signal, sum, and observed sea level on axes [3]
        axes[3].plot(
            tide_gauge[start_date:end_date].index,
            tide_gauge[start_date:end_date],
            color="black",
            label="Observed sea level",
            linewidth=0.7,
        )
        axes[3].plot(
            eta_df[start_date:end_date] / 100,
            color="darkorange",
            label="Total tidal signal",
            linewidth=0.5,
        )
        axes[3].plot(
            sum_values.index,
            sum_values / 100,
            color="darkblue",
            label="Sum of selected components",
            linewidth=0.5,
        )
        l = axes[3].legend(
            fontsize="small", loc="upper right", bbox_to_anchor=(1, 1.2), ncol=3
        )
        for line in l.get_lines():
            line.set_linewidth(3)

        # Set labels and legend
        fig.text(
            -0.03, 0.5, "Sea level [m]", va="center", rotation="vertical", fontsize=14
        )
        fig.text(0.5, -0.05, "Time", ha="center", va="center", fontsize=14)
        plt.tight_layout()
        plt.show()

    # Create an interactive widget with checkboxes
    figure = widgets.interactive(
        plot_timeseries,
        date_range=date_range_selector,
        **{checkbox.description: checkbox for checkbox in checkboxes},
    )

    # Create a new container for arranging controls
    controls = widgets.VBox([figure.children[0], checkbox_row, figure.children[-1]])
    controls.layout.height = "100%"
    display(controls)


# %% Questions in 2d_tidal_constituents


def questions_2d():
    import numpy as np
    import ipywidgets as widgets

    Answer1 = [14.765, 14.8]
    Answer2 = "daily inequality"
    Answer3 = [1.075, 1.08]
    Q1 = "Beating period of M2 and S2 is:"
    Q2 = "The phenomenon is:"
    Q3 = "Beating period of M2 and K1 is:"

    def Numerical_question_body(Question, answer):
        # makes the widgets
        question_widget = widgets.Label(value=Question)
        unit_widget = widgets.Label(
            value="Answer:", layout=widgets.Layout(width="50px")
        )
        if isinstance(answer[0], str):
            value_widget = widgets.Text(
                value="", disabled=False, layout=widgets.Layout(width="80px")
            )
        else:
            value_widget = widgets.FloatText(
                value=0, disabled=False, step=0.01, layout=widgets.Layout(width="80px")
            )

        submit_button = widgets.Button(
            description="Check",
        )

        output_widget = widgets.HTML(
            value="",
            placeholder="",
            disabled=False,
            layout=widgets.Layout(width="500px", border="none"),
            overflow="hidden",
        )
        # output_widget.add_class('Broad_widget')

        HBox1 = widgets.HBox([unit_widget, value_widget, output_widget])
        # HBox.layout.justify_content = 'flex-start' # dont adjust the layout on the window

        # place all the horizontal boxes in one vertical box, and display it.
        quiz_widget = widgets.VBox([question_widget] + [HBox1] + [submit_button])
        quiz_widget.layout.flex = "none"

        display(quiz_widget)

        def check_answers(button, answer=answer):
            # get value from widget and check if this corresponds with the answer
            response = value_widget.value
            if isinstance(answer[0], float):
                if response >= answer[0] and response <= answer[1]:
                    output_widget.value = '<span style="color: green;margin-left: 8px;">Correct! Well done.</span>'
                else:
                    output_widget.value = '<span style="color: red;margin-left: 8px;">Incorrect, please try again.</span>'
            elif response.lower() == answer:  # if the answer is correct
                output_widget.value = '<span style="color: green;margin-left: 8px;">Correct! Well done.</span>'
            else:  # the answer is wrong
                output_widget.value = '<span style="color: red;margin-left: 8px;">Incorrect, please try again.</span>'

        submit_button.on_click(check_answers)

    # organise the questions, units, and answers
    questions = [Q1, Q2, Q3]
    Answers = [Answer1, Answer2, Answer3]

    # make and display the questions
    general_question = [
        "1. Set the time range to around 30 days and select only the main semi-diurnal components (M2 and S2). Which phenomenon can you detect when looking at the combined signal of these two? What is the period of this beating (in days)? ",
        "2. Now select the M2 and K1 components. Looking at the combined signal, which phenomenon can you detect this time?",
        "3. Can you explain this phenomenon from the beating period of M2 and K1? Compute this beating period (in days).",
    ]

    for i in range(len(general_question)):
        print("\n\n\033[1m" + general_question[i] + "\033[0m")
        Numerical_question_body(questions[i], Answers[i])

    return None


# %% Questions in 3a_tidal_environments - tidal characters


def questions_3a1():
    import numpy as np
    import ipywidgets as widgets

    Q1_text = "Scheveningen"
    Q2_text = "Galveston"
    Q3_text = "Jakarta"
    Q4_text = "Valparaiso"
    Answer1 = "Semi-diurnal"
    Answer2 = "Mixed, mainly diurnal"
    Answer3 = "Diurnal"
    Answer4 = "Mixed, mainly semi-diurnal"

    options = [
        "Semi-diurnal",
        "Mixed, mainly semi-diurnal",
        "Mixed, mainly diurnal",
        "Diurnal",
    ]

    def question_body(Question, answer, options):
        question_widget = widgets.Label(value=Question)
        unit_widget = widgets.Label(
            value="Answer:", layout=widgets.Layout(width="50px")
        )

        # Use a dropdown menu instead of a text widget
        value_widget = widgets.Dropdown(
            options=options,
            value=None,
            disabled=False,
            layout=widgets.Layout(width="200px"),
        )

        submit_button = widgets.Button(
            description="Check",
        )

        output_widget = widgets.HTML(
            value="",
            placeholder="",
            disabled=False,
            layout=widgets.Layout(width="500px", border="none"),
            overflow="hidden",
        )

        HBox1 = widgets.HBox([unit_widget, value_widget, output_widget])

        quiz_widget = widgets.VBox([question_widget] + [HBox1] + [submit_button])
        quiz_widget.layout.flex = "none"

        display(quiz_widget)

        def check_answers(button, answer=answer):
            response = value_widget.value
            if response == answer:
                output_widget.value = '<span style="color: green;margin-left: 8px;">Correct! Well done.</span>'
            else:
                output_widget.value = '<span style="color: red;margin-left: 8px;">Incorrect, please try again.</span>'

        submit_button.on_click(check_answers)

    # Organize the questions, units, and answers
    questions = [Q1_text, Q2_text, Q3_text, Q4_text]
    Answers = [Answer1, Answer2, Answer3, Answer4]

    for Question, answer in zip(questions, Answers):
        question_body(Question, answer, options)

    return None


## Missing a condition that A!=B, ..


# %% plot_4timeseries_with_interactive_controls - from 3a

import matplotlib.pyplot as plt
import ipywidgets as widgets
from warnings import filterwarnings


def plot_4timeseries_with_interactive_controls(comps, dates, tide):
    locs = ["Scheveningen", "Valparaiso", "Jakarta", "Galveston"]

    # Define a list of checkboxes for component selection and put them in one row
    checkboxes = [
        widgets.Checkbox(
            value=(comp in ["M2", "S2", "N2", "K2", "K1", "O1", "P1", "Q1"]),
            description=comp,
            layout=widgets.Layout(width="auto"),
        )
        for comp in comps
    ]
    checkbox_row = widgets.HBox(
        checkboxes, layout=widgets.Layout(display="flex", flex_flow="row wrap")
    )

    # Plot with interactive slider and checkboxes
    date_range_selector = widgets.SelectionRangeSlider(
        options=[(date.strftime("%d/%m %Hh"), date) for date in dates],
        index=(0, len(dates) - 1),
        description="Dates",
        orientation="horizontal",
        layout={"width": "700px"},
        continuous_update=False,
        readout=True,
    )

    def plot_timeseries(date_range, **kwargs):
        start_date, end_date = date_range

        # Filter selected components
        selected_components = [comp for comp, value in kwargs.items() if value]

        # Plot selected components
        fig, axes = plt.subplots(
            nrows=4, ncols=2, figsize=(12, 10), sharex=True, constrained_layout=False
        )

        for comp in selected_components:
            axes[0, 0].plot(
                tide[locs[0]][comp.lower()][start_date:end_date],
                label=comp,
                linewidth=0.5,
            )
            axes[0, 1].plot(
                tide[locs[1]][comp.lower()][start_date:end_date],
                label=comp,
                linewidth=0.5,
            )
            axes[2, 0].plot(
                tide[locs[2]][comp.lower()][start_date:end_date],
                label=comp,
                linewidth=0.5,
            )
            axes[2, 1].plot(
                tide[locs[3]][comp.lower()][start_date:end_date],
                label=comp,
                linewidth=0.5,
            )
        l = axes[0, 1].legend(
            fontsize="small", loc="upper right", bbox_to_anchor=(1.3, 1)
        )
        for line in l.get_lines():
            line.set_linewidth(3)
        axes[0, 0].set_title(f"{locs[0]}", fontweight="bold")
        axes[0, 1].set_title(f"{locs[1]}", fontweight="bold")
        axes[2, 0].set_title(f"{locs[2]}", fontweight="bold")
        axes[2, 1].set_title(f"{locs[3]}", fontweight="bold")

        # Calculate and plot the sum
        sum_values = [0] * len(locs)
        for i, loc in enumerate(locs):
            sum_values[i] = sum(
                tide[loc][comp.lower()][start_date:end_date]
                for comp in selected_components
            )

        axes[1, 0].plot(
            sum_values[0].index,
            sum_values[0],
            color="darkblue",
            label="Sum of selected components",
            linewidth=0.5,
        )
        axes[1, 1].plot(
            sum_values[1].index,
            sum_values[1],
            color="darkblue",
            label="Sum of selected components",
            linewidth=0.5,
        )
        axes[3, 0].plot(
            sum_values[2].index,
            sum_values[2],
            color="darkblue",
            label="Sum of selected components",
            linewidth=0.5,
        )
        axes[3, 1].plot(
            sum_values[3].index,
            sum_values[3],
            color="darkblue",
            label="Sum of selected components",
            linewidth=0.5,
        )

        # Set labels and legend
        for ax in axes.flat:
            ax.tick_params(axis="x", rotation=30)
        fig.text(
            0.05, 0.5, "Sea level [cm]", va="center", rotation="vertical", fontsize=14
        )
        fig.text(0.5, 0.05, "Time", ha="center", va="center", fontsize=14)
        plt.show()

    filterwarnings("ignore", category=UserWarning)

    # Create an interactive widget with checkboxes
    figure = widgets.interactive(
        plot_timeseries,
        date_range=date_range_selector,
        **{checkbox.description: checkbox for checkbox in checkboxes},
    )

    # Create a new container for arranging controls
    controls = widgets.VBox([figure.children[0], checkbox_row, figure.children[-1]])
    controls.layout.height = "100%"
    display(controls)


# %% Questions in 3a_tidal_environments - tidal beating


def questions_3a2():
    import numpy as np
    import ipywidgets as widgets

    Q11_text = "TC1"
    Q12_text = "TC2"
    Q13_text = "D1"
    Answer11 = ["m2", "s2"]
    Answer12 = Answer11
    Answer13 = [14.752, 14.8]

    Q21_text = "TC3"
    Q22_text = "TC4"
    Q23_text = "D2"
    Answer21 = ["k1", "o1"]
    Answer22 = Answer21
    Answer23 = [13.659, 13.7]

    Q31_text = "Month1"
    Q32_text = "Month2"
    Q33_text = "TC5"
    Q34_text = "TC6"
    Answer31 = ["march", "september"]
    Answer32 = Answer31
    Answer33 = ["s2", "k2"]
    Answer34 = Answer33

    Q41_text = "Month3"
    Q42_text = "Month4"
    Q43_text = "TC7"
    Q44_text = "TC8"
    Answer41 = ["june", "december"]
    Answer42 = Answer41
    Answer43 = ["k1", "p1"]
    Answer44 = Answer43

    def Numerical_question_body(Question, answer):
        # makes the widgets
        question_widget = widgets.Label(value=Question)
        unit_widget = widgets.Label(
            value="Answer:", layout=widgets.Layout(width="50px")
        )
        if isinstance(answer[0], str):
            value_widget = widgets.Text(
                value="", disabled=False, layout=widgets.Layout(width="80px")
            )
        else:
            value_widget = widgets.FloatText(
                value=0, disabled=False, step=0.01, layout=widgets.Layout(width="80px")
            )

        submit_button = widgets.Button(
            description="Check",
        )

        output_widget = widgets.HTML(
            value="",
            placeholder="",
            disabled=False,
            layout=widgets.Layout(width="500px", border="none"),
            overflow="hidden",
        )

        HBox1 = widgets.HBox([unit_widget, value_widget, output_widget])
        # HBox.layout.justify_content = 'flex-start' # dont adjust the layout on the window

        # place all the horizontal boxes in one vertical box, and display it.
        quiz_widget = widgets.VBox([question_widget] + [HBox1] + [submit_button])
        quiz_widget.layout.flex = "none"

        display(quiz_widget)

        def check_answers(button, answer=answer):
            # get value from widget and check if this corresponds with the answer
            response = value_widget.value
            if isinstance(answer[0], float):
                if response >= answer[0] and response <= answer[1]:
                    output_widget.value = '<span style="color: green;margin-left: 8px;">Correct! Well done.</span>'
                else:
                    output_widget.value = '<span style="color: red;margin-left: 8px;">Incorrect, please try again.</span>'
            elif response.lower() in answer:  # if the answer is correct
                output_widget.value = '<span style="color: green;margin-left: 8px;">Correct! Well done.</span>'
            else:  # the answer is wrong
                output_widget.value = '<span style="color: red;margin-left: 8px;">Incorrect, please try again.</span>'

        submit_button.on_click(check_answers)

    # organise the questions, units, and answers
    questions = [
        [Q11_text, Q12_text, Q13_text],
        [Q21_text, Q22_text, Q23_text],
        [Q31_text, Q32_text, Q33_text, Q34_text],
        [Q41_text, Q42_text, Q43_text, Q44_text],
    ]
    Answers = [
        [Answer11, Answer12, Answer13],
        [Answer21, Answer22, Answer23],
        [Answer31, Answer32, Answer33, Answer34],
        [Answer41, Answer42, Answer43, Answer44],
    ]

    # make and display the questions
    general_question4 = [
        "1. In a semi-diurnal environment, spring tide occurs for tidal constituents TC1 and TC2 every D1 days. Set the time range to around 30 days, which phenomenon can you detect when looking at the combined signal of these two constituents?",
        "2. In a diurnal environment, spring tide occurs for tidal constituents TC3 and TC4 every D2 days. What is the main difference to the signal from question 1?",
        "3. Strongest semi-diurnal tides are in the months Month1 and Month2, as can be seen from adding constituents TC5 and TC6.",
        "4. Strongest diurnal tides are in the months Month3 and Month4, as can be seen from adding constituents TC7 and TC8.",
    ]
    for i, g in enumerate(general_question4):
        print("\n\n\033[1m" + g + "\033[0m")
        for Question, answer in zip(questions[i], Answers[i]):
            Numerical_question_body(Question, answer)

    return None


## Missing a condition that A!=B, ..
# %% plot_2timeseries_with_interactive_controls - from 4b

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import ipywidgets as widgets
from warnings import filterwarnings
from matplotlib.ticker import MaxNLocator, StrMethodFormatter


def plot_2timeseries_with_interactive_controls(comps, dates, tide):
    locs = ["Scheveningen", "Jakarta"]
    all_comp = comps = [
        "M2",
        "S2",
        "N2",
        "K2",
        "K1",
        "O1",
        "P1",
        "Q1",
        "M3",
        "M4",
        "M6",
        "M8",
        "S4",
        "MN4",
        "MS4",
    ]
    # Define a list of checkboxes for component selection and put them in one row
    checkboxes = [
        widgets.Checkbox(
            value=(comp in ["M2"]),
            description=comp,
            layout=widgets.Layout(width="auto"),
        )
        for comp in comps
    ]
    checkbox_row = widgets.HBox(
        checkboxes, layout=widgets.Layout(display="flex", flex_flow="row wrap")
    )

    # Plot with interactive slider and checkboxes
    date_range_selector = widgets.SelectionRangeSlider(
        options=[(date.strftime("%d/%m %Hh"), date) for date in dates],
        index=(0, len(dates) - 1),
        description="Dates",
        orientation="horizontal",
        layout={"width": "700px"},
        continuous_update=False,
        readout=True,
    )

    def plot_timeseries(date_range, **kwargs):
        start_date, end_date = date_range

        # Filter selected components
        selected_components = [comp for comp, value in kwargs.items() if value]

        # Plot selected components
        fig, axes = plt.subplots(
            nrows=3, ncols=2, figsize=(12, 7), sharex=True, constrained_layout=False
        )

        for comp in selected_components:
            axes[0, 0].plot(
                tide[locs[0]][comp.lower()][start_date:end_date],
                label=comp,
                linewidth=0.5,
            )
            axes[0, 1].plot(
                tide[locs[1]][comp.lower()][start_date:end_date],
                label=comp,
                linewidth=0.5,
            )
        l = axes[0, 1].legend(
            fontsize="small", loc="upper right", bbox_to_anchor=(1.2, 1)
        )
        for line in l.get_lines():
            line.set_linewidth(3)
        axes[0, 0].set_title(f"{locs[0]}", fontweight="bold")
        axes[0, 1].set_title(f"{locs[1]}", fontweight="bold")

        # Calculate and plot the sum
        sum_values = [0] * len(locs)
        for i, loc in enumerate(locs):
            sum_values[i] = sum(
                tide[loc][comp.lower()][start_date:end_date]
                for comp in selected_components
            )

        axes[1, 0].plot(
            sum_values[0].index,
            sum_values[0],
            color="darkblue",
            label="Sum of selected components",
            linewidth=0.5,
        )
        axes[1, 1].plot(
            sum_values[1].index,
            sum_values[1],
            color="darkblue",
            label="Sum of selected components",
            linewidth=0.5,
        )
        l1 = axes[1, 1].legend(
            fontsize="small", loc="upper right", bbox_to_anchor=(1, 1.2)
        )
        for line in l1.get_lines():
            line.set_linewidth(3)

        sum_allvalues = [0] * len(locs)
        for i, loc in enumerate(locs):
            sum_allvalues[i] = sum(
                tide[loc][comp.lower()][start_date:end_date] for comp in all_comp
            )
        axes[2, 0].plot(
            sum_allvalues[0].index,
            sum_allvalues[0],
            color="black",
            label="Total tidal signal",
            linewidth=0.5,
        )
        axes[2, 1].plot(
            sum_allvalues[1].index,
            sum_allvalues[1],
            color="black",
            label="Total tidal signal",
            linewidth=0.5,
        )
        l2 = axes[2, 1].legend(
            fontsize="small", loc="upper right", bbox_to_anchor=(1, 1.2)
        )
        for line in l2.get_lines():
            line.set_linewidth(3)

        # Set labels and legend
        for ax in axes.flat:
            ax.tick_params(axis="x", rotation=0)
            ax.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m\n%H:%Mh"))
            ax.xaxis.set_major_locator(MaxNLocator(nbins=6))
        fig.text(
            0.05, 0.5, "Sea level [cm]", va="center", rotation="vertical", fontsize=14
        )
        fig.text(0.5, 0.05, "Time", ha="center", va="center", fontsize=14)
        plt.show()

    filterwarnings("ignore", category=UserWarning)

    # Create an interactive widget with checkboxes
    figure = widgets.interactive(
        plot_timeseries,
        date_range=date_range_selector,
        **{checkbox.description: checkbox for checkbox in checkboxes},
    )

    # Create a new container for arranging controls
    controls = widgets.VBox([figure.children[0], checkbox_row, figure.children[-1]])
    controls.layout.height = "100%"
    display(controls)


# %% Questions in 4b_shallow_water_tides


def questions_4b():
    import numpy as np
    import ipywidgets as widgets

    options2 = ["M3", "M4", "M6", "M8", "S4"]

    options1 = [
        "M2",
        "S2",
        "N2",
        "K2",  # semi-diurnal
        "K1",
        "O1",
        "P1",
        "Q1",  # diurnal
        "M3",
        "M4",
        "M6",
        "M8",
        "S4",
        "MN4",
        "MS4",
    ]  # short period (overtides)

    options = [options1, options2]

    Answer2 = ["M6"]
    Answer1 = ["M4", "MS4", "MN4", "S4"]

    answers = [Answer1, Answer2]

    Q1 = " "
    Q2 = " "

    questions = [Q1, Q2]

    def multiple_choice_question_body(Question, options, answer):
        question_widget = widgets.Label(
            value=Question, layout=widgets.Layout(width="500px")
        )

        # Use Checkbox widget for multiple-choice options
        checkboxes = [widgets.Checkbox(description=opt, value=False) for opt in options]

        submit_button = widgets.Button(
            description="Check",
        )

        output_widget = widgets.HTML(
            value="",
            placeholder="",
            disabled=False,
            layout=widgets.Layout(width="500px", border="none"),
            overflow="hidden",
        )

        VBox1 = widgets.VBox(
            [question_widget] + checkboxes + [submit_button, output_widget]
        )

        display(VBox1)

        def check_answers(button, answer=answer):
            # Check if all checkboxes are selected
            selected_options = [
                checkbox.description for checkbox in checkboxes if checkbox.value
            ]
            if set(selected_options) == set(answer):
                output_widget.value = '<span style="color: green;margin-left: 8px;">Correct! Well done.</span>'
            else:
                output_widget.value = '<span style="color: red;margin-left: 8px;">Incorrect, please try again.</span>'

        submit_button.on_click(check_answers)

    # make and display the questions

    general_question1 = "1. Select components whose period is around 6 hours. Validate your choice with the spectral plot from notebook 2d_tidal_constituents (Tidal Amplitudes chapter)."

    general_question2 = """2. Two important sources for non-linearity in the tidal propagation equations are bottom friction and continuity.
    - Compare the periods of M2 and M3, M4, M6, and M8.
    - Compare the periods of S2 and S4.
    How were these higher harmonics generated? What is the main overtide that is generated as a consequence of the friction depending non-linearly on the tidal velocity?"""

    general_question34 = """3. Select components M2 and M4.
    - Are the two constituents in phase? What do you notice in the combined signal?
    - Compare to Fig. 5.71 from the textbook. Determine which panels in Fig. 5.71 best match the signals from Scheveningen and Jakarta. Check if one of them is a combination of two panels.

4. Select the main tidal constituents and compare the resulting combined signal (second plot) to the total tidal signal, which includes the overtides (third plot). What contribution do the overtides have to the total tidal signal?"""

    print("\n\n\033[1m" + general_question1 + "\033[0m")
    multiple_choice_question_body(questions[0], options1, answers[0])
    print("\n\n\033[1m" + general_question2 + "\033[0m")
    multiple_choice_question_body(questions[1], options2, answers[1])
    print("\n\n\033[1m" + general_question34 + "\033[0m")

    return None
