'''
An Excel workbook may contain multiple sheets of related data. The New Developer Survey response workbook has sheets for different years. Because read_excel() loads only the first sheet by default, you've already gotten survey responses for 2016. Now, you'll create a data frame of 2017 responses using read_excel()'s sheet_name argument in a couple different ways.

pandas has been imported as pd.

Instructions 1/2
50 XP
Instructions 1/2
50 XP
Create a data frame from the second workbook sheet by passing the sheet's position to sheet_name.

Create a data frame from the 2017 sheet by providing the sheet's name to read_excel().
'''
# Load pandas as pd
import pandas as pd
import matplotlib as plt

# Create df from second worksheet by referencing its position
responses_2017 = pd.read_excel("c:/Users/a1bg468812/PycharmProjects/lagorep/Data Engineer with Python/Data files/fcc-new-coder-survey.xlsx",
                               sheet_name=1)

# Graph where people would like to get a developer job
#job_prefs = responses_2017.groupby("c:/Users/a1bg468812/PycharmProjects/lagorep/Data Engineer with Python/Data files/fcc-new-coder-survey.xlsx").JobPref.count()
#job_prefs.plot.barh()
#plt.show()

# Load both the 2016 and 2017 sheets by name
all_survey_data = pd.read_excel("c:/Users/a1bg468812/PycharmProjects/lagorep/Data Engineer with Python/Data files/fcc-new-coder-survey.xlsx",
                                sheet_name=['2016','2017'])

# View the data type of all_survey_data
print(type(all_survey_data))