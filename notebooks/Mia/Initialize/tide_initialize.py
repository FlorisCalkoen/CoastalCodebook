def init():
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
    general_question4 = ["1. In a semi-diurnal environment, spring tide occurs for tidal constituents A and B every N days. Set the time range to around 30 days, which phenomenon can you detect when looking at the combined signal of these two constituents?", 
                     "2. In a diurnal environment, spring tide occurs for tidal constituents C and D every M days. What is the main difference to the signal from question 1?",
                     "3. Strongest semi-diurnal tides are in the months M1 and M2, as can be seen from adding constituents E and F.",
                     "4. Strongest diurnal tides are in the months M3 and M4, as can be seen from adding constituents G and H."
                       ]
    
    general_question56 = ["5. The combinations we looked at above have periods of up to 2 weeks. But we also know that there are much longer variations. Set the time-range to 1 year and plot the combinations S2/K2 and K1/P1. What kind of combined signal can you see now?", 
                         "6. Finally activate all eight principal components and analyse the combined signals. What are the dominant components at each location?"
                         ]
    for i, g in enumerate(general_question4):
        print("\n\n\033[1m" + g + "\033[0m")
        for Question, answer in zip(questions[i], Answers[i]):
            Numerical_question_body(Question, answer)
    print("\n\n\033[1m" + general_question56[0] + "\033[0m")
    print("\n\n\033[1m" + general_question56[1] + "\033[0m\n")

    return None


## Missing a condition that A!=B, ..