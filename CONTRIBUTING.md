# Contributing Document

Thanks for taking some time to check out this document, I hope it goes a long way
to helping you contribute to this repo.

## Quick Overview

First things first, this repo is mainly a catalog of all of The Renegade Coder's 
How to Python series content. The main purpose of this repo is to display
this content in an easy-to-read format in the main README. This README is 
currently automatically generated through a combination of GitHub Actions
an Python code.

However, in addition to the README, there are plenty of gold nuggest throughout
the repo. For example, the following folders feature additional content:

- Challenges: a list of all of the How to Python challenges with solutions and testing
- Notebooks: a list of all articles in Jupyter Notebook format
- Testing: a list of performance tests for all solutions

In the following subsections, we'll take a look at how you can contribute to each of
these collections.

## Challenges

In every article in the How to Pythons series, there is a coding challenge. The goal
of the challenges collection is to provide a place where folks can share their
solutions to each challenge. 

Each challenge is in a folder that is named after the article it originates from. Inside
this folder, you'll find a README which summarizes the challenge. In addition, you'll find
a solution file which shares the name of the function that is to be implemented (e.g.,
capitalize.py). In this solution file, all of the functions will share the same name
followed by a number (e.g., capitalize_1()). These solutions are then tested automatically
through a test file that shares the name of the solution file (e.g., test_capitalize.py). 
This test file is automatically executed through GitHub actions using pytest. 

To aid in our efforts to expand this collection, you're welcome to provide solutions,
migrate challenges that have not be included yet, and write tests.
