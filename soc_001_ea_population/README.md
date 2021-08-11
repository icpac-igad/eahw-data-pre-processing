## East Africa Population (Grid, 100m) Dataset Pre-processing

This file describes the data pre-processing that was done
to [Population Count - Constrained Individual Countries](https://www.worldpop.org/geodata/listing?id=78)
for [display on EA Hazards Watch]({link to dataset's metadata page on EA Hazards Watch}).

The source provided the data as individual downloadable tiff files for each country. The files were downloaded for the
East Africa Countries listed below, and then joined merger using the GDAL merge tool.

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

Please see
the [Python script](https://github.com/icpac-igad/eahw-data-pre-processing/blob/main/soc_001_ea_population/soc_001_ea_population_processing.py)
for more details on this processing.

You can view the processed {EA Hazards Watch public title}
dataset [on EA Hazards Watch]({link to dataset's metadata page on Hazards Watch}).

You can also download the original dataset [from the source website](https://www.worldpop.org/geodata/listing?id=78).

###### Note: This dataset processing was done by [Erick Otenyo](mailto:erick.otenyo@igad.int), and QC'd by [Abubakr Babiker](mailto:Abubakr.Babiker@igad.int).