'''
pandas does not infer that columns contain datetime data; it interprets them as object or string data unless told otherwise. Correctly modeling datetimes is easy when they are in a standard format -- we can use the parse_dates argument to tell read_excel() to read columns as datetime data.

The New Developer Survey responses contain some columns with easy-to-parse timestamps. In this exercise, you'll make sure they're the right data type.

pandas has been loaded as pd.

Instructions
100 XP
Load fcc_survey.xlsx, making sure that the Part1StartTime column is parsed as datetime data.
View the first few values of the survey_data.Part1StartTime to make sure it contains datetimes.
'''
import pandas as pd

# Load file, with Part1StartTime parsed as datetime data
survey_data = pd.read_excel("c:/Users/a1bg468812/PycharmProjects/lagorep/Data Engineer with Python/Data files/fcc-new-coder-survey.xls",
                            header=2,
                            parse_dates=[60],
                            sheet_name=None)

# Print first few values of Part1StartTime
print(survey_data.Part1StartTime.head())

#print only the header
#survey_data.head()

