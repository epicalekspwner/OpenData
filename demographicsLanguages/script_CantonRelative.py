# script_CantonRelative
# Convert Absolute Values Into Relative Ones (Within Canton)
# /demographicsLanguages/

# Import Pandas and OS Libraries
import pandas as pd
import os

# Set Periodicity
periodicity = list(range(2016, 2021))

# Create New Dictionary
dictURL = {}

# Create Corresponding URLs and Store Them in the Dictionary Created Beforehand
for year in periodicity:
    dictURL['{0}'.format(year)] = 'https://raw.githubusercontent.com/epicalekspwner/OpenDataCustomerAnalytics/main/demographicsLanguages/' + str(year) + '_demographicsLanguages_Absolute.csv'

# Get the Dictionary Keys to Access the URLs
keys = list(dictURL.keys())

# Create New Dictionary for Storing the DataFrames
dictDataFrames = {}

# Accessing the Original Datasets Through URLs and Converting Them Into DataFrames
for i in range(len(keys)):
    dictDataFrames['{0}'.format(keys[i])] = pd.read_csv(dictURL[keys[i]])

# Get Column Names and Drop Useless Attribute for Relativeness
attr = list(dictDataFrames[keys[0]].columns)
attrToBeRemoved = ['region', 'total', 'german_IC', 'french_IC', 'italian_IC', 'romansh_IC', 'english_IC', 'portuguese_IC', 'bosnianCroatianMontenegrinSerbian_IC', 'albanian_IC', 'spanish_IC', 'turkish_IC', 'otherLanguages_IC']
for i in attrToBeRemoved:
    attr.remove(i)

# Iteration and Convertion Into Percentage (Within Canton)
for i in range(len(dictDataFrames)):
    for j in attr:
        dictDataFrames[keys[i]][j] = round(dictDataFrames[keys[i]][j] / dictDataFrames[keys[i]]['total'], 4)

# Export Data With Automated Files Management
for i in dictDataFrames.keys():
    exportPath = 'C:/GitHub/OpenDataCustomerAnalytics/demographicsLanguages/'
    exportPathExist = os.path.exists(exportPath)
    if not exportPathExist:
        os.makedirs(exportPath)
    exportFile = 'C:/GitHub/OpenDataCustomerAnalytics/demographicsLanguages/{0}_demographicsLanguages_CantonRelative.csv'.format(i)
    dictDataFrames[i].to_csv(exportFile, na_rep='NaN', index=False)
