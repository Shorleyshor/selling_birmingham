console.log(data);

let trace1 = 
{
  x: [row.Price],
  y: [row.Bedrooms],
  mode: "lines"
};

let traceData = 
[
  trace1
];

let layout = 
{
title: "Bedroom Vs Price Sactter Graph" 
};
  
Plotly.newPlot("BedroomsPriceScatter", traceData, layout);