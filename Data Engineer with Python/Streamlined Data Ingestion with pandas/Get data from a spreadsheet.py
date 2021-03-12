'''
Get data from a spreadsheet
In this exercise, you'll create a data frame from a "base case" Excel file: one with a single sheet of tabular data. The fcc_survey.xlsx file here has a sample of responses from FreeCodeCamp's annual New Developer Survey. This survey asks participants about their demographics, education, work and home life, plus questions about how they're learning to code. Let's load all of it.

pandas has not been pre-loaded in this exercise, so you'll need to import it yourself before using read_excel() to load the spreadsheet.

Instructions
100 XP
Load the pandas library as pd.
Read in fcc_survey.xlsx and assign it to the variable survey_responses.
Print the first few records of survey_responses.
'''

# Load pandas as pd
import pandas as pd

# Read spreadsheet and assign it to survey_responses
survey_responses = pd.read_excel("c:/Users/a1bg468812/PycharmProjects/lagorep/Data Engineer with Python/Data files/fcc-new-coder-survey.xlsx",
                                 header=2)

# View the head of the data frame
print(survey_responses.head())

# Create string of lettered columns to load
col_string = "AD,AW:BA"

# Load data with skiprows and usecols set
survey_responses = pd.read_excel("c:/Users/a1bg468812/PycharmProjects/lagorep/Data Engineer with Python/Data files/fcc-new-coder-survey.xlsx",
                        skiprows=2,
                        usecols=col_string)

# View the names of the columns selected
print(survey_responses.columns)