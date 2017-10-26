# Get the identity file
import csv
import file_reader

def read_identity():
    """
    Read the identity file.
    the identity file is *.identity, where * denotes the subject name.
    The *identity is a csv file.
    Variable names are down the first column
        Variables: Subject, Experiment_name, Session_number
    
    Returns a dictionary
    """
    
	file_path = "/home/pi/Experiment/identity.txt"
	return( file_reader.read_one_col_csv( file_path ) )