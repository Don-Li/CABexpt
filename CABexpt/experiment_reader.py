# Experiment details reader

import csv
import file_reader
import os
import log_file
import clock
from glob import glob

def read_experiment( dirctory ):
    """
    Read a CSV file and return a dictionary of parameters
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

def read_experiment_params( file_name, subject, session ):
    """ Read a CSV file and return a dictionary of parameters """
    
    with open( file_name, mode = "r" ) as file:
        csv_file= csv.reader( file, delimiter = "," )
        
        # First row is always a header
        # Always has "subject" and "session"
        header = csv_file.__next__()
        try:
            subject_column = header.index( "subject" )
        except ValueError:
            msg = " 'subject' column not found"
            print( msg )
            log_file.update_log( time = clock.get_date_hmdmy(), entry = msg )
        try:
            session_column = header.index( "session" )
        except ValueError:
            msg = " 'session' column not found"
            print( msg )
            log_file.update_log( time = clock.get_date_hmdmy(), entry = msg )
        
        # Find columns for parameters
        parameter_cols = [ x for x in range( len(header) ) if x not in [subject_column, session_column] ]
        parameter_names = [ header[x] for x in parameter_cols ]
        
        parameter_dict = {}
        
        for row in csv_file:
            if row[ subject_column ] == subject and row[ session_column ] == session:
                parameter_dict[ "subject" ] = row[ subject_column ]
                parameter_dict[ "session" ] = row[ session_column ]
                for params in range( len(parameter_cols) ):
                    # Record log files
                    value = row[params]
                    parameter_name = parameter_names[params]
                    parameter_dict[ parameter_name ] = value
                    msg = " subject %s, session %s, parameter %s, value %s" % (subject, session, parameter_name, value )
                    log_file.update_log( time = clock.get_date_hmdmy(), entry = msg )
    
    return( parameter_dict )