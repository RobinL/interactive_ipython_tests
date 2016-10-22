from IPython.display import Javascript, display
from ipywidgets import IntSlider

def get_d3_script(template,square_size, num_squares,step):
    squares = range(num_squares)
    squares = [math.sin(i/step)*square_size for i in squares]    
    return template.format(squares=squares)




def display_d3():
    Javascript("""$.getScript('http://cdnjs.cloudflare.com/ajax/libs/d3/3.5.6/d3.min.js')""")
    js_template = open("custom_js.js").read()
	w = IntSlider()
    script = get_d3_script(js_template)
	display(w)
    
