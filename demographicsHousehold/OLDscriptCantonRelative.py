# Connect Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Import Pandas Library
import pandas as pd

# Set Periodicity From 2016 to 2020
periodicity = range(2016,2021)

# Create New Dictionary
dictURL = {}

# Create Corresponding URLs and Store Them in the Dictionary Created Beforehand
for year in periodicity:
  dictURL['df_{0}'.format(year)] = 'https://raw.githubusercontent.com/epicalekspwner/OpenDataCustomerAnalytics/main/demographicsHousehold/' + str(year) + '_demographicsHouseholdAbsolute.csv'

# Get the Dictionary Keys to Access the URLs
keys = list(dictURL.keys())

# Create New Dictionary for Storing the DataFranes
dictDataFrames = {}

# Accessing the Original Datasets Through URLs and Converting Them Into DataFrames
for i in range(len(keys)):
  dictDataFrames['{0}'.format(keys[i])] = pd.read_csv(dictURL[keys[i]])
  
# Get Column Names and Drop Useless Attribute
attr = list(dictDataFrames[keys[0]].columns)
attr.remove('region')
attr.remove('total')
attr.remove('averageSizeHousehold')

# Iteration and Convertion Into Percentage (Within Canton)
for i in range(len(dictDataFrames)):
  for j in attr:
    dictDataFrames[keys[i]][j] = round(dictDataFrames[keys[i]][j]/dictDataFrames[keys[i]]['total'], 4)
for i in range(len(dictDataFrames)):
  dictDataFrames[keys[i]]['total'] = round(dictDataFrames[keys[i]]['total']/dictDataFrames[keys[i]]['total'], 4)

# Export DataFrames
yearList = list(periodicity)
for i in range(len(dictDataFrames)):
  exportLink = '/content/drive/MyDrive/Datasets/{0}_demographicsHouseholdCantonRelative.csv'.format(yearList[i])
  dictDataFrames[keys[i]].to_csv(exportLink)
