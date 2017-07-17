# Experiment details reader

import csv
import file_reader
import os
from glob import glob

def read_experiment():
	directory = "/home/pi/Experiment"
	files = os.chdir( directory )
	# .expt is the file extension for the experiment details
	expt_file = glob("%s/*.expt" % directory)
	file_path = directory + expt_file[0]
	return( file_reader.read_one_col_csv( file_path ) )
