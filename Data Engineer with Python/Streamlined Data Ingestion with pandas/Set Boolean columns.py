'''
Datasets may have columns that are most accurately modeled as Boolean values. However, pandas usually loads these as floats by default, since defaulting to Booleans may have undesired effects like turning NA values into Trues.

fcc_survey_subset.xlsx contains a string ID column and several True/False columns indicating financial stressors. You'll evaluate which non-ID columns have no NA values and therefore can be set as Boolean, then tell read_excel() to load them as such with the dtype argument.

pandas is loaded as pd.

Instructions 1/2
50 XP
Count NA values in each column of survey_data with isna() and sum(). Note which columns besides ID.x, if any, have zero NAs.

'''
import pandas as pd

# Load the data
survey_data = pd.read_excel("c:/Users/a1bg468812/PycharmProjects/lagorep/Data Engineer with Python/Data files/fcc-new-coder-survey.xlsx")

# Count NA values in each column
print(survey_data.isna().sum())
print(survey_data)
print(survey_data.dtypes())

# Load file with Yes as a True value and No as a False value
survey_subset = pd.read_excel("c:/Users/a1bg468812/PycharmProjects/lagorep/Data Engineer with Python/Data files/fcc-new-coder-survey.xls",
                              dtype={"HasDebt": bool,
                              "AttendedBootCampYesNo": bool},
                              true_values=["Yes"],
                              false_values=["No"])

# View the data
print(survey_subset.head())