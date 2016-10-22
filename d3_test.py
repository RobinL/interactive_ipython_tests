from IPython.display import Javascript, display, clear_output
from ipywidgets import IntSlider
import math
from functools import partial



class Interface:

    def __init__(self):
        self.display_interface()

    def get_d3_script(self, template,square_size, num_squares=10,step=2):
        squares = range(num_squares)
        squares = [math.sin(i/step)*square_size for i in squares]    
        return template.format(squares=squares)

    def display_d3(self, passed_arguments):
        js_template = open("custom_js.js").read()
        script = self.get_d3_script(js_template, passed_arguments["owner"].value)
        clear_output(True)
        display(Javascript(script))

    def display_interface(self):
        display(Javascript("""$.getScript('http://cdnjs.cloudflare.com/ajax/libs/d3/3.5.6/d3.min.js')"""))
        self.int_widget = IntSlider()
        
     
        self.int_widget.observe(self.display_d3)
        display(self.int_widget)
        # print "hello"
