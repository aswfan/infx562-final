var margin = {top: 20, right: 20, bottom: 30, left: 40},
    width = 500 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom,
    sleepTime = 2000,
    defaultDuration = 800,
    time=0,
    step_p2=0;

/* 
 * value accessor - returns the value to encode for a given data object.
 * scale - maps value to a visual display encoding, such as a pixel position.
 * map function - maps from data value to display value
 * axis - sets up axis
 */ 

var x_p2 = d3v3.scale.linear()
    .domain([-1,1])
    .range([0, width]);

var y_p2 = d3v3.scale.linear()
    .domain([-1,1])
    .range([height, 0]);

//var color = d3.scale.category10();

var xAxis = d3v3.svg.axis()
    .scale(x_p2)
    .orient("bottom");

var yAxis = d3v3.svg.axis()
    .scale(y_p2)
    .orient("left");

// add the graph canvas to the body of the webpage
var svg2 = d3.select("#_2dChart").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// load data
d3v3.csv("data/3data.csv", function(error, dat_2d) {

// change string (from CSV) into number format
dat_2d.forEach(function(d) {
  d["0"] = +d["0"];
  d["1"] = +d["1"];
  d["step"]=+d["step"];
  // console.log(d);
});

//console.log(xAxis)
// x-axis
svg2.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + height + ")")
    .call(xAxis)
  .append("text")
    .attr("class", "label")
    .attr("x", width)
    .attr("y", -6)
    .style("text-anchor", "end")
    .text("PC1");

// y-axis
svg2.append("g")
    .attr("class", "y axis")
    .call(yAxis)
  .append("text")
    .attr("class", "label")
    .attr("transform", "rotate(-90)")
    .attr("y", 6)
    .attr("dy", ".71em")
    .style("text-anchor", "end")
    .text("PC2");

// draw dots
function plotData(data_f){
    
svg2.append("g")
    .selectAll("circle")
    .data(data_f)
    .enter().append("circle")
    .attr("r", 5)
    .attr("cx", data_f=>x_p2(data_f["0"]))
    .attr("cy", data_f=>y_p2(data_f["1"]))
    .attr("fill",function(d){ if(d["label"]=="a"){ return "black";}else{
        if(d["label"]=="b"){return "red";}else{
            return "blue"
        }}})
    }



function sleep(milliseconds) {
      var start = new Date().getTime();
      for (var i = 0; i < 1e7; i++) {
        if ((new Date().getTime() - start) > milliseconds){
          break;
        }
        
      }
    }


function updateData() {
      d3.selectAll("circle").remove();
      time += Math.PI/8;
      step_p2 = step_p2 % 4 + 1;
      data_f=dat_2d.filter(dat_2d => dat_2d.step === step_p2);
    
    plotData( data_f );
    sleep(sleepTime/10);
    
    
    }

console.log(dat_2d)
setInterval( updateData,defaultDuration + sleepTime );


});