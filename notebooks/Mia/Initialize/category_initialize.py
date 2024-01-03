def init():
    import numpy as np
    import ipywidgets as widgets
    
    Q1_text = 'Scheveningen'
    Q2_text = 'Galveston'
    Q3_text = 'Rio de Janeiro'
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