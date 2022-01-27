# Connect Google Drive to Colab
from google.colab import drive
drive.mount('/content/drive')

# Import Pandas Library
import pandas as pd

# Import, Load Data Into DataFrames & Replace 'XXX' With Actual Token
df2016 = pd.read_csv('https://raw.githubusercontent.com/epicalekspwner/OpenDataCustomerAnalytics/main/demographicsStructure/2016_demographicsStructureAbsolute.csv?token=XXX')
df2017 = pd.read_csv('https://raw.githubusercontent.com/epicalekspwner/OpenDataCustomerAnalytics/main/demographicsStructure/2017_demographicsStructureAbsolute.csv?token=XXX')
df2018 = pd.read_csv('https://raw.githubusercontent.com/epicalekspwner/OpenDataCustomerAnalytics/main/demographicsStructure/2018_demographicsStructureAbsolute.csv?token=XXX')
df2019 = pd.read_csv('https://raw.githubusercontent.com/epicalekspwner/OpenDataCustomerAnalytics/main/demographicsStructure/2019_demographicsStructureAbsolute.csv?token=XXX')
df2020 = pd.read_csv('https://raw.githubusercontent.com/epicalekspwner/OpenDataCustomerAnalytics/main/demographicsStructure/2020_demographicsStructureAbsolute.csv?token=XXX')
list_dataset = [df2016, df2017, df2018, df2019, df2020]

# Get Column Names and Drop Useless Attribute
attr = list(df2016.columns)
attr.remove('region')

# Iteration and Convertion Into Percentage (Within Country)
for i in list_dataset:
  for j in attr:
    i[j] = round(i[j]/i[j][26], 4)

# Export Processed DataFrames
df2016.to_csv('/content/drive/MyDrive/Datasets/2016_demographicsStructureCountryRelative.csv')
df2017.to_csv('/content/drive/MyDrive/Datasets/2017_demographicsStructureCountryRelative.csv')
df2018.to_csv('/content/drive/MyDrive/Datasets/2018_demographicsStructureCountryRelative.csv')
df2019.to_csv('/content/drive/MyDrive/Datasets/2019_demographicsStructureCountryRelative.csv')
df2020.to_csv('/content/drive/MyDrive/Datasets/2020_demographicsStructureCountryRelative.csv')
