# script_CantonRelative
# Convert Absolute Values Into Relative Ones (Within Canton)
# /demographicsEducation/

# Import Pandas Library
import pandas as pd

# Set Periodicity
periodicity = list(range(2016, 2021))

# Create New Dictionary
dictURL = {}

# Create Corresponding URLs and Store Them in the Dictionary Created Beforehand
for year in periodicity:
    dictURL['{0}'.format(year)] = 'https://raw.githubusercontent.com/epicalekspwner/OpenDataCustomerAnalytics/main/demographicsEducation/' + str(year) + '_demographicsEducation_Absolute.csv'

# Get the Dictionary Keys to Access the URLs
keys = list(dictURL.keys())

# Create New Dictionary for Storing the DataFranes
dictDataFrames = {}

# Accessing the Original Datasets Through URLs and Converting Them Into DataFrames
for i in range(len(keys)):
    dictDataFrames['{0}'.format(keys[i])] = pd.read_csv(dictURL[keys[i]])

# Get Column Names and Drop Useless Attribute for Relativeness
attr = list(dictDataFrames[keys[0]].columns)
attrToBeRemoved = ['region', 'total', 'total_IC', 'withoutPostCompulsoryEducation_IC', 'secondLevel2ProfessionalTraining_IC',
                   'secondLevel2GeneralTraining_IC', 'thirdLevelHigherProfessionalTraining_IC', 'thirdLevelUniversities_IC']
for i in attrToBeRemoved:
    attr.remove(i)

# Iteration and Convertion Into Percentage (Within Canton)
for i in range(len(dictDataFrames)):
    for j in attr:
        dictDataFrames[keys[i]][j] = round(dictDataFrames[keys[i]][j] / dictDataFrames[keys[i]]['total'], 4)
for i in range(len(dictDataFrames)):
    dictDataFrames[keys[i]]['total'] = round(dictDataFrames[keys[i]]['total'] / dictDataFrames[keys[i]]['total'], 4)

# Export DataFrames
for i in dictDataFrames.keys():
    exportLink = 'C:/Users/aleks/OneDrive/Documents/GitHub/OpenDataCustomerAnalytics/demographicsEducation/{0}_demographicsEducation_CantonRelative.csv'.format(i)
    dictDataFrames[i].to_csv(exportLink, na_rep='NaN', index=False)
