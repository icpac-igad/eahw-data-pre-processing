## East Africa ACLED Conflict Data

This file describes the data pre-processing that was done
to [ACLED Conflict data](https://acleddata.com/data-export-tool/)
for [display on EA Hazards Watch]({link to dataset's metadata page on EA Hazards Watch}).

The source provided a metered data export tool
at [https://acleddata.com/data-export-tool/](https://acleddata.com/data-export-tool/), that requires an API key obtained
by creating an account. The export tool allows to download country data going back up to 3 years. Using this tool, the
data was exported as CSV from `2018-09-03` to `2021-09-07` for the below East Africa Countries:

- Burundi
- Djibouti
- Ethiopia
- Eritrea
- Kenya
- Rwanda
- Somalia
- South Sudan
- Sudan
- Tanzania
- Uganda

The exported `csv`file was saved to a file
named `2018-09-03-2021-09-07-Burundi-Djibouti-Eritrea-Ethiopia-Kenya-Rwanda-Somalia-South_Sudan-Sudan-Tanzania-Uganda.csv`
Please note this file is not included in the repo. You will have to download it and change the file accordingly in the
script.

The CSV file was then converted to a `Geojson` using Geopandas.

Please see
the [Python script](https://github.com/icpac-igad/eahw-data-pre-processing/blob/main/acled_confict_data/acled_conflict_data.py)
for more details on this processing.

You can view the processed  East Africa ACLED Conflict Data
dataset [on EA Hazards Watch]({link to dataset's metadata page on Hazards Watch}).

You can also download the original dataset [from the source website](https://acleddata.com/data-export-tool/).

###### Note: This dataset processing was done by [Erick Otenyo](mailto:erick.otenyo@igad.int).