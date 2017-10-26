# Set up directories

import os
import csv
import identity

def setup_directory():

    # Always use this directory
    directory = "/home/pi/experiment/"
    os.chdir( directory )

    # Read the "identity.txt" file    
    # "identity.txt" will contain the subject name, experiment name, and whether setup has already been done.    
    identity = identity.read_identity()

    # Always use these folders
    folders = ["data","log"]

    # Look through the folders and make them if they do not already exist.
    # Throw an error if a folder already exists.

    if identity["setup"] == "False":
        for folder in folders:
            if os.path.exists( folder ):
                raise NameError( "Attempting setup but %s already exists" % folder )
            else:
                print( "Constructing '%s' folder" % ( folder ) )
                os.makedirs(folder)

    # Set identity to True in "identity.txt"
    identity[ "setup" ] = "True"

    # Write "identity.txt"
    with open( "identity.txt", "w" ) as file:
        writer = csv.writer( file )
        writer.writerows( identity.items() )
