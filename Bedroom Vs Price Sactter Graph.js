console.log(dropped_data)

let trace1 = {
  x: [],
  y: [],
  mode: "lines"
};

let traceData = [trace1];

data.forEach(function(val) {
  trace1.x.push(val["Price"]);
  trace1.y.push(val["Bedrooms"]);

let layout = {
title: "Bedroom Vs Price Sactter Graph" } 
  
});

Plotly.newPlot('Bedroom Vs Price Sactter Graph', traceData, layout);