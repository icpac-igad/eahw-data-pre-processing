import os
import sys

import pandas as pd
import geopandas as gpd

utils_path = os.path.join(os.path.abspath(os.getenv('PROCESSING_DIR')), 'utils')

if utils_path not in sys.path:
    sys.path.append(utils_path)
import util_files
import logging

# Set up logging
# Get the top-level logger object
logger = logging.getLogger()

for handler in logger.handlers:
    logger.removeHandler(handler)

logger.setLevel(logging.INFO)
# make it print to the console.
console = logging.StreamHandler()
logger.addHandler(console)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

dataset_name = 'acled_conflict_data'

logger.info('Executing script for dataset: ' + dataset_name)

# create a new sub-directory within your specified dir called 'data'
# within this directory, create files to store raw and processed data
data_dir = util_files.prep_dirs(dataset_name)

# Read CSV to dataframe
logger.info("Reading CSV file")
df = pd.read_csv(
    f"{data_dir}/2018-09-03-2021-09-07-Burundi-Djibouti-Eritrea-Ethiopia-Kenya-Rwanda-Somalia-South_Sudan-Sudan-Tanzania-Uganda.csv")

# convert  to geodataframe
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude))

# set crs
gdf = gdf.set_crs(4326, allow_override=True)

# save as geojson file
logger.info("Saving as Geojson")
gdf.to_file(f"{data_dir}/{dataset_name}.geojson", driver='GeoJSON')

logger.info("Saving Complete..")
