# Connect Google Drive to Colab
from google.colab import drive
drive.mount('/content/drive')

# Import Pandas Library
import pandas as pd

# Import and Load Data Into DataFrames
df2016 = 'https://raw.githubusercontent.com/epicalekspwner/OpenData/main/popStructure/2016_popStructureAbsolute.csv'
df2017 = 'https://raw.githubusercontent.com/epicalekspwner/OpenData/main/popStructure/2017_popStructureAbsolute.csv'
df2018 = 'https://raw.githubusercontent.com/epicalekspwner/OpenData/main/popStructure/2018_popStructureAbsolute.csv'
df2019 = 'https://raw.githubusercontent.com/epicalekspwner/OpenData/main/popStructure/2019_popStructureAbsolute.csv'
df2020 = 'https://raw.githubusercontent.com/epicalekspwner/OpenData/main/popStructure/2020_popStructureAbsolute.csv'
list_dataset = [df2016, df2017, df2018, df2019, df2020]

# Get Column Names and Drop Useless Attribute
attr = list(df.columns)
attr.remove('region')
attr.remove('total')

#
for i in attr:
  df2016[i] = round(df2016[i]/df2016['total'], 4)
for i in attr:
  df2017[i] = round(df2017[i]/df2017['total'], 4)
for i in attr:
  df2018[i] = round(df2018[i]/df2018['total'], 4)  
for i in attr:
  df2019[i] = round(df2019[i]/df2019['total'], 4)  
for i in attr:
  df2016[i] = round(df2020[i]/df2020['total'], 4)

# Iteration and Convertion Into Percentage (Within Canton)
for i in list_dataset:
  for j in attr:
    i[j] = round(i[j]/i['total'], 4)
for i in list_dataset:
  i['total'] = round(i['total']/i['total'], 4)
  
  
  for i in attr:
  df[i] = round(df[i]/df['total'], 4)
  
  
  
# Export Processed DataFrames
df2016.to_csv('/content/drive/MyDrive/Datasets/2016_popStructureCantonRelative.csv')
df2017.to_csv('/content/drive/MyDrive/Datasets/2017_popStructureCantonRelative.csv')
df2018.to_csv('/content/drive/MyDrive/Datasets/2018_popStructureCantonRelative.csv')
df2019.to_csv('/content/drive/MyDrive/Datasets/2019_popStructureCantonRelative.csv')
df2020.to_csv('/content/drive/MyDrive/Datasets/2020_popStructureCantonRelative.csv')
