import matplotlib.pyplot as plt
import numpy as np

class SketchAppQuestion():
    """class to create SketchApp questions, for the Coastal Codebook/Quizbook."""
    def __init__(self, question_data, aspect_ratio=5):
        
        self.xmin = question_data['xmin']
        self.xmax = question_data['xmax']
        self.ymin = question_data['ymin']
        self.ymax = question_data['ymax']
        
        self.ar = (self.xmax - self.xmin) / (self.ymax - self.ymin) / aspect_ratio

        self.correct = question_data['answer']
        
        self.x_points = []
        self.y_points = []

        self.epsilon = question_data['epsilon']
        
    def draw_figure(self, aspect_ratio=5):
        
        self.fig, self.ax = plt.subplots(figsize=(10,5))

        # Connect the event handlers
        self.fig.canvas.mpl_connect('button_press_event', on_click)
        self.fig.canvas.mpl_connect('motion_notify_event', on_motion)

        self.plot_points(lim_to_zero=False)

        plt.show()
        
    def on_click(event, **kwargs):
        
        try:
            x = event.xdata
            y = event.ydata
            
            if x and y:

                if event.button == 1:  # Left click
                    
                    x_points.append(x)
                    y_points.append(y)
                            
                elif event.button == 3:  # Right click
                    
                    x_array = np.array(x_points)
                    y_array = np.array(y_points)
                    
                    distances = np.sqrt((x_array-x)**2 + (y_array-y)**2)
                    
                    # Check if clicked on an existing point to remove it
                    if any(distances < epsilon):
                        
                        id = np.argwhere(distances<epsilon)[0][0]
                        
                        x_points.pop(id)
                        y_points.pop(id)
        except TypeError:
            pass
        
        self.plot_points(kwargs)
        
    def plot_points(lim_to_zero=True):
    
        plt.cla()
        ax.axvline(0, color='k')
        ax.axhline(0, color='k')
        if lim_to_zero:
            plot_x_points = [xmin] + x_points + [xmax]
            plot_y_points = [0] + y_points + [0]
        else:
            plot_x_points = x_points
            plot_y_points = y_points
        
        try:
            sort_ids = np.argsort(plot_x_points)
            
            plot_x_points = np.array(plot_x_points)[sort_ids]
            plot_y_points = np.array(plot_y_points)[sort_ids]
            
            cs = interpolator(plot_x_points, plot_y_points, extrapolate=None)
        
            xs = np.linspace(xmin, xmax, 100)
            ys = cs(xs)
            
            ax.plot(xs, ys, color='r')
        
        except:
            pass
        
        plt.scatter(plot_x_points, plot_y_points, color='red')
                
        ax.set_xlim((xmin, xmax))
        ax.set_ylim((ymin, ymax))
        ax.set_aspect(aspect_ratio)
        
        ax.set_title('Left click to add points, Right click to remove points')
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        
        # Display the plot
        plt.grid(True)
        
        plt.draw()
        
    def close(self):
        
        plt.close(fig='all')
