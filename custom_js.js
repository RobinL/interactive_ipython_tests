require.config({{
    paths: {{
        d3: "http://127.0.0.1:8888/files/d3.v4.min",
        mydata: "http://127.0.0.1:8888/files/mydata"
     }}
 }});



require(["d3", "mydata"], function(d3,mydata) {{

    debugger;
    var myElem = document.getElementById('squares_svg');

    if (myElem === null) {{

        var e = element.get(0)
        var svg = d3.select(e).append("svg")
            .attr("height",400)
            .attr("width",2000)
            .attr("id", "squares_svg")

    }} else {{

        var svg = d3.select("#squares_svg")
        svg.selectAll("*").remove();

    }}
        
    var squares = {squares}

    function my_sum(my_array) {{
        var sum = my_array.reduce(add, 0);
        function add(a, b) {{
            return Math.abs(a) + Math.abs(b);
        }}
        return sum
    }}

    var my_max = Math.max.apply(Math, squares);

    var color = d3.scaleLinear()
        .domain([0,my_max*3/4,my_max])
        .range(["red", "purple","blue"]);

    svg.selectAll("hello")
        .data(squares)
        .enter()
        .append("rect")
        .attr("width",function(d) {{return Math.abs(d)}})
        .attr("height",function(d){{return Math.abs(d)}})
        .attr("fill", function(d) {{return color(Math.abs(d)) }})
        .attr("x", function(d,i){{return 10 + my_sum(squares.slice(0,i)) +i*5 }})
        .attr("y",function(d,i){{return 100 + d*2}})
        console.log(1234)

    $.getJSON( "../files/mydata.json", function( data ) {{
        debugger;
    }}
    );

}})