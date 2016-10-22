from ipywidgets import widgets
from IPython.display import display
from IPython.display import HTML

global_vars = {}

def handle_submit(sender):
    print(global_vars["text_widget"].value)
    global_vars["text_widget"].value = global_vars["text_widget"].value.upper()

def display_interface():
    display(HTML(open("custom_styles.html").read()))
    global_vars["text_widget"] =  widgets.Text()
    global_vars["text_widget"].on_submit(handle_submit)
    display(global_vars["text_widget"])
    