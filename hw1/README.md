# Homework 1: Histograms

This homework assignment asks you to write a python function to build histograms, then use that function to explore a data set that we have provided to you.

# Goals

In this assignment you will:
* Write a python function
* Use plotting tools to visualize data
* Perform an *exploratory study* of a dataset to investigate its properties

# Background

## Histograms

Histograms are a standard way of visualizing numerical data to study its *distribution*. In a histogram, data is *quantized* into bins, and then the bins are plotted to visualize how much data is in each bucket. This gives a sense of the distribution of the data. Of course, an important question is how big the bins should be. If there are too few bins, then you lose fine distinctions between data and may not be able to capture the distribution (consider a histogram with only one bin -- all the data will be in the same bin, and all you can tell is how much data you have!) Conversely, if there are too many bins, then you wind up with bins that provide very little information for capturing the distribution (consider a histogram with a separate bin for each data point -- no easy way to see the distribution of the data when each bin has 0 or 1 data points in it!)

Lecture 2 gives the necessary background to understand histograms and guidelines for choosing the number of bins

## Python functions

Python functions are written much like C functions, except for Python's indentation based syntax, and the fact that Python does not use static types. Consider the `min` function:
```
def min(x, y) :
    if x < y :
        return x
    else :
        return y
```

Python functions also let you specify default arguments, use named parameters when invoking functions, and return multiple values. See [Lecture 1](https://engineering.purdue.edu/~milind/datascience/2018spring/notes/lecture-1.pdf) for more details.

## Python plotting

We will be using `matplotlib` for most of our visualization in this class. This is a very powerful plotting library, with many features well beyond what we will need. Most of the time, we will be using the `pyplot` submodule of `matplotlib` which lets you easily produce simple plots with a simple syntax.

`pyplot` provides a built-in histogram plotting routine, `hist`. Here is how you can use `hist` to plot a histogram with 20 buckets over the range 0 to 100, and save the result into `test.png`:

```
import matplotlib.pyplot as plt

# read in input data into list called inp

plt.hist(inp, bins=10, range=(0, 100))
plt.savefig('test.png')
```

Note the use of named arguments when calling `hist` (`bins` and `range`). If you want to just display the plot instead of saving it, you could replace the last line with `plt.show()`.

The `hist` function makes histograms too easy, so in this assignment, we will use a function we provide for you to plot your histograms, included in `helper.py`:

`plotHisto(histo, 'test.png', minimum, maximum)`

Here, `histo` is a list of *histogram bin values* (rather than a list of data points). In other words, to use this function, you will need to compute the bin values yourself given some input data. `minimum` and `maximum` are the min and max of the histogram range.

# Instructions

## 1) Set up your repository for this homework

Click the link on Blackboard to set up a repository for homework 1, then clone it, as you did for homework 0.

The repository should contain 5 files:

1. This README
2. An input data file, called `math_scores.txt`
3. A file containing `plotHisto`, called `helper.py`
4. A starter file for your homework, called `hw1.py`
5. A similar starter file if you want to use Jupyter Notebook instead, called `hw1.ipynb`

## 2) Fill in the missing functionality of hw1.py

`hw1.py` shows you how to import functions from other files (in this case, `tester.py`), and provides the skeleton of the function we want you to write, `buildHisto`. This function takes four arguments:

1. `data` -- the input list of data points
2. `numbins` -- the number of bins (equally spaced) you want in your histogram
3. `minimum` -- the minimum range of your histogram
4. `maximum` -- the maximum range of your histogram

> Note that depending on how you write your histogram code, you may need
> to be careful with data points whose values are equal to the maximum
> range, to ensure that you put them in the correct bin (the last one)
> -- for our purposes, we are making an exception to the right boundary
> of a bin's range being exclusive.

There are also two other commented-out sections of code, which you can use along the way to completing the homework.

> If you want to do this step using Jupyter Notebook instead of a
> regular Python script, please modify `hw1.ipynb` instead of `hw1.py`.

## 3) Perform the following data analyses

Answer the following questions, using the code you have written in part 2 (you may have to write additional code). Your writeup (if you are not using a Jupyter Notebook) should be in a Word document called `hw1.doc` or a PDF called `hw1.pdf`.

1. Using the `buildHisto` function you wrote, create a histogram with 10 bins and plot it. Save the resulting plot in `hist1.png`. Describe what the histogram is showing you. Set the minimum and maximum values of the histogram as `0.0` and `100.0`. (Some code to help you get started with this is already in `hw1.py`)

2. Create a histogram with 200 bins and plot it. Save the resulting plot in `hist2.png`. Describe what the histogram is showing you.

3. How many bins would be good for this data set? Why? Using that number of bins, plot a histogram and save it in `hist3.png`. Describe what this histogram is telling you about the data.

4. Randomly select 10% of the data points from the input data set, and plot those with the same number of bins you determined in #3, saving the result in `hist4.png`. Describe the results. What happens if you use 1000 bins for your sampled data? Is there any benefit to using more than 1000 bins (hint: looking at the raw data may help you answer this question)? (You may find [`numpy.random.choice`](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.random.choice.html) useful in performing your random sample; remember to sample without replacement!)

5. **BONUS (worth 5 points)** Your histogram routine is written to produce *uniform width* bins. Is there any kind of data set where it might be more useful to have *variable width* bins (some bins span a wider range of data points than others)? Explain.

6. **BONUS (worth 10 points)** Write a function to compute cross validation for a given histogram, as described in Lecture 2. Use this information to determine the optimal bin width for the data set we gave you. Write up your results (a plot showing cross validation scores for different bin widths will be very useful here!)

> If you want to do this step using a Jupyter notebook instead of
> writing Python code plus a separate writeup, you can do so. In that
> case, you can use the `show` function of `pyplot` to display your
> plots inline in your notebook (use `%matplotlib inline` on the
> first line of the notebook) instead of saving the figures. To call
> `plotHisto` in "inline" mode, pass the additional parameter `True` to
> the function:
>
> `plotHisto(histo, 'histo1.png', 0.0, 100.0, plotinline = True)`

# Hints and tips

You may find the following Python functions useful:

* `min()` and `max()` will return the minimum and maximum, respectively, of an input list of data.
* `int()` will return an integer (using floor) when passed a floating point value. You may find this useful when trying to convert a floating point value to a bin index.
* In class, we saw `len()` used to tell us the length of a string. This function can also tell us the number of elements in a list.

# What you need to submit

If you are modifying `hw1.py`, please submit the modified python file, plus the four `.png` files we asked you to generate, plus a file called either `hw1.doc` or `hw1.pdf` with your answers to the questions.

If you are modifying `hw1.ipynb`, please submit that file. We expect your answers to the questions to be written up in the notebook, and all the required plots to be included inline.

# Submitting your code

Please tag the version of the code that you want to submit with `submission`, as you did in HW0.