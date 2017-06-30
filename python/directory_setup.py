# Set up directories


import os

import csv



def setup_directory():

    # Always use this directory

    directory = "/home/pigeonpi/experiment/"

    os.chdir( directory )


    # Read the "identity.txt" file
    
    # "identity.txt" will contain the subject name, experiment name, and whether setup has already been done.
    
    with open( "identity.txt", "r" ) as file:

        reader = csv.reader(file, delimiter = ",")

        identity = { row[0].strip(" "): row[1].strip(" ") for row in reader }



    # Always use these folders

    folders = ["parameters","data","secret"]


    # Look through the folders and make them if they do not already exist.

    # Throw an error if a folder already exists.

    if identity["setup"] == "False":

        for folder in folders:

            if os.path.exists( folder ):

                raise NameError( "Attempting setup but %s already exists" % folder )

            else:

                print( "Constructing '%s' folder" % folder )

                os.makedirs(folder)


    # Set identity to True in "identity.txt"

    identity[ "setup" ] = "True"


    # Write "identity.txt"

    with open( "identity.txt", "w" ) as file:

        writer = csv.writer( file )

        writer.writerows( identity.items() )
