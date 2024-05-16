import matplotlib.pyplot as plt
import numpy as np

from scipy.interpolate import PchipInterpolator


class SketchAppQuestion():
    """class to create SketchApp questions, for the Coastal Codebook/Quizbook."""
    def __init__(self, question_data):
        """Initionalizer for the SketchAppQuestion class.

        Args:
            question_data (dict): dictionary containing the data to be used for this instance of the SketchAppQuestion class.
        """
        # used for plotting and to generate the answer
        self.xmin = question_data['xmin']
        self.xmax = question_data['xmax']
        self.ymin = question_data['ymin']
        self.ymax = question_data['ymax']
        
        # used to set the limit value when drawing (if true, two points at the min and max x values are added at y=0)
        self.lim_to_zero = question_data['lim_to_zero']

        # answers (y answer should be an array of values describing the correct answer)
        self.yanswer = question_data['answer']
        self.xanswer = np.linspace(self.xmin, self.xmax, len(self.yanswer))
        
        # initialize the iterable of points used to keep track of the points students clicked
        self.x_points = []
        self.y_points = []

        # maximum distance when clicking on a point to remove it
        self.epsilon = question_data['epsilon']
        
        # for plotting
        self.xlabel = question_data['xlabel']
        self.ylabel = question_data['ylabel']
        self.title = question_data['title']
        
        # interpolator used for the splines (find more at scipy.interpolate.***)
        self.interpolator = PchipInterpolator
        
        return None
        
    def draw_figure(self, figsize=(10,5), aspect_ratio=5, N=500):
        """Function to create the figure.

        Args:
            aspect_ratio (int, optional): The aspect ratio that will be used for the figure (defined as x / y = aspect_ratio). Defaults to 5.
            figsize (tuple, optional): figure size. Defaults to (10,5).
            N (int, optional): number of points used for drawing the splines. Defaults to 500.
        """
        # create figure
        self.fig, self.ax = plt.subplots(figsize=figsize)
        
        # save aspect ratio
        self.ar = (self.xmax - self.xmin) / (self.ymax - self.ymin) / aspect_ratio
        
        # save the number of points
        self.N = N

        # Connect the event handlers
        self.cid = self.fig.canvas.mpl_connect('button_press_event', self.on_click)

        # plot points (and also set title, grid, etc.)
        self.plot_points()

        # make sure the figure is shown
        plt.show()
        
        return None
        
    def on_click(self, event):
        """This function is executed when a click on screen occurs.

        Args:
            event (event): a click event.
        """
        # add a try statement for if the click event occurred outside of the plot boundaries, which will give None values to x and y
        try:
            self.x = event.xdata
            self.y = event.ydata
            
            if self.x and self.y:

                if event.button == 1:  # Left click
                    
                    self.x_points.append(self.x)
                    self.y_points.append(self.y)
                            
                elif event.button == 3:  # Right click
                    
                    self.x_array = np.array(self.x_points)
                    self.y_array = np.array(self.y_points)
                    
                    # calculate distances from all points to click location
                    distances = np.sqrt((self.x_array - self.x)**2 + (self.y_array - self.y)**2)
                    
                    # Check if clicked on an existing point to remove it
                    if any(distances < self.epsilon):
                        
                        id = np.argwhere(distances<self.epsilon)[0][0]
                        
                        self.x_points.pop(id)
                        self.y_points.pop(id)
        except TypeError:
            pass
        
        self.plot_points()
        
        return None
        
    def plot_points(self):
        """This function plots the points that the user has clicked.
        """
        # clear existing ax
        self.ax.clear()
        
        # draw axis
        self.ax.axvline(0, color='k')
        self.ax.axhline(0, color='k')
        
        # add points if limit to zero is true
        if self.lim_to_zero:
            plot_x_points = [self.xmin] + self.x_points + [self.xmax]
            plot_y_points = [0] + self.y_points + [0]
        else:
            plot_x_points = self.x_points
            plot_y_points = self.y_points
        
        # try statement for if plot list is empty and cant be sorted
        try:
            sort_ids = np.argsort(plot_x_points)
            
            plot_x_points = np.array(plot_x_points)[sort_ids]
            plot_y_points = np.array(plot_y_points)[sort_ids]
            
            cs = self.interpolator(plot_x_points, plot_y_points, extrapolate=None)
        
            xs = np.linspace(self.xmin, self.xmax, self.N)
            ys = cs(xs)
            
            self.ax.plot(xs, ys, color='r', label='your answer')
        
        except:
            pass
        
        self.ax.scatter(
            plot_x_points, 
            plot_y_points,
            c="None",
            edgecolors='k',
            label='your points'
        )
        
        # add the appearance of the plot to the axis
        self.plot_appearance()
                
    def plot_appearance(self):
        """Adds title, limits, aspect, grid, and axis labels to plot.
        """
        self.ax.set_xlim((self.xmin, self.xmax))
        self.ax.set_ylim((self.ymin, self.ymax))
        self.ax.set_aspect(self.ar)
        
        self.ax.set_title(self.title)
        self.ax.set_xlabel(self.xlabel)
        self.ax.set_ylabel(self.ylabel)
        
        self.ax.grid(True)
        
        # re-draw the plot
        plt.draw()
        
        return None
        
    def plot_answer(self):
        """plot the correct answer.
        """
        # disconnect the user from the events (user can no longer click additional points)
        self.fig.canvas.mpl_disconnect(self.cid)
        
        # add correct answer to plot
        self.ax.plot(self.xanswer, self.yanswer, color='grey', label='correct answer')
        
        # add legend to plot
        self.ax.legend()
        
        # re-draw the plot
        plt.draw()
        
    def check_answer(self):
        """
        This function checks the given answer with the correct answer. It was based on the SketchApp 
        Documentation V3.1 (July 20, 2023) by Anatoly Ilin & Mario van den Berg
        """
        print("to be implemented")
        
    def close(self):
        """Close the plot.
        """
        plt.close(fig='all')
