from IPython.display import Javascript, display, clear_output
from ipywidgets import IntSlider, FloatSlider, Layout, HBox
import math
from functools import partial


class Interface:

    def __init__(self):
        self.widgets = {}
        self.display_interface()

    def get_d3_script(self, template):

        num_squares = self.widgets["num_squares_widget"].value
        square_size = self.widgets["square_size_widget"].value
        step = self.widgets["step_widget"].value
        squares = range(num_squares)
        squares = [math.sin(i/step)*square_size for i in squares]    

        return template.format(squares=squares)

    def display_d3(self,caller):
        js_template = open("custom_js.js").read()
        script = self.get_d3_script(js_template)
        clear_output(True)
        display(Javascript(script))
    

# http://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html
    def display_interface(self):
        self.widgets["square_size_widget"] = FloatSlider(description="Choose square size: ", value = 20, min = 5, max=40,continuous_update=False)
        self.widgets["num_squares_widget"] = IntSlider(description="Choose num squares: ", value = 20, min = 1, max=100,continuous_update=False)
        self.widgets["step_widget"] = FloatSlider(description="Choose step ", value = 3, min = 1, max=10,continuous_update=False)

        widget_list = []
        for k,v in self.widgets.iteritems():
            v.layout = Layout(flex='1 1 auto', width='auto')
            widget_list.append(v)
            v.observe(self.display_d3)
 
        display(HBox(widget_list))
        self.widgets["square_size_widget"].value = 21

        

        
