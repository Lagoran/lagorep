'''
So far, you've parsed dates that pandas could interpret automatically. But if a date is in a non-standard format, like 19991231 for December 31, 1999, it can't be parsed at the import stage. Instead, use pd.to_datetime() to convert strings to dates after import.

The New Developer Survey data has been loaded as survey_data but contains an unparsed datetime field. We'll use to_datetime() to convert it, passing in the column to convert and a string representing the date format used.

For more on date format codes, see this reference. Some common codes are year (%Y), month (%m), day (%d), hour (%H), minute (%M), and second (%S).

pandas has been imported as pd.

Instructions 2/3
1 XP
Parse Part2EndTime using pd.to_datetime(), the format keyword argument, and the format string you just identified. Assign the result back to the Part2EndTime column.

Hint
You can go back to Step 1 to view the string by clicking the step in the Instructions bar.
Make sure the format argument describes the datetimes as they appear, including separators like colons or spaces.
The format keyword must be specified.
'''

import pandas as pd

# Load file, supplying the dict to parse_dates
survey_data = pd.read_excel("c:/Users/a1bg468812/PycharmProjects/lagorep/Data Engineer with Python/Data files/fcc-new-coder-survey.xls"
                            ,
                            header=2
                            #parse_dates=datetime_cols,
                            #parse_dates=[62]
                            )

print(survey_data.head())
print(survey_data['Age'].head())
print(survey_data['Part2EndTime'].head())


# Parse datetimes and assign result back to Part2EndTime
#survey_data["Part2EndTime"] = pd.to_datetime(survey_data["Part2EndTime"],
#                                             format="%m%d%Y %H:%M:%S")

# Print first few values of Part2EndTime
#print(survey_data.Part2EndTime.head())
