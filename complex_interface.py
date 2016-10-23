from IPython.display import Javascript, display, clear_output
from ipywidgets import IntSlider, FloatSlider, Layout, HBox
import math
from functools import partial

import pandas as pd

import statsmodels.formula.api as sm
from IPython.display import display

def sim_regression(num_points, variance, ):
    df = pd.DataFrame(np.random.multivariate_normal([0,0,0,0],[[1,0,0,0],[0,1,0,0],[0,0,1,0], [0,0,0,1]], num_points), columns=['x1', 'x2', 'x3', 'e'])
    df['y'] = 5 + 2*df['x1'] - 0.5*df['x2'] + df['x3'] + df['e']
    result = sm.ols(formula="y ~ x1 + x2 + x3", data=df).fit()
    display(result.summary())
    

class Interface:

    def __init__(self):
        self.widgets = {}
        self.display_interface()


    def display_outputs(self,caller):
        js_template = open("custom_js.js").read()
        script = self.get_d3_script(js_template)
        clear_output(True)
        display(Javascript(script))
    

# http://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html
    def display_interface(self):
        self.widgets["dep_variables_dropdown_widget"] = FloatSlider(description="Choose square size: ", value = 20, min = 5, max=40,continuous_update=False)
        # Nuber of points
        # Variance



        widget_list = []
        for k,v in self.widgets.iteritems():
            v.layout = Layout(flex='1 1 auto', width='auto')
            widget_list.append(v)
            v.observe(self.display_d3)
 
        display(HBox(widget_list))
        self.widgets["square_size_widget"].value = 21

        

        
