import glob
import os
import sys
import urllib.request

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

# name of dataset. This will be the final name of the file that will be generated
dataset_name = 'soc_001_ea_population'

logger.info('Executing script for dataset: ' + dataset_name)
# create a new sub-directory within your specified dir called 'data'
# within this directory, create files to store raw and processed data
data_dir = util_files.prep_dirs(dataset_name)

'''
Download data for each country and save to data directory
'''

# the base url used to download the data from the source website
base_url = "https://data.worldpop.org/GIS/Population/Global_2000_2020_Constrained/2020/maxar_v1"

# country specific url endpoints
countries_url = {
    "burundi": "BDI/bdi_ppp_2020_constrained.tif",
    "djibouti": "DJI/dji_ppp_2020_constrained.tif",
    "ethiopia": "ETH/eth_ppp_2020_constrained.tif",
    "eritrea": "ERI/eri_ppp_2020_constrained.tif",
    "kenya": "KEN/ken_ppp_2020_constrained.tif",
    "rwanda": "RWA/rwa_ppp_2020_constrained.tif",
    "somalia": "SOM/som_ppp_2020_constrained.tif",
    "south_sudan": "SSD/ssd_ppp_2020_constrained.tif",
    "sudan": "SDN/sdn_ppp_2020_constrained.tif",
    "tanzania": "TZA/tza_ppp_2020_constrained.tif",
    "uganda": "UGA/uga_ppp_2020_constrained.tif"
}
# download the data from the source for each country
for country, country_url in countries_url.items():
    logger.info('Downloading data for country: ' + country)
    url = f"{base_url}/{country_url}"
    raw_data_file = os.path.join(data_dir, f"{country}.tif")
    urllib.request.urlretrieve(url, raw_data_file)

'''
Process data
'''

logger.info("Merging all the country files to one file using gdal_merge.py")
# the path to the unprocessed data files
tifs = glob.glob(os.path.abspath(os.path.join(data_dir, '*.tif')))

# merge tifs to one single file
merged = os.path.abspath(os.path.join(data_dir, f'{dataset_name}.tif'))

util_files.merge_geotiffs(tifs, merged, nodata=-9999)

logger.info("Merging Complete")
