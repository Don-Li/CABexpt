﻿from csv import reader
import numpy as np
import log_file
import clock

class parameter_manager(object):
    """
    Parameter manager
    A class for managing the parameter values for an experiment.
    Attributes:
        self.Conditions
            A list containing all the condition names in the parameter file.
        self.Parameters
            A list containing all the 
        self.Repeats
        self.Condition_now
        self.Condition_now_name
        self.Parameters_now
        self.Parameter_names
    """
    
    def __init__( self ):
        self.Conditions = []
        self.Parameters = []
        self.Repeats = []
        self.Condition_now = []
        self.Condition_now_name = []
        self.Parameters_now = []
        self.Parameter_names = []
        
    read_params = read_params
    set_param_now = set_param_now
    assign_params = assign_params

def read_params( subject, file_path ):
    with open( file_path, "r" ) as file:
        csv_file = reader( file, delimiter = "," )
    
        # First row is always a header
        header = csv_file.__next__()
        subject_column = header.index( subject )
    
        for row in csv_file:
        # "#" decorator in the csv to indicate blocks of parameters for each condition
            if row[0].startswith( "#" ):
                self.Conditions.append( row[0][1:] )
                self.Repeats.append( int( row(subject_columns) ) )
            else:
                self.Parameters.append( row[subject_column] )
                self.Parameter_names.append( row[0] )

def set_param_now():
    # Cumulative number of sessions for each repeat
    cum_repeats = np.cumsum( self.Repeats )
    # Raise error if the session number is more than the sessions specified
    if session > cum_repeats[-1]:
        error_msg = "Session number larger than number of conditions"
        raise ValueError( error_msg )
                
    self.Condition_now = np.where( cum_repeats >= session )[0][0]
    self.Condition_now_name = self.Conditions[ condition_now ]
    self.Parameters_now = self.Parameters[ condition_now_name ]            
                
def assign_params():

    # Assign parameters to the global environment
    assignments = []
    for param in range( 0, len( self.Parameters_now ) ):
        param_name = self.Parameter_names[param]
        param_value = self.Parameter[param]
        assignment_str = param_name + " = " + param_value
        print( assignment_str )
        globals()[param_name] = float( param_value )
        assignments.append( assignment_str )

    # Make a record in the log file
    date = clock.get_date_hmdmy()
    log_file.update_logs( date, assignments )
