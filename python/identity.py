# Get the identity file
import csv
import file_reader

def read_identity():
    """
    Returns a dictionary
    """
    
	file_path = "/home/pi/Experiment/identity.txt"
	return( file_reader.read_one_col_csv( file_path ) )