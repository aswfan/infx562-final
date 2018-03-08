// add this to index.html, in front of </body>:
//<script src="js/text.js"></script>

var page1 = d3.select("#page1");

var page2 = d3.select("#page2");

var page3 = d3.select("#page3");

page1.append('div')
    .append('text')
    .text("On the left is the scatter plot of the original dataset, we could tell from the plot that the relationship between X and Y is quite linear. If we look at the plot on the right side, after linear transformation (PCA), most of the variance is now on the first principal component. While second principal component only account for a small portion of the variance.");
    //.style("font-size","12px");


page2.append('div')
    .append('text')
    .text("In this page we want to show how powerful PCA is when we want to display the difference among points. Now we see a 3-D scatter plot on the left side and a 2-D scatter plot on the right side which shows the first and second principal component. So even if it is a data change over time, we could easily tell how their could be clustered with our eyes.");
    //.style("font-size","12px");

page3.append('div')
    .append('text')
    .text("In this page we would like to explore other datasets with high dimensionality.");
