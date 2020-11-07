# Data related jobs overview
* Created a tool that predicted the salary of data related jobs (MAE~ $11.9k) to help data scientist negotiate for their salaries.
* Investigated the inlflunetioal features with a significant effect on the salary, and the skillset required for differnt job titles 
* Scrapped 10000+ data related jobs (data analyst, data science, data engineer, data architect and machine learning engineer) across The US, over the priod of a month
* Cleaned the data and extracted and engineered features from the job description text
* Built several regressors, evaluated and optimized their preformance
* Built a client facing API using flask

## Motivation
Data related jobs (data scientist, data analyst, machine learning engineer etc.) are among the hottest jobs, and target of the majority of job seekers. The Glassdoor report has placed them among the best jobs based on the satisfaction rating, median annual base salary and the number of job opening. To be successful in this competitive market, a job seeker should identify what skills are highly valued in the market, attempt to learn and add them to his/her skillsets, and more importantly customize his/her resume, cover letters, online profiles, portfolios to demonstrate them as much as possible. This project attempts to help you to be a smart job seeker and tell you what qualities and top skills the market desires for each type of data related positions, and a step further, helps you navigate the salary negotiation and make the best choice.

## Code and resources used
* Python Version:** 3.7
* Packages:** pandas, numpy, scikitlearn, nltk, matplotlib, re, seaborn, flask, selnium, pickle
* Scraper article: https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905

## Web Scraping
Tweaked the web Scraper to scrape 10000+ job postings from glassdoor.com. Each job we got the following:
* Job title
* Job description (the whole description)
* Rating
* Location
* Company size (number of employees)
* Industry
* Sector
* Revenue
* Type of ownership
* Company founded year
* Salary range (predicted by Glassdoor or provided by the employer)

## Data Cleaning
After scraping the jobs from glassdoor, data cleaning was performed:
* Dropped the duplicates, and jobs without predicted salaries
* Dropped jobs with missing info, since they were less than 10%
* Extracted numeric values for salary from the salary range predcited by glassdoor or reported by employers
* Extracted the average years of experience required for the job
* Formed 5 categories for titles and put jobs in them based on the scraped job titles
* Extracted the seniorty level of the jobs the scraped job titles
* Extracted state out of location 
* Made columns for some common data tools if they were required by the jobs (python, machine learning, deep learning, big data, cloud computing)


## EDA
![GitHub Logo](pie_chart_salary_distribution.jpg)



