# Homework 3 : Estimation and Confidence Intervals

This homework looks at using various techniques for making determinations of statistical significance. It is due March 2nd.

# Goals

In this assignment you will:
* Use a p-test to determine the statistical significance of sample means
* Use *bootstrapping* to study sample means and variances.

# Background

In this assignment, we will be studying a [real world data set](https://web.stanford.edu/~hastie/ElemStatLearn/datasets/prostate.info.txt), drawn from [here](https://web.stanford.edu/~hastie/ElemStatLearn/), included as `hw03.csv`. This data set shows a bunch of features for prostate cancer patients (columns 1 through 8 of the dataset), as well as an outcome variable (column 9). (Note that there's also a "column 0" that just gives the data point index.) Finally, each of the data points is classified as part of the *training set* or *testing set* (column 10; a `T` indicates training and an `F` indicates testing).

The reason we break data sets up into training and testing is in helping us build predictive models: can the values of the features help us predict the outcome variable? As part of this process, we use two data sets: a *training* data set that we use to build the model, and a *testing* data set that we use to test the predictions it makes (we can't use the same data set for both -- we want to know how the trained model will perform on *new* data).  We will talk much more about predictive models in later lectures of the course; this assignment isn't really about that.

One important thing to understand when building a model is whether the training data set has different characteristics than the testing data set (if it does, that increases the chances that a model built using the training data will not do a good job of predicting the test data). In this assignment, we will use various statistical techniques to probe the characteristics of our data set.

# Instructions

## 0) Set up your repository for this homework.

Click the link on Blackboard to set up a repository for homework 3, then clone it, as you did for homework 0.

The repository should contain 5 files:

1. This README
2. An input data file called `hw03.csv`
3. A helper file called `csv_reader.py` (this is slightly different than the one from homework 2).

## 1) Homework Problem 1: Confidence intervals

For problem 1, put your code in a file called `hw3_1.py` and your writeup in a file called `hw3_1.doc` or `hw3_1.pdf`. If you are using Jupyter Notebook, put your code and writeup in `hw3_1.ipynb`

The objective of this problem is to investigate whether there is any significant difference between the training and testing portion.
First of all, you need to classify the data into training and testing. You can write a Python function to perform this task by checking the indicators in the last column. (You can use the csv reader function given in `csv_reader.py`, which will give you tuples of data similar to hw2 to process, or you can directly use Pandas dataframes to do this).

Now, there are 8 features: `lcavol`, `lweight`, etc. For each feature, and for each class, we can compute their sample mean. That is, for `lcavol` we will compute a mean `mu1` for class T, and `mu0` for class F. We can also compute the sample variance `sigma1` and `sigma0`, the number of samples `n1` and `n0`.

>Depending on which computing platform you use, the way sample variance being calculated could be different. For example, in Python, sample variance is defined as
>
> S^2 = (1/N) sum(i=1 to N) (X_i - Xbar)^2
>
>whereas in MATLAB the sample variance is defined as
>
>S^2 = (1/(N-1)) sum(i=1 to N) (X_i - Xbar)^2.
>
>The difference between the two is subtle. The reason why MATLAB prefers (N-1) is that (N-1) will ensure the calculated S^2 unbiased. What is bias? Remember S^2 is a function of the random variables X_1, … X_N. So S^2 itself is a random variable and has its own distribution (aka histogram). The mean of S^2, ideally, should equal to the true variance sigma^2. However, this can only happen when you define S^2 using (N-1). If you use N, then the calculated S^2 will have a mean different from sigma^2. Which one is better? Practically this does not cause a problem, especially when N is reasonably large. It will become an issue when N is small. In this homework exercise, you can use either.


Given these statistical values, we want to check whether a feature X has a sample mean significantly different between class T and class F. To do so, we can use the p-value method. Let's assume that the tolerance level is alpha = 0.05 on both tails (so totally 0.1, which is 10%). We want to check whether mu0 and mu1 are close. Write a Python program and determine which of the eight feature has significant difference in its sample mean among the two classes. 

In your writeup, explain your procedure for determining whether the means have a statistical difference and tell us which feature *does* have a significant difference between the training and testing sets.

## 2) Homework Problem 2: Bootstrap

For problem 2, put your code in a file called `hw3_2.py` and your writeup in a file called `hw3_2.doc` or `hw3_2.pdf`. If you are using Jupyter Notebook, put your code and writeup in `hw3_2.ipynb`

In this part of the exercise, we like to use bootstrap to estimate the confidence interval of the sample means. 

First of all, for each feature and for each class, estimate the sample means and the sample variance. The confidence interval is then mu +/- z\_alpha sigma/sqrt(n) where n is the number of samples. In this exercise we can let z\_alpha = 1 for simplicity. (By the way, what is the corresponding alpha that makes z_alpha = 1?)

Now, write a bootstrap algorithm to estimate the confidence interval. In your bootstrap algorithm, you can repeat the simulation for T = 10000 times. For each time, you pick n samples randomly *with replacement*, where n is the number of data points for that feature. Then, compute the variance across these T simulations.

Compare the bootstrapped confidence interval and the confidence interval you would obtain directly. If you did everything right, these two numbers should be similar.

Next, among all the 8 features, which feature has a more reliable sample mean? Justify your answer from the bootstrapped confidence interval. 

**Bonus**: Repeat the bootstrap steps for median instead of the mean. Report what you find.


# What you need to submit

Each of the homework problems specify what file(s) to generate and submit for
that problem. Remember that if you are writing code in a `.py` file, you must
include your writeup in an accompanying `.doc` or `.pdf` file. If you are
writing code in a `.ipynb` file, your writeup should be included inline.

# Submitting your code

Please tag the version of the code that you want to submit with `submission`, as you did in HW0.

Don't forget to commit the code that you want to submit *before* tagging your submission. You have to do this in two steps.