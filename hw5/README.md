# Homework 5 : Classification

This homework looks at using two different techniques to classify pixels in an image (of a cat) as either foreground ("cat") or background ("grass").

This homework is due April 6th.

# Goals

In this assignment you will:

* Build a naive Bayes classifier to perform pixel classification
* Build a k-nearest neighbor classifier to perform pixel classification.

# Background

This homework uses an image called `cat_grass.png`. Each pixel in this image can be assigned to the foreground ("It's a cat!") or the background ("It's just grass"). We have given you training data for the two classes, in `hw5_cat.txt` and `hw5_grass.txt`.

# Instructions

## 0) Set up your repository for this homework.

Click the link on Blackboard to set up a repository for homework 5, then clone it, as you did for homework 0.

The repository should contain 6 files:

1. This README
2. Training data called `hw5_cat.txt`, with pixels that are all in the class "cat," and `hw5_grass.txt`, with pixels that are all in the class "grass."
3. A PDF with the homework writeup called `hw05.pdf`
4. A helper file called `helper.py` that has a helper function for normalizing your data.
5. A test image, `cat_grass.png` whose pixels you will classify.

## 1) Homework Problem 1: Naive Bayes

For problem 1, put your code in a file called `hw5_1.py` and your writeup in a file called `hw5_1.doc` or `hw5_1.pdf`. If you are using Jupyter Notebook, put your code and writeup in `hw5_1.ipynb`.

Do exercise 1 from `hw05.pdf`

We ask you to generate an image at the end of problem 1. Please generate an image called `hw5_1.png`

## 2) Homework Problem 2: Bootstrap

For problem 1, put your code in a file called `hw5_1.py` and your writeup in a file called `hw5_1.doc` or `hw5_1.pdf`. If you are using Jupyter Notebook, put your code and writeup in `hw5_1.ipynb`.

Do exercise 1 from `hw05.pdf`

We ask you to generate an image at the end of problem 1. Please generate an image called `hw5_2.png`

# What you need to submit

Each of the homework problems specify what file(s) to generate and submit for
that problem. Remember that if you are writing code in a `.py` file, you must
include your writeup in an accompanying `.doc` or `.pdf` file. If you are
writing code in a `.ipynb` file, your writeup should be included inline.

Please also include the two generated images in your submission.

# Submitting your code

Please tag the version of the code that you want to submit with `submission`, as you did in HW0.

Don't forget to commit the code that you want to submit *before* tagging your submission. You have to do this in two steps.