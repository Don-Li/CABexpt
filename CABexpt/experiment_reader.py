# Experiment details reader

import csv
import file_reader
import os
import dropbox_download
from glob import glob

def read_experiment( dirctory ):
    """
    Return a dictionary
    """
    files = os.chdir( directory )
    # .expt is the file extension for the experiment details
    expt_file = glob("%s/*.expt" % directory)
    file_path = directory + expt_file[0]
    return( file_reader.read_one_col_csv( file_path ) )

def clone_experiment_folder( directory ):
    original_wd = os.getcwd()
    file_names = os.chdir( directory )
    for file in file_names:
        file_to_download = "/experiment" + file_names[file]
        dropbox_download.dropbox_download( file_to_download, "/home/pi/Experiment" )
    os.chdir( original_wd )