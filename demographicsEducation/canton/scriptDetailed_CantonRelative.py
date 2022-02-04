# Connect Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Import Pandas Library
import pandas as pd

# Set Cantons and Periodicity
canton = ['AG', 'AI', 'AR', 'BE', 'BL', 'BS', 'FR', 'GE', 'GL', 'GR', 'JU', 'LU', 'NE', 'NW', 'OW', 'SG', 'SH', 'SO', 'SZ', 'TG', 'TI', 'UR', 'VD', 'VS', 'ZG', 'ZH']
periodicity = list(range(2016, 2021))

# Create New Dictionary
dictURL = {}

# Create Corresponding URLs and Store Them in the Dictionary Created Beforehand
for c in canton:
  for year in periodicity:
    dictURL['{0}_{1}'.format(year,c)] ='https://raw.githubusercontent.com/epicalekspwner/OpenDataCustomerAnalytics/main/demographicsEducation/canton/' + str(c) + '/Absolute/'  + str(year) +'_' + str(c) + '_demographicsEducation_Absolute.csv'

# Get the Dictionary Keys to Access the URLs
keys = list(dictURL.keys())

# Create New Dictionary for Storing the DataFranes
dictDataFrames = {}

# Accessing the Original Datasets Through URLs and Converting Them Into DataFrames
for i in range(len(keys)):
  dictDataFrames['{0}'.format(keys[i])] = pd.read_csv(dictURL[keys[i]])

# Get Column Names and Drop Useless Attribute for Relativeness
attr = list(dictDataFrames[keys[0]].columns)
attrToBeRemoved = ['total', 'attribute', 'total_IC','withoutPostCompulsoryEducation_IC','secondLevel2ProfessionalTraining_IC','secondLevel2GeneralTraining_IC','thirdLevelHigherProfessionalTraining_IC','thirdLevelUniversities_IC']
for i in attrToBeRemoved:
  attr.remove(i)

# Get Column Names For IC Percent Formating
attr_IC = ['total_IC','withoutPostCompulsoryEducation_IC','secondLevel2ProfessionalTraining_IC','secondLevel2GeneralTraining_IC','thirdLevelHigherProfessionalTraining_IC','thirdLevelUniversities_IC']

# Iteration and Convertion Into Percentage (Within Canton)
for i in range(len(dictDataFrames)):
  for j in attr:
    dictDataFrames[keys[i]][j] = round(dictDataFrames[keys[i]][j]/dictDataFrames[keys[i]]['total'], 4)
  for k in attr_IC:
    dictDataFrames[keys[i]][k] = round(dictDataFrames[keys[i]][k]/100, 3)
for i in range(len(dictDataFrames)):
  dictDataFrames[keys[i]]['total'] = round(dictDataFrames[keys[i]]['total']/dictDataFrames[keys[i]]['total'], 4)
    
# Export DataFrames
for i in dictDataFrames.keys():
  exportLink = '/content/drive/MyDrive/Datasets1/{0}/{1}_demographicsEducationCantonRelative.csv'.format(i[-2:],i)
  dictDataFrames[i].to_csv(exportLink, na_rep = 'NaN', index = False)
