# Get the identity file
import csv

def read_identity():
	file_path = "/home/pi/Experiment/identity.txt"
	with open( file_path, "r") as file:
		identity_file = csv.reader( file, delimiter = "," )
		identity = { row[0].strip(" "): row[1].strip(" ") for row in reader }
	return( identity )

def get_subject_from_identity():
	identity = read_identity()
	return( identity["Subject"] )