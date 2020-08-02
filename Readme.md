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

## Why I'm the ideal candidate for Hellofresh and this position

- Combining an extensive Business Education with a lot of Technical know-how, both are a absolute must haves for successful BI and Data Analysis (/Science) projects.
- Lot's of practical experience in Project Management, Consulting, Coding Projects and Stakeholder Management
- I'm very much a go-getter and quite ambitious, which I feel suits very well with the company culture.
- Great academic results (Accepted into Honors program, only 25 students each year get selected out of my whole Faculty), proving that I can work diligently and know what I'm doing instead of just importing- and running Python libraries .

## Why This Job

- I would absolutely love to be able to work on real life data, with real life impact
- The Amsterdam office seems to have strong Data Science and BI focus, or is seriously trying to expand it's expertise in this matter. Either way: awesome situation for an ambitious student like me.
- (Probably) working under Willem Lankhorst, who has had an interesting previous career at BCG.
- Hellotech would allow me to quickly make huge strides in my technical prowess, the feed of the Friday event on Twitter seems so cool!
- The timing from September until January/February 2021 is perfect as a combination with writing my masterthesis.

## Why HelloFresh

- Founded in 2011 and just a year ago reached 2,5 million (!) active customers.
- Small enough to not be bureaucratic, big enough to have an extensive network, lots of data and maybe an international career, given it's growth.
- The Amsterdam office has great reviews on Glasdoor.be
- Hellofresh' core values really resonate with my own.
    1. Maintaining an egoless environment.  I'm a big believer striving to be the absolute best, while staying humble and actively seeking out criticism, which is the only way to get even better.
    2. Continuous learning. Being able to both challenging myself and the status quo on a continuous basis is an absolute must in any position I consider. I'm very much a self-taught data-analyst and I need to be able to continue on that path
    3. Data-driven. What gets measured gets managed, show me the data and I'll believe you. It's as simple as that.
- I like free fruit and sports classes! 


## Why wouldn't I want to work for Hellofresh

- Not a Dutch company, it's main office is in Germany. Which might be a problem further down the road as local employees tend to be most able to quickly climb trough the ranks. Currently as a temporary employee not an issue however.
- Fear that the company still too bureaucratic. I'm a very entrepreneurial spirit: I work best having as much agency as possible, but I also can handle the burden of having nowhere to hide when something goes wrong, taking responsibility and handing fair criticism. 



