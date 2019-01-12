# Homework 2 : Sampling and Distributions

This homework asks you to experiment with sampling to make estimates of distributions.

# Goals

In this assignment you will:
* Use `numpy` sampling to draw samples from a given distribution
* Estimate the parameters of the distribution, and describe your findings
* Use filtering to figure out which *features* of a dataset are important.

# Background

## Distributions

In Lecture 5, we discussed the idea of data having a *distribution* -- the
"shape" of the data follows some known pattern. For example, the possible
number of heads you see after 1000 coin flips follows a *binomial*
distribution. Many statistical methods that we use to understand the patterns
in data rely on assumptions about the distribution of the underlying data. For
example, the number of people arriving at an escalator in a one-hour time
window (remember Lecture 3!) is often modeled as a *Poisson* distribution.

In this homework, we will explore various properties of data sets to
understand their distributions.

## Sampling

One of the most important topics in data analytics is *sampling*. In many
situations, your goal is to draw conclusions about a data set or a population
where you do not have access to *all* of the data. Instead, you only have
access to a subset, or *sample* of the data (this could be because operating
on the entire data set or even *collecting* the data in the first place is
prohibitively expensive).

There are many different approaches to sampling (you could devote an entire
course to it!) In this course we will focus primarily on *uniform random
sampling*, where each element of the underlying data set is equally likely to
appear in the sample we are studying.

In this homework, we will compute properties like *sample mean* (the mean of a
sample) and consider how this property is affected by things like the size of
the sample, or by the randomness introduced by sampling.

If you have a list of data in Python, the `numpy` function `random.choice` will let you sample the data:

`numpy.random.choice(data, sampleSize, replace=False)`

Note that we want to set `replace=False` to make sure that we don't sample the same element from the data set more than once.

## Feature selection

Later in this class, we will spend a lot of time talking about *features* of data: a given element in a data set can be described by a wide variety of *features* that, combined, describe the data point (think of a set of features describing yourself: your height, eye color, hair color, etc.) When investigating a data set, some features are important (their value has some connection to the property you're studying) and others are not (their value does not really affect the property you're studying).

An important part of data analysis is determining which features matter for a given problem. This homework will only investigate this task in a high-level way; we will talk more about understanding correlations between features later.

# Instructions

## 0) Set up your repository for this homework.

Click the link on Blackboard to set up a repository for homework 2, then clone it, as you did for homework 0.

The repository should contain 5 files:

1. This README
2. 5 input data files, called `hw02_problem1.csv`, `hw02_problem2a.csv`, `hw02_problem2b.csv`, `hw02_problem2c.csv`, and `hw02_problem3.csv`
3. A helper file called `csv_reader.py`

## 1) Homework Problem 1: Sampling

For problem 1, put your code in a file called `hw2_1.py` and your writeup in a file called `hw2_1.doc` or `hw2_1.pdf`. If you are using Jupyter Notebook, put your code and writeup in `hw2_1.ipynb`

Problem 1 of the homework uses the input dataset `hw02_problem1.csv`. You should do the following. 

1. Read this dataset into a Python list (you can use `numpy.loadtxt` function like you did in Homework 1)

2. Generate a random sample of `k = 50` data points from the input data set. Using the `plotHisto` function from Homework 1 (or the `matplotlib.pyplot.hist` function), plot the histogram. (Include this histogram in your homework writeup)

3. Repeat this process for `k` values of 200, 1000, and 5000, and one last time for the entire data set (`k = 10000`). Explain what you see: how does increasing `k` change the results? What happens if you re-generate the histograms?

4. Write a function `sampleMean` that takes two arguments: a data set and `k` to sample `k` items from the data set and compute the mean of the *sampled* data (you can use a reduction function like we discussed in Lecture 4, or you can use `numpy`'s built in `mean` function).

5. Use `sampleMean` to write code that generates a list of 1000 sample means computed from samples of size 100. Plot these sample means on a histogram. Include this resulting histogram in your writeup. Explain what you see. How would you interpret the *mean* of these sample means? The *variance*? What if you increase the number of sample means you collect to 10000? Describe the histogram you plotted in comparison to the mean of the *entire data set*.

## 2) Homework Problem 2: Distributions

For problem 2, put your code in a file called `hw2_2.py` and your writeup in a file called `hw2_2.doc` or `hw2_2.pdf`. If you are using Jupyter Notebook, put your code and writeup in `hw2_2.ipynb`

Problem 2 of the homework asks you to compute quantile-quantile (QQ) plots for three input data sets: `hw02_problem2a.csv`, `hw02_problem2b.csv`, `hw02_problem2c.csv`. 

Each of these data sets was generated using one of 8 possible distributions:

* Gaussian (`norm`)
* Cauchy (`cauchy`)
* Cosine (`cosine`)
* Exponential (`expon`)
* Uniform (`uniform`)
* Laplace (`laplace`)
* Wald (`wald`)
* Rayleigh (`rayleigh`)

For each data set, tell us which distribution was used to generate the data (you may find it helpful to plot histograms of the data sets). Use QQ plots as part of your answer. You may find the `scipy` function `probplot` useful for this. For example, the following code will create a QQ plot comparing an input data set to a Gaussian distribution:

```
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt(`hw02_problem2a.csv`)

stats.probplot(data, dist = 'norm', plot=plt)
plt.show() # modify this to write the plot to a file instead
```

(To compare to the other distributions, use the names in parentheses from the above list)

## 3) Homework Problem 3: Filtering data

For problem 3, put your code in a file called `hw2_3.py` and your writeup in a file called `hw2_3.doc` or `hw2_3.pdf`. If you are using Jupyter Notebook, put your code and writeup in `hw2_3.ipynb`

In this problem, we will consider a simple data analysis problem.
`hw02_problem3.csv` contains a set of data points. Each data point consists of
3 *features* (properties): a "score", then two colors: either "red" or
"green," and then either "black" or "white." So, for example, one data point
in the data set represents a piece of data with the properties `<7.39, red,
white>` while another represents a piece of data with the properties `<77.13,
green, black>`.

We will read this data into a Python list with a specific kind of structure:
each element in the list will represent one data point, and each data point
will be represented by a *tuple*, a python structure with three entries in it.
The first entry will be the score, the second entry will be the red/green
feature and the third entry will be the black/white feature.

> Python tuples are a little like immutable lists: you access the
> entries in a tuple using the same kind of array notation (`t[0]`
> accesses the first element in tuple `t`, etc.), but you cannot change
> how long they are (they don't have a method like `append`) and once
> you create a tuple you cannot change its values.
>
> We'll talk more about tuples and other data structures in Lecture 6

We have provided a helper routine in `csv_reader.py` that will read the given input file into the desired list of tuples. You can use it as follows:

```
from csv_reader import readData

data = readData(`hw02_problem3.csv`)

print data[0] #prints "(74.13, 'green', 'white')"
print data[0][0] #prints "74.13"
print data[0][1] #prints "green"
print data[0][2] #prints "white"
```

Using this data, perform the following tasks:

1. Plot the histogram of the score data in this data set. (Hint: write a
function that iterates over `data` and creates a new list using just the first
entry of each tuple). What does this histogram tell you about your data?

2. This data is created by taking two simple distributions of data and
combining them. Each data point is from one of the two distributions. The
value of *one* of the two features (the red/green feature or the black/white
feature) indicates which distribution a data point comes from. Which feature
is it? Explain how you figured this out, and present supporting code/data.
(Hint: you can combine the `filter` function that we wrote in Lecture 4 with
the function you wrote in task 1 of this problem to help generate the data you
need)

## 4) **BONUS Problem** (worth 10 points)

For this problem, put your code in a file called `hw2_bonus.py` and your
writeup in a file called `hw2_bonus.doc` or `hw2_bonus.pdf`. If you are using
Jupyter Notebook, put your code and writeup in `hw2_bonus.ipynb`

In problem 1, you used sampling to analyze a data set, computing sample mean
and sample variance. You also wrote a function called `sampleMean` that lets
you quickly draw a sample from a data set and compute its mean, then used that
function to study what happens if you draw *many* samples from a data set and
look at the sample means.

In problem 2, you looked at three different data sets with three different
distributions.

For this bonus problem, repeat the process of generating and plotting 10000
sample means for *each* of the data sets you used in problem 2. Describe your
findings. What is interesting about each of the sets of sample means you
found? In comparison to the true means of each data set?

> In answering this problem, you may find it interesting to read about the [Central Limit Theorem](https://en.wikipedia.org/wiki/Central_limit_theorem)

# What you need to submit

Each of the homework problems specify what file(s) to generate and submit for
that problem. Remember that if you are writing code in a `.py` file, you must
include your writeup in an accompanying `.doc` or `.pdf` file. If you are
writing code in a `.ipynb` file, your writeup should be included inline.

# Submitting your code

Please tag the version of the code that you want to submit with `submission`, as you did in HW0.

Don't forget to commit the code that you want to submit *before* tagging your submission. You have to do this in two steps.