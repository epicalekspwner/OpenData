## geographicsGeometry/ZIP: Files, Metadata & Attributes

### **Files**
- ```zipLocalities.csv```: Dataset of localities associated with their FSO-ids, postal codes, communes and cantons 

### Metadata

#### Open Data Domain
- **Domain Name**: Official Geographical Directories
- **Purpose of Use**: n/a

#### Dataset
- **Title**: Répertoire officiel des localités
- **Identifier**: PLZO_CSV_LV95
- **Publishing Date**: 2022-02-01
- **Periodicity**: n/a
- **Language**: DE
- **Format**: CSV
- **Size**: 308 Ko

#### Dataset Attributes
- **Names**: See below
- **Values**:
  - Locality: Textual
  - ZIP: Numerical
  - Additional digit: 
  - FSO number: Numerical
  - Canton: Textual
  - E: Numerical
  - N: Numerical
  - Language: Textual
- **Types**:
  - Locality: String
  - ZIP: Discrete
  - Additional digit: Discrete
  - FSO number: Discrete
  - Canton: String
  - E: Continuous
  - N: Continuous
  - Language: String
- **Units**:
  - Locality: n/a
  - ZIP: n/a
  - Additional digit: n/a 
  - FSO number: n/a 
  - Canton: n/a
  - E: n/a
  - N: n/a
  - Language: n/a

#### Level of Detail
- **Spatial Coverage**: Switzerland
- **Temporal Coverage**: n/a
- **Spacial Granularity**: Locality
- **Temporal Granularity**: n/a

#### License
- **License Name**: OPEN-BY
- **License URL**: https://data.geo.admin.ch/ch.swisstopo-vd.ortschaftenverzeichnis_plz/
- **Permissions**: Open use. Must provide the source.
- **Jurisdiction**: Switzerland

#### Version
- **Date of Publication**: 2022-02-01
- **Date of Modification**: 2022-02-01

#### Organization
- **Original Data Source**: Federal Office of Topography swisstopo; Cantons; La Poste
- **Publisher**: Géodésie et Direction fédérale des mensurations cadastrales, Mensuration officielle et cadastre RDPPF
- **Managed By**: Géodésie et Direction fédérale des mensurations cadastrales, Mensuration officielle et cadastre RDPPF
- **Contact Point**: https://www.cadastre.ch/fr/services/service/registry/plz.html#tabs_0

#### Distribution
- **Access URL**: https://www.cadastre.ch/fr/services/service/registry/plz.html
- **Download URL**: https://data.geo.admin.ch/ch.swisstopo-vd.ortschaftenverzeichnis_plz/PLZO_CSV_LV95.zip


### Attributes
- ```locality```: Official name of the locality
- ```zip```: Four-digit postal code (ZIP)
- ```additionalDigit```: Additional digits providing ZIP6 when combined with the the PLZ attribute
- ```commune```: Name of the main commune of the locality (not to be used as an identifier)
- ```numberFSO```: Number of the main commune of the locality (not to be used as an identifier)
- ```canton```: Abbreviation of the canton in which the locality is predominantly located
- ```e```: East coordinate indicating the position of any point within the perimeter of the locality or postcode
- ```n```: North coordinate indicating the position of any point within the perimeter of the locality or postcode
- ```language```: Abbreviation of the locality official language
