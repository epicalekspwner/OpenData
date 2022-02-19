# scriptGenderGuesser
# scripts/genderGuesser/

# Install Requiered Library
!pip install unidecode -q

# Import Requiered Libraries
import numpy as np
import pandas as pd
import unidecode as udc

# Import Database
nameGenderDatabase = pd.read_csv('https://raw.githubusercontent.com/epicalekspwner/OpenDataCustomerAnalytics/main/scripts/genderGuesser/namesGenderDatabase.csv')

# Function Definition:
def genderGuesser(customerName):
  try:
    indice = name_gender[name_gender['NAME'] == unidecode.unidecode(customerName.upper())]['TREND'].item()
    if indice > 0:
      return 'female'
    if indice == 0:
      return 'unknown'
    else:
      return 'male'
  except ValueError:
    return 'NaN'