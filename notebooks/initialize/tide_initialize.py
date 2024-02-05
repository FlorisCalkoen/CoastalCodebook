def init3():
    import numpy as np
    import ipywidgets as widgets
    
    Q11_text = 'A'
    Q12_text = 'B'
    Q13_text = 'N'
    Answer11 = ["m2", "s2"]
    Answer12 = Answer11
    Answer13 = [14.77, 15]
    
    Q21_text = 'C'
    Q22_text = 'D'
    Q23_text = 'M'
    Answer21 = ["k1", "o1"]
    Answer22 = Answer21
    Answer23 = [13.5, 14]
    
    Q31_text = 'M1'
    Q32_text = 'M2'
    Q33_text = 'E'
    Q34_text = 'F'
    Answer31 = ["march", "september"]
    Answer32 = Answer31
    Answer33 = ["s2", "k2"]
    Answer34 = Answer33
    
    Q41_text = 'M3'
    Q42_text = 'M4'
    Q43_text = 'G'
    Q44_text = 'H'
    Answer41 = ["june", "december"]
    Answer42 = Answer41
    Answer43 = ["k1", "p1"]
    Answer44 = Answer43
    
    
    def Numerical_question_body(Question, answer):
        
        # makes the widgets
        question_widget = widgets.Label(value= Question)
        unit_widget = widgets.Label(value= 'Answer:', layout=widgets.Layout(width='50px'))
        if isinstance(answer[0], str):
            value_widget = widgets.Text(value='', disabled=False, layout=widgets.Layout(width='80px'))
        else:
            value_widget = widgets.FloatText(value=0, disabled=False, step = 0.01, layout=widgets.Layout(width='80px'))
    
        
        submit_button = widgets.Button(description='Check',)
    
        output_widget = widgets.Text(value= '', placeholder='', description='Feedback:', disabled=False, layout=widgets.Layout(width='500px'), overflow='hidden')
        #output_widget.add_class('Broad_widget')
    
        HBox1 = widgets.HBox([unit_widget, value_widget, output_widget])
        #HBox.layout.justify_content = 'flex-start' # dont adjust the layout on the window 
    
        #place all the horizontal boxes in one vertical box, and display it.
        quiz_widget = widgets.VBox([question_widget] + [HBox1] + [submit_button])
        quiz_widget.layout.flex = 'none'
    
        display(quiz_widget)
    
        def check_answers(button, answer = answer):
    
            # get value from widget and check if this corresponds with the answer
            response = value_widget.value
            if isinstance(answer[0], float):
                if response >= answer[0] and response <= answer[1]:
                    output_widget.value = str('Correct! Well done.')
                else:
                    output_widget.value = str('Incorrect, please try again.')
            elif response.lower() in answer: # if the answer is correct
                output_widget.value = str('Correct! Well done.')
            else: # the answer is wrong
                output_widget.value = str('Incorrect, please try again.')
    
        submit_button.on_click(check_answers)
    
    
    # organise the questions, units, and answers    
    questions = [[Q11_text, Q12_text, Q13_text],
                [Q21_text, Q22_text, Q23_text],
                [Q31_text, Q32_text, Q33_text, Q34_text],
                [Q41_text, Q42_text, Q43_text, Q44_text]]
    Answers = [[Answer11, Answer12, Answer13],
              [Answer21, Answer22, Answer23],
              [Answer31, Answer32, Answer33, Answer34],
              [Answer41, Answer42, Answer43, Answer44]]
           
    # make and display the questions
    general_question4 = ["1. In a semi-diurnal environment, spring tide occurs for tidal constituents A and B every N days. If you set the time range to around 30 days, which phenomenon can you detect when looking at the combined signal of these two constituents?", 
                     "2. In a diurnal environment, spring tide occurs for tidal constituents C and D every M days. What is the main difference to the signal from question 1?",
                     "3. Strongest semi-diurnal tides are in the months M1 and M2, as can be seen from adding constituents E and F.",
                     "4. Strongest diurnal tides are in the months M3 and M4, as can be seen from adding constituents G and H."
                       ]
    
    general_question56 = ["5. The combinations we looked at above have periods of up to 2 weeks. But we also know that there are much longer variations. Set the time-range to 1 year and plot the combinations S2/K2 and K1/P1. What kind of combined signal can you see now?", 
                         "6. Finally activate all components and analyse the total signal. What are the dominant components at each location? Why is the total tidal signal so different among locations?"
                         ]
    for i, g in enumerate(general_question4):
        print("\n\n\033[1m" + g + "\033[0m")
        for Question, answer in zip(questions[i], Answers[i]):
            Numerical_question_body(Question, answer)
    print("\n\n\033[1m" + general_question56[0] + "\033[0m")
    print("\n\n\033[1m" + general_question56[1] + "\033[0m\n")

    return None


## Missing a condition that A!=B, ..

#%% Questions in 2d_tidal_constituents

def init1():
    import numpy as np
    import ipywidgets as widgets
    
    Answer1 = [14.77, 15]
    Answer2 = "daily inequality"
    Q1 = "Beating period of M2 and S2 is:"
    Q2 = "The phenomenon is:"
    
    def Numerical_question_body(Question, answer):
       
       # makes the widgets
       question_widget = widgets.Label(value= Question)
       unit_widget = widgets.Label(value= 'Answer:', layout=widgets.Layout(width='50px'))
       if isinstance(answer[0], str):
           value_widget = widgets.Text(value='', disabled=False, layout=widgets.Layout(width='80px'))
       else:
           value_widget = widgets.FloatText(value=0, disabled=False, step = 0.01, layout=widgets.Layout(width='80px'))
       
       submit_button = widgets.Button(description='Check',)
   
       output_widget = widgets.Text(value= '', placeholder='', description='Feedback:', disabled=False, layout=widgets.Layout(width='500px'), overflow='hidden')
       #output_widget.add_class('Broad_widget')
   
       HBox1 = widgets.HBox([unit_widget, value_widget, output_widget])
       #HBox.layout.justify_content = 'flex-start' # dont adjust the layout on the window 
   
       #place all the horizontal boxes in one vertical box, and display it.
       quiz_widget = widgets.VBox([question_widget] + [HBox1] + [submit_button])
       quiz_widget.layout.flex = 'none'
   
       display(quiz_widget)
   
       def check_answers(button, answer = answer):
   
           # get value from widget and check if this corresponds with the answer
           response = value_widget.value
           if isinstance(answer[0], float):
               if response >= answer[0] and response <= answer[1]:
                   output_widget.value = str('Correct! Well done.')
               else:
                   output_widget.value = str('Incorrect, please try again.')
           elif response.lower() in answer: # if the answer is correct
               output_widget.value = str('Correct! Well done.')
           else: # the answer is wrong
               output_widget.value = str('Incorrect, please try again.')
   
       submit_button.on_click(check_answers)

    # organise the questions, units, and answers    
    questions = [Q1, Q2]
    Answers = [Answer1, Answer2]    
           
    # make and display the questions
    general_question = ["1. Set the time range to around 30 days and select only the main semi-diurnal components (M2 and S2). Which phenomenon can you detect when looking at the combined signal of these two? What is the period of this combined signal (in days)? ", 
                     "2. Now select the M2 and K1 components. Looking at the combined signal, which phenomenon can you detect this time?"
    ]
    
    for i in range(len(general_question)):
        print("\n\n\033[1m" + general_question[i] + "\033[0m")
        Numerical_question_body(questions[i], Answers[i])

    return None

#%% Questions in 3a_tidal_environments - tidal characters

def init2():
    import numpy as np
    import ipywidgets as widgets
    
    Q1_text = 'Scheveningen'
    Q2_text = 'Galveston'
    Q3_text = 'Valparaiso'
    Q4_text = 'Jakarta'
    Answer1 = "semidiurnal"
    Answer2 = "mixed, mainly diurnal"
    Answer3 = "mixed, mainly semidiurnal"
    Answer4 = "diurnal"
    
    
    def question_body(Question, answer):
        
        # makes the widgets
        question_widget = widgets.Label(value= Question)
        unit_widget = widgets.Label(value= 'Answer:', layout=widgets.Layout(width='50px'))
        value_widget = widgets.Text(value='', disabled=False, layout=widgets.Layout(width='80px'))
        
        
        submit_button = widgets.Button(description='Check',)
    
        output_widget = widgets.Text(value= '', placeholder='', description='Feedback:', disabled=False, layout=widgets.Layout(width='500px'), overflow='hidden')
        #output_widget.add_class('Broad_widget')
    
        HBox1 = widgets.HBox([unit_widget, value_widget, output_widget])
        #HBox.layout.justify_content = 'flex-start' # dont adjust the layout on the window 
    
        #place all the horizontal boxes in one vertical box, and display it.
        quiz_widget = widgets.VBox([question_widget] + [HBox1] + [submit_button])
        quiz_widget.layout.flex = 'none'
    
        display(quiz_widget)
    
        def check_answers(button, answer = answer):
    
            # get value from widget and check if this corresponds with the answer
            response = value_widget.value
            if response.lower() == answer: # if the answer is correct
                output_widget.value = str('Correct! Well done.')
            else: # the answer is wrong
                output_widget.value = str('Incorrect, please try again.')
    
        submit_button.on_click(check_answers)
    
    
    # organise the questions, units, and answers    
    questions = [Q1_text, Q2_text, Q3_text, Q4_text]
    Answers = [Answer1, Answer2, Answer3, Answer4]
           
    for Question, answer in zip(questions, Answers):
        question_body(Question, answer)
   
    return None


## Missing a condition that A!=B, ..

#%% plot_timeseries_with_interactive_controls

import matplotlib.pyplot as plt
import ipywidgets as widgets

def plot_timeseries_with_interactive_controls(comps, dates, tide_fes, tide_gauge):
    # Define a list of checkboxes for component selection and put them in one row
    checkboxes = [widgets.Checkbox(value=True, description=comp, layout=widgets.Layout(width='auto')) for comp in comps[:-4]]
    checkbox_row = widgets.HBox(checkboxes, layout=widgets.Layout(display='flex', flex_flow='row wrap'))

    # Plot with interactive slider and checkboxes
    date_range_selector = widgets.SelectionRangeSlider(
        options=[(date.strftime('%d-%m-%Y %H:%M'), date) for date in dates],
        index=(0, len(dates)-1),
        description='Dates',
        orientation='horizontal',
        layout={'width': '700px'},
        continuous_update=False,
        readout=True
    )

    def plot_timeseries(date_range, **kwargs):
        start_date, end_date = date_range

        # Filter selected components
        selected_components = [comp for comp, value in kwargs.items() if value]

        # Plot selected components on axes[0]
        fig, axes = plt.subplots(nrows=3, figsize=(10, 8), sharex=True, constrained_layout=False)
        for comp in selected_components:
            axes[0].plot(tide_fes[comp]['scheveningen'][start_date:end_date], 
                         label=comp, linewidth=0.5)
        axes[0].legend(fontsize='small', loc='upper right')

        # Calculate and plot the sum on axes[1]
        sum_values = sum(tide_fes[comp]['scheveningen'][start_date:end_date] for comp in selected_components)
        axes[1].plot(sum_values.index, sum_values, color='darkblue', 
                     label='Sum of selected components', linewidth=0.5)
        axes[1].legend(fontsize='small', loc='upper right')

        # Plot total tidal signal and observed sea level on axes[2]
        axes[2].plot(tide_gauge[start_date:end_date].index, tide_gauge[start_date:end_date], color='black', 
                     label='Observed sea level', linewidth=0.7)
        axes[2].plot(tide_fes['all']['scheveningen'][start_date:end_date], color='blue', 
                     label='Total tidal signal', linewidth=0.5)
        axes[2].legend(fontsize='small', loc='upper right')

        # Set labels and legend
        fig.text(-0.03, 0.5, 'Sea level [m]', va='center', rotation='vertical', fontsize=14)
        fig.text(0.5, -0.05, 'Time', ha='center', va='center', fontsize=14)
        plt.tight_layout()
        plt.show()

    # Create an interactive widget with checkboxes
    figure = widgets.interactive(plot_timeseries,
                      date_range=date_range_selector,
                      **{checkbox.description: checkbox for checkbox in checkboxes})

    # Create a new container for arranging controls
    controls = widgets.VBox([figure.children[0], checkbox_row, figure.children[-1]])
    controls.layout.height = '100%'
    display(controls)

#%% plot_grav_pull
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
        "X": [0,0,0.2,0],
        "A": [0, 0.3, 0.2, -0.025],
        "B": [0.3 * np.cos(45 * np.pi / 180), 0.3 * np.cos(45 * np.pi / 180), 0.25, -0.015],
        "C": [0.3, 0, 0.25, 0],
        "D": [0.3 * np.cos(45 * np.pi / 180), -0.3 * np.cos(45 * np.pi / 180), 0.25, 0.015],
        "E": [0, -0.3, 0.2, 0.025],
        "F": [-0.3 * np.cos(45 * np.pi / 180), -0.3 * np.cos(45 * np.pi / 180), 0.15, 0.01],
        "G": [-0.3, 0, 0.15, 0],
        "H": [-0.3 * np.cos(45 * np.pi / 180), 0.3 * np.cos(45 * np.pi / 180), 0.15, -0.01],
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
                    facecolor="None"
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
        
#%% plot_tide_diagram

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
    ax.text(0, 0, "Earth", ha="center", va="center", fontsize=10)
    ax.set_title(title, fontsize=10)
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=5)
    plt.axis("equal")
    plt.axis("off")
    plt.tight_layout()
    
#%% plot_4timeseries_with_interactive_controls

import matplotlib.pyplot as plt
import ipywidgets as widgets
from warnings import filterwarnings


def plot_4timeseries_with_interactive_controls(comps, dates, tide_fes, locs):
    # Define a list of checkboxes for component selection and put them in one row
    checkboxes = [widgets.Checkbox(value=True, description=comp, layout=widgets.Layout(width='auto')) for comp in comps]
    checkbox_row = widgets.HBox(checkboxes, layout=widgets.Layout(display='flex', flex_flow='row wrap'))

    # Plot with interactive slider and checkboxes
    date_range_selector = widgets.SelectionRangeSlider(
        options=[(date.strftime('%d-%m-%Y %H:%M'), date) for date in dates],
        index=(0, len(dates)-1),
        description='Dates',
        orientation='horizontal',
        layout={'width': '700px'},
        continuous_update=False,
        readout=True
    )

    def plot_timeseries(date_range, **kwargs):
        start_date, end_date = date_range

        # Filter selected components
        selected_components = [comp for comp, value in kwargs.items() if value]

        # Plot selected components
        fig, axes = plt.subplots(nrows=4, ncols=2,  figsize=(10, 8), sharex=True, constrained_layout=False)
        
        for comp in selected_components:
            axes[0, 0].plot(tide_fes[comp][locs[0]][start_date:end_date], label=comp, linewidth=0.5)
            axes[0, 1].plot(tide_fes[comp][locs[1]][start_date:end_date], label=comp, linewidth=0.5)
            axes[2, 0].plot(tide_fes[comp][locs[2]][start_date:end_date], label=comp, linewidth=0.5)
            axes[2, 1].plot(tide_fes[comp][locs[3]][start_date:end_date], label=comp, linewidth=0.5)
        axes[0, 1].legend(fontsize='small', loc='upper right', bbox_to_anchor=(1.3, 1))
        axes[0, 0].set_title(f'{locs[0].capitalize()}', fontweight='bold')
        axes[0, 1].set_title(f'{locs[1].capitalize()}', fontweight='bold')
        axes[2, 0].set_title(f'{locs[2].capitalize()}', fontweight='bold')
        axes[2, 1].set_title(f'{locs[3].capitalize()}', fontweight='bold')

        # Calculate and plot the sum
        sum_values = [0] * len(locs)        
        for i, loc in enumerate(locs):
            sum_values[i] = sum(tide_fes[comp][loc][start_date:end_date] for comp in selected_components)

        axes[1, 0].plot(sum_values[0].index, sum_values[0], color='darkblue', 
                 label='Sum of selected components', linewidth=0.5)
        axes[1, 1].plot(sum_values[1].index, sum_values[1], color='darkblue', 
                         label='Sum of selected components', linewidth=0.5)
        axes[3, 0].plot(sum_values[2].index, sum_values[2], color='darkblue', 
                         label='Sum of selected components', linewidth=0.5)
        axes[3, 1].plot(sum_values[3].index, sum_values[3], color='darkblue', 
                         label='Sum of selected components', linewidth=0.5)

        # Set labels and legend
        for ax in axes.flat:
            ax.tick_params(axis='x', rotation=30)
        fig.text(0.05, 0.5, 'Sea level [m]', va='center', rotation='vertical', fontsize=14)
        fig.text(0.5, 0.05, 'Time', ha='center', va='center', fontsize=14)
        plt.show()
    
    filterwarnings("ignore", category=UserWarning)


    # Create an interactive widget with checkboxes
    figure = widgets.interactive(plot_timeseries,
                      date_range=date_range_selector,
                      **{checkbox.description: checkbox for checkbox in checkboxes})

    # Create a new container for arranging controls
    controls = widgets.VBox([figure.children[0], checkbox_row, figure.children[-1]])
    controls.layout.height = '100%'
    display(controls)