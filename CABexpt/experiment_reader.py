# Experiment details reader

import csv
import file_reader
import os
import log_file
from clock import get_date_hmdmy
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

def read_experiment_params( subject, session, file_name, directory ):
    """ Read a CSV file and return a dictionary of parameters """
    
    session = str(session)
    msg = " subject %s, session %s, reading %s" % (subject, session, file_name)
    log_file.update_log( time = get_date_hmdmy(), entry = msg, directory = directory )
    
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
            log_file.update_log( time = get_date_hmdmy(), entry = msg, directory = directory )
            return( None )
        try:
            session_column = header.index( "session" )
        except ValueError:
            msg = " 'session' column not found"
            print( msg )
            log_file.update_log( time = get_date_hmdmy(), entry = msg, directory = directory )
            return( None )
        
        # Find columns for parameters
        parameter_cols = [ x for x in range( len(header) ) if x not in [subject_column, session_column] ]
        
        parameter_dict = {}
        got_subject_session = False
        
        for row in csv_file:
            if row[ subject_column ] == subject and row[ session_column ] == session:
                parameter_dict[ "subject" ] = row[ subject_column ]
                parameter_dict[ "session" ] = int( row[ session_column ] )
                for col in parameter_cols:
                    # Record log files
                    value = row[col]
                    parameter_name = header[col]
                    parameter_dict[ parameter_name ] = value
                    msg = " subject %s, session %s, %s := %s" % (subject, session, parameter_name, value )
                    log_file.update_log( time = get_date_hmdmy(), entry = msg, directory = directory )
                got_subject_session = True
                
        if not got_subject_session:
            msg = " failed to find subject %s, session %s" % (subject, session)
            log_file.update_log( time = get_date_hmdmy(), entry = msg, directory = directory )
    
    return( parameter_dict )

def read_session_info( subject, file_name, directory ):
    """ Read session information """
    
    with open( file_name, mode = "r" ) as file:
        csv_file = csv.reader( file, delimiter = "," )
        
        # First row is always a header
        # Always has "subject" and "session"
        header = csv_file.__next__()
        
        # Try to read subject and session
        try:
            subject_column = header.index( "subject" )
        except ValueError:
            msg = " 'subject' column not found"
            print( msg )
            log_file.update_log( time = get_date_hmdmy(), entry = msg, directory = directory )
            return( None )
        try:
            session_column = header.index( "session" )
        except ValueError:
            msg = " 'session' column not found"
            print( msg )
            log_file.update_log( time = get_date_hmdmy(), entry = msg, directory = directory )
            return( None )
        
        got_session = False
        
        for row in csv_file:
            if row[ subject_column ] == subject:
                session = row[ session_column ]
                msg = " from %s found session %s" % (file_name, session)
                log_file.update_log( time = get_date_hmdmy(), entry = msg, directory = directory )
                got_session = True

        if not got_session:
            msg = " failed to find session in %s" % (file_name)
            log_file.update_log( time = get_date_hmdmy(), entry = msg, directory = directory )
            return( None )
    
    return( session )