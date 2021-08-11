import os
import sys

import dotenv

dotenv.load_dotenv(os.getenv('EAHW_ENV'))

import subprocess
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def prep_dirs(dataset_name):
    '''
    Sets working directory for processing dataset, and creates needed directories as necessary
    INPUT   dataset_name: full name of dataset to be processed
    RETURN  data_dir: relative path of directory for holding downloaded and processed data
    '''
    # first, set the directory that you are working in with the path variable
    path = os.path.abspath(os.path.join(os.getenv('PROCESSING_DIR'), dataset_name))

    if not os.path.exists(path):
        os.mkdir(path)
    # move to this directory
    os.chdir(path)
    logger.debug('Working directory absolute path: ' + path)

    # create a new sub-directory within your specified dir called 'data'
    # within this directory, create files to store raw and processed data
    data_dir = 'data'
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)
    return data_dir


def convert_geotiff_to_nc(tif):
    '''
    Convert single-band geotiff file to netcdf
    INPUT   tif: file name of geotiff to convert (string)
    RETURN  nc: file name of generated netcdf (string)
    '''

    # generate a name to save the nc file we will translate the geotiff file into
    nc = '{}.nc'.format(os.path.splitext(tif)[0])
    # translate the geotiff file into a netcdf file
    cmd = ['gdal_translate', '-of', 'NetCDF', tif, nc]
    completed_process = subprocess.run(cmd, shell=False)
    logger.debug(str(completed_process))
    if completed_process.returncode != 0:
        raise Exception('Geotiff conversion to NetCDF using gdal_translate failed! Command: ' + str(cmd))

    return nc


def merge_netcdfs(ncs, output_file):
    '''
    Merge input single-variable netcdf into one single netcdf.

    INPUT   ncs: file names of all single-band netcdfs to merge (list of strings)
            output_file: output file
    RETURN  output_file: file name of combined netcdf (string)
    '''
    # merge all the ncs
    cmd = ['ncrcat', ' '.join(ncs), output_file]
    completed_process = subprocess.run(cmd, shell=False)
    logger.debug(str(completed_process))
    if completed_process.returncode != 0:
        raise Exception('Merging of Netcdfs using ncrcat failed! Command: ' + str(cmd))
    return output_file


def merge_geotiffs(tifs, multitif, ot=None, nodata=None):
    '''
    Merge input single-band geotiffs into one multi-band geotiff. This is a "dumb" merge; for example,
    it destroys all band metadata.
    INPUT   tifs: file names of all single-band geotiffs to merge (list of strings)
            multitif: file name of resulting, multi-band geotiff
    '''
    # merge all the sub tifs from this netcdf to create an overall tif representing all variable
    merge_path = os.path.abspath(os.path.join(os.getenv('GDAL_DIR'), 'gdal_merge.py'))
    cmd = '{} "{}" '
    if ot is not None:
        cmd += '-ot {} '.format(ot)
    if nodata is not None:
        cmd += '-a_nodata {} '.format(nodata)
    cmd += '-n -9999 -o {} {}'
    cmd = cmd.format(sys.executable, merge_path, multitif, ' '.join(tifs), )
    completed_process = subprocess.run(cmd, shell=True)
    logger.debug(str(completed_process))
    if completed_process.returncode != 0:
        raise Exception('Merging of GeoTiffs using gdal_merge.py failed! Command: ' + str(cmd))
    return
