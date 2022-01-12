# Connect Google Drive to Colab
from google.colab import drive
drive.mount('/content/drive')

# Import Pandas Library
import pandas as pd

# Import and Load Data Into DataFrames
df2016 = pd.read_csv('https://raw.githubusercontent.com/epicalekspwner/OpenDataCustomerAnalytics/main/popHousehold/2016_popHouseholdAbsolute.csv')
df2017 = pd.read_csv('https://raw.githubusercontent.com/epicalekspwner/OpenDataCustomerAnalytics/main/popHousehold/2017_popHouseholdAbsolute.csv')
df2018 = pd.read_csv('https://raw.githubusercontent.com/epicalekspwner/OpenDataCustomerAnalytics/main/popHousehold/2018_popHouseholdAbsolute.csv')
df2019 = pd.read_csv('https://raw.githubusercontent.com/epicalekspwner/OpenDataCustomerAnalytics/main/popHousehold/2019_popHouseholdAbsolute.csv')
df2020 = pd.read_csv('https://raw.githubusercontent.com/epicalekspwner/OpenDataCustomerAnalytics/main/popHousehold/2020_popHouseholdAbsolute.csv')
list_dataset = [df2016, df2017, df2018, df2019, df2020]

# Get Column Names and Drop Useless Attribute
attr = list(df2016.columns)
attr.remove('region')
attr.remove('total')
attr.remove('averageSizeHousehold')

# Iteration and Convertion Into Percentage (Within Canton)
for i in list_dataset:
  for j in attr:
    i[j] = round(i[j]/i['total'], 4)
for i in list_dataset:
  i['total'] = round(i['total']/i['total'], 4)
  
# Export Processed DataFrames
df2016.to_csv('/content/drive/MyDrive/Datasets/2016_popHouseholdCantonRelative.csv')
df2017.to_csv('/content/drive/MyDrive/Datasets/2017_popHouseholdCantonRelative.csv')
df2018.to_csv('/content/drive/MyDrive/Datasets/2018_popHouseholdCantonRelative.csv')
df2019.to_csv('/content/drive/MyDrive/Datasets/2019_popHouseholdCantonRelative.csv')
df2020.to_csv('/content/drive/MyDrive/Datasets/2020_popHouseholdCantonRelative.csv')
