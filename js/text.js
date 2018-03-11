 // add this to index.html, in front of </body>:
//<script src="js/text.js"></script>

var page0 = d3.select("#page0text");

var page1 = d3.select("#page1text");

var page2 = d3.select("#page2text");

var page3 = d3.select("#page3text");

page0.append('p')
    .text("When building a predictive model with dataset without dependent variable, for example when we want to group dataset or segmentize customers, we usually use unsupervised techniques like clustering and SVM. Principal component analysis (PCA) is among one of these unsupervised tools. One of its advantage is that it is a linear transformation process that makes data visualization in a 2-D plan fairly easy.")
    .append('p').text("PCA refers to the process by which principal component analysis are computed, and the subsequent use of these components in understanding the data.")
    .append('p').text("PCA provides a tool to do just this. It finds a low-dimensional representation of a data set that contains as much as possible of the variation. The idea is that each of the n observations lives in p-dimensional space, but not all of these dimensions are equally interesting. PCA seeks a small number of dimensions that are as interesting as possible, where the concept of interesting is measured by the amount that the observations vary along each dimension. Each of the dimensions found by PCA is a linear combination of the p features. We now explain the manner in which these dimensions, or principal components, are found.")
    .append('p').text("The first principal component of a set of features X1,X2, . . . , Xp is the normalized linear combination of the features.");

page1.append('p')
    .text("On the left is the scatter plot of the original dataset, we could tell from the plot that the relationship between X and Y is quite linear. If we look at the plot on the right side, after linear transformation (PCA), most of the variance is now on the first principal component. While second principal component only account for a small portion of the variance.");
    //.style("font-size","12px");


page2.append('p')
    .text("In this page we want to show how powerful PCA is when we want to display the difference among points. Now we see a 3-D scatter plot on the left side and a 2-D scatter plot on the right side which shows the first and second principal component. So even if it is a data change over time, we could easily tell how their could be clustered with our eyes.");
    //.style("font-size","12px");

page3.append('p')
    .text("In this page we would like to explore other datasets with high dimensionality.");

