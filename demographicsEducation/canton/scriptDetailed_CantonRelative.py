# scriptDetailed_CantonRelative
# Convert Absolute Values Into Relative Ones (Within Canton)
# /demographicsEducation/canton/

# Import Pandas and OS Libraries
import pandas as pd
import os

# Set Cantons and Periodicity
canton = ['AG', 'AI', 'AR', 'BE', 'BL', 'BS', 'FR', 'GE', 'GL', 'GR', 'JU', 'LU', 'NE', 'NW', 'OW', 'SG', 'SH', 'SO', 'SZ', 'TG', 'TI', 'UR', 'VD', 'VS', 'ZG', 'ZH']
periodicity = list(range(2016, 2021))

# Create New Dictionary
dictURL = {}

# Create Corresponding URLs and Store Them in the Dictionary Created Beforehand
for c in canton:
    for year in periodicity:
        dictURL['{0}_{1}'.format(year, c)] = 'https://raw.githubusercontent.com/epicalekspwner/OpenDataCustomerAnalytics/main/demographicsEducation/canton/' + str(c) + '/Absolute/' + str(year) + '_' + str(c) + '_demographicsEducation_Absolute.csv'

# Get the Dictionary Keys to Access the URLs
keys = list(dictURL.keys())

# Create New Dictionary for Storing the DataFranes
dictDataFrames = {}

# Accessing the Original Datasets Through URLs and Converting Them Into DataFrames
for i in range(len(keys)):
    dictDataFrames['{0}'.format(keys[i])] = pd.read_csv(dictURL[keys[i]])

# Get Column Names and Drop Useless Attribute for Relativeness
attr = list(dictDataFrames[keys[0]].columns)
attrToBeRemoved = ['attribute', 'total', 'total_IC', 'withoutPostCompulsoryEducation_IC', 'secondLevel2ProfessionalTraining_IC', 'secondLevel2GeneralTraining_IC', 'thirdLevelHigherProfessionalTraining_IC', 'thirdLevelUniversities_IC']
for i in attrToBeRemoved:
    attr.remove(i)

# Iteration and Convertion Into Percentage (Within Canton)
for i in range(len(dictDataFrames)):
    for j in attr:
        dictDataFrames[keys[i]][j] = round(dictDataFrames[keys[i]][j] / dictDataFrames[keys[i]]['total'], 4)

# Export Data With Automated Files Management
for i in dictDataFrames.keys():
    exportPath = 'C:/GitHub/OpenDataCustomerAnalytics/demographicsEducation/canton/{0}/CantonRelative/'.format(i[-2:])
    exportPathExist = os.path.exists(exportPath)
    if not exportPathExist:
        os.makedirs(exportPath)
    exportFile = 'C:/GitHub/OpenDataCustomerAnalytics/demographicsEducation/canton/{0}/CantonRelative/{1}_demographicsEducation_CantonRelative.csv'.format(i[-2:], i)
    dictDataFrames[i].to_csv(exportFile, na_rep='NaN', index=False)
