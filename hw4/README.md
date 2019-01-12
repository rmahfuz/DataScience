# Homework 4 : Regression

This homework looks at using various techniques for making determinations of statistical significance. It is due March 23rd.

# Goals

In this assignment you will:

* Compute a linear regression to model the contribution of various factors to prostate cancer markers
* Use autoregression to predict stock prices

# Background

In this assignment, we will use several different data sets. For part 1 of the
assignment, we will use `hw04.csv` (which is the same prostate data set as
`hw03.csv` from the previous assignment -- you can use similar routines as
last time to read it in and process it). For part 2 of the assignment, we will
use `google_stock_train.txt` and `nvs_stock_train.txt`

This assignment will require performing a lot of matrix computations to compute your regressions. You will likely find NumPy's [matrix library](https://docs.scipy.org/doc/numpy/reference/generated/numpy.matrix.html) and [linear algebra library](https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.linalg.html) useful.

A few tips and tricks for using NumPy matrices and completing this assignment:

1. If you create a NumPy matrix, the attributes `.T` and `.I` will give you the transposed and inverse matrices, respectively. So `m.T` will give you the transposed version of matrix `m`.

2. Keep track of the dimensionality of your matrices, to make sure that you are computing things correctly. `.shape` will tell you the dimensions of your matrix. So if `m.shape` returns `(67, 8)`, that means that `m` is a 67x8 matrix.

3. `.mean(0)` will compute the column means of a matrix, and `.sum(0)` will compute the column sums of a matrix. So if you have a 67x8 matrix `m` and you compute `m.mean(0)`, you will get a new 1x8 matrix containing the means of each column.

4. Elementwise computation in NumPy is subtle, because it tries to do the "right" thing in ways you may not expect. If you want to subtract off a single value `x` from *each* element of a matrix `m`, `m - x` will do that. If `x` is instead a 1xC matrix, then `m - x` will subtract the "row" `x` from each *row* of `m`. Hence, `m - m.mean(0)` will subtract from each element in `m` the mean of the column that element is in.

5. If you are using numpy matrices, you cannot use `*` and `**` to do elementwise multiplication or exponentiation (those will instead do matrix multiplication and exponentiation). You will have to use `numpy.multiply` and `numpy.power` to do that.

# Instructions

## 0) Set up your repository for this homework.

Click the link on Blackboard to set up a repository for homework 4, then clone it, as you did for homework 0.

The repository should contain 6 files:

1. This README
2. Input data files called `hw04.csv`, `google_stock_train.txt`, and `nvs_stock_train.txt`
3. A PDF with the homework writeup called `hw04.pdf`
4. A helper file called `csv_reader.py` (this is the same as the file from HW 3).

## 1) Homework Problem 1: Regression

For problem 1, put your code in a file called `hw4_1.py` and your writeup in a file called `hw4_1.doc` or `hw4_1.pdf`. If you are using Jupyter Notebook, put your code and writeup in `hw4_1.ipynb`

Do exercise 1 from `hw04.pdf`

## 2) Homework Problem 2: Bootstrap

For problem 2, put your code in a file called `hw4_2.py` and your writeup in a file called `hw4_2.doc` or `hw4_2.pdf`. If you are using Jupyter Notebook, put your code and writeup in `hw4_2.ipynb`

Do exercise 2 from `hw04.pdf`

# What you need to submit

Each of the homework problems specify what file(s) to generate and submit for
that problem. Remember that if you are writing code in a `.py` file, you must
include your writeup in an accompanying `.doc` or `.pdf` file. If you are
writing code in a `.ipynb` file, your writeup should be included inline.

# Submitting your code

Please tag the version of the code that you want to submit with `submission`, as you did in HW0.

Don't forget to commit the code that you want to submit *before* tagging your submission. You have to do this in two steps.