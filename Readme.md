# 1) Project Description

## General overview

This repo consists of two separate- but related projects: 

'Sales Prediction' shows my AI knowledge and is meant to prove my usefulness as a BI (descriptive) /Data (predictive) Analyst (60% of the job). Although I could of course not showcase everything. For example: almost no Visualisation is present, due to the fact that this project was already getting quite sizable. 

'OOP' was written with the other 40% of the job in mind: helping Hellofresh transition to more sophisticated self-built tools.

I also opted to not do any Time Series Forecasting even though it will be a significant part of the BI position, and chose for a more vanilla project, predicting future sales. I consciously made this choice because TS-analyses are bit more of a niche topic within general DS. I do however posses the mathematical and technical skills from my Supply-Chain- and Production courses at the university, and took an online course in TS forecasting in Python a while back, but the topic of how to translate my theoretical knowledge to Python code is currently not fresh enough in my mind. It will however be a big requirement in the BI position and I'll very quickly get this knowledge back to the level that i want it to be.

## A) Sales Prediction  

In the first project ('Sales prediction') I want to showcase my knowledge of doing a basic AI learning project. The goal of this project is to (very quickly) do some basic EDA, Cleaning and training. 
Nothing really to add here in this readme, I provided a lot of documentation and comments in the Jupyter file itself.

## B) OOP
As 40% of the job I'm applying for consists of improving the tooling and transition to more sophisticated self-built tools, I felt that I had to prove to have some experience in OOP programming (Although 95% of my current work is Functional). Also a great opportunity to Work with an API, List comprehension, doing quite complex operations on json files,..What the project does is quite nonsensical (simulating someone who eats meals and gains calories), and is set up in a way so I can quickly show that I posses these core techniques. 

### 1) app.py
This is the main file. Only run this file and not the others.

It wil ask the user how many meals she wants to eat, gets that many meals from a json file (the one I received for my Python assigment) containing recipes, calculates the amount of calories in each recipe using a public API, it then counts how much each user has already eaten.

### 2) The classes
For the purpose of simulating someone eating, we define two classes: Recipe and Health, each with it's own distinct attributes and methods. The method names kinda speak for themselves but very brief:
 - 'get_total_calories' accepts a string of ingredients, passes this on to a public API to get an approximation of the calories for each ingredient. The result is then received as a json with a lot of information for each ingredient, which the method parses through to extract the total amount of calories for each ingredient. We then sum up the calories from each ingredient in the meal via a list comprehension and return the result as an int to the user
 - 'eat' accepts a, beforehand unknown, number of recipe names, pushed them trough the 'get_total_calories' method (in a way) to get the total number of calories of each recipe, messages the user each time something is 'eaten', and in the end prints the total number of calories eaten in that session.
 
Because we work with classes, the program will remember the total amount of calories eaten and will not forget it after the 'eating-session' (calling .eat() ) is over.


### BONUS: reasons_to_hire_me- function

The most important part of the whole project. You can skip all the rest.



# 2) Main Job Requirements 

- 60%: Support key operational BI
    - (Demand-) Forecasting (Statsmodels: ACF, PACF, ARIMA, Vector AutoRegression, maybe even Deep Learning using a RNN?,... )
    - Customer Behavior Analysis (Churn prediction, Visualisation, Clustering into Customer Segments, Predicting future food trends)

- 40%: Improving (Excel) tooling and transition to more sophisticated self-built tools
    - OOP-concepts
    - Basic Data Warehousing?

Goal: the task is to predict the demand for the next 10 weeks 

Data source: https://www.kaggle.com/kannanaikkal/food-demand-forecasting

GitHub repo: https://github.com/JonasHeymans/HelloFoodFreak (Access can be provided upon request)
