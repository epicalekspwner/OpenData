# Connect Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Import Pandas Library
import pandas as pd

# Import, Load Data Into DataFrames & Replace 'XXX' With Actual Token
df2016 = pd.read_csv('https://raw.githubusercontent.com/epicalekspwner/OpenDataCustomerAnalytics/main/demographicsEducation/byCanton/AG/2016_AG_demographicsEducationAbsolute.csv')
df2017 = pd.read_csv('https://raw.githubusercontent.com/epicalekspwner/OpenDataCustomerAnalytics/main/demographicsEducation/byCanton/AG/2017_AG_demographicsEducationAbsolute.csv')
df2018 = pd.read_csv('https://raw.githubusercontent.com/epicalekspwner/OpenDataCustomerAnalytics/main/demographicsEducation/byCanton/AG/2018_AG_demographicsEducationAbsolute.csv')
df2019 = pd.read_csv('https://raw.githubusercontent.com/epicalekspwner/OpenDataCustomerAnalytics/main/demographicsEducation/byCanton/AG/2019_AG_demographicsEducationAbsolute.csv')
list_dataset = [df2016, df2017, df2018, df2019]

# Get Column Names and Drop Useless Attribute
attr = list(df2016.columns)
attr.remove('total')
attr.remove('attribute')
IC = ['total_IC','withoutPostCompulsoryEducation_IC','secondLevel2ProfessionalTraining_IC','secondLevel2GeneralTraining_IC','thirdLevelHigherProfessionalTraining_IC','thirdLevelUniversities_IC']
for i in IC:
  attr.remove(i)

# Iteration and Convertion Into Percentage (Within Canton)
for i in list_dataset:
  for j in attr:
    i[j] = round(i[j]/i['total'], 4)
for i in list_dataset:
  i['total'] = round(i['total']/i['total'], 4)
  
# Export Processed DataFrames
df2016.to_csv('/content/drive/MyDrive/Datasets/2016_AG_demographicsEducationCantonRelative.csv')
df2017.to_csv('/content/drive/MyDrive/Datasets/2017_AG_demographicsEducationCantonRelative.csv')
df2018.to_csv('/content/drive/MyDrive/Datasets/2018_AG_demographicsEducationCantonRelative.csv')
df2019.to_csv('/content/drive/MyDrive/Datasets/2019_AG_demographicsEducationCantonRelative.csv')
