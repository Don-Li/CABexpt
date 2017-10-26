# File reader

def read_one_col_csv( file_path ):
	with open( file_path, "r" ) as file:
		read_file = csv.reader( file, delimiter = "," )
		return_dict = { row[0].strip(" "): row[1].strip(" ") for row in read_file }
	return( return_dict )
    