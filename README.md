# East Africa Hazards Watch Dataset Pre-processing

#### Purpose

This Github repository documents the pre-processing done to the datasets displayed
on [East Africa Hazards Watch](https://eahazardswatch.icpac.net).

#### File Structure

The processing done to each dataset should be stored in a single file, named with the EAHW ID and public title used on
EA Hazards Watch. This folder should **always** include a README.md file that describes the processing that was done. A
template for this file can be found in this repository with the name README_template.md. If a script (preferably Python)
was used to process the dataset, that code should also be included as a separate file. The general structure can be
summarized as follows:

```
Repository
|
|- Dataset 1 folder = {eahw_id}_{public_title}
| |-{eahw_id}_{public_title}_processing.py # optional, script used to process the dataset
| |-README.md # file describing the processing
| +-...
|
|-Dataset 2 folder
| +-...
|
+-...
```

#### Contents of README.md

If the pre-processing was done in Excel, and functions used should be clearly described.For datasets that were processed
in Google Earth Engine (GEE), a link to the GEE script should be included, AND the code should be included in the
README.md file as a code snippet for users who do not have access to Google Earth Engine.

If the pre-processing was done using a script that has been uploaded to Github, the readme should still be included and
describe the general steps that were taken - which datasets were used, how were they modified, etc.

#### Contents of script, if included

If a script was used to process the dataset, the code should be uploaded to this Github. This code should be thoroughly
commented so that readers unfamiliar with the coding language can still follow the process.

All codes should be written using open-source tools and programming languages. Tools and modules that require a
subscription should be avoided (e.g., ArcGIS).


