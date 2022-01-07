# Open Data for Customer Analytics

## Scripts

### Convert Absolute Numbers Into Percentages (Within Country)

```
# Import Module/Dataset and Load It Into a DataFrame
import pandas as pd
df = pd.read_csv('/path', sep=';')

# Get Column Names and Drop Useless Attribute
attr = list(df.columns)
attr.remove('region')

# Iteration and Convertion Into Percentage
for i in attr:
  df[i]= df[i]/df[i][26]
  
# Export DataFrame
df.to_csv('/path')
```

## Datasets

### popStructure

**Files**
- [2020_popStructureAbsolute.csv](https://github.com/epicalekspwner/OpenData/blob/main/popStructure/2020_popStructureAbsolute.csv): absolute numbers of people per canton
- [2020_popStructureCantonRelative.csv](https://github.com/epicalekspwner/OpenData/blob/main/popStructure/2020_popStructureCantonRelative.csv): relative numbers of people (percentages) within the canton
- [2020_popStructureCountryRelative.csv](https://github.com/epicalekspwner/OpenData/blob/main/popStructure/2020_popStructureCountryRelative.csv): relative numbers of people (percentages) within the country

**Metadata**
- **Title**: Structure of the permanent resident population by canton, 2010-2020
- **Identifer**: je-e-01.02.03.04
- **Publishing Date**: 01.09.2021
- **Format**: XLSX
- **Size**: 89 kB
- **Publisher**: Federal Statistical Office
- **Access URL**: https://www.bfs.admin.ch/bfs/en/home/statistics/catalogues-databases.assetdetail.18344223.html

**Attributes**
- **Total**
  - ```total```
- **Age** 
  - ```age0_19``` 
  - ```age20_64``` 
  - ```age65+```
- **Sex** 
  - ```sexMale``` 
  - ```sexFemale``` 
- **Citizenship**
  - ```citizenSwiss``` 
   - ```citizenForeign``` 
- **Marital Status**
  - ```maritalSingle``` 
  - ```maritalMarried``` 
  - ```maritalWidowed``` 
  - ```maritalDivorced``` 
  - ```maritalUnmarried``` 
  - ```martialRegistredPartnership``` 
  - ```maritalDisolvedPartnership```
- **Typology: Area with Urban Character** 
  - ```typoUrbanCore``` 
  - ```typoUrbanCoreInfluence``` 
  - ```typoNoUrbanCoreInfluence``` 
