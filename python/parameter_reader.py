import os
import csv
import numpy as np
import log_file

def load_params(subject, session, file_path):
    with open( file_path, "r") as file:
        csv_file = csv.reader( file, delimiter = "," )

        # First row is always a header
        header = csv_file.__next__()
        subject_column = header.index( subject )

        # Parameter dictionary: keys contain condition names, values contain lists of tuples
        parameters = {}
        # Repeats list
        repeats = []
        # List of condition names
        condition_names = []

        for row in csv_file:
            # "#" decorator in the csv to indicate blocks of parameters for conditions
            if row[0].startswith("#"):
                condition_name = row[0][1:]
                repeats.append( int( row[subject_column] ) )
                condition_names.append( condition_name )
                parameters[ condition_name ] = []
            else:
                parameters[ condition_name ].append((row[0],row[subject_column]))

    # Cumulative number of sessions for each repeat
    cum_repeats = np.cumsum( repeats )
    # Raise error if the session number is more than the sessions specified
    if session > cum_repeats[-1]:
        error_msg = "Session number larger than number of conditions"
        raise ValueError( error_msg )
        
    condition_now = np.where( cum_repeats >= session )[0][0]
    condition_now_name = condition_names[ condition_now ]
    parameters_now = parameters[ condition_now_name ]

    # Assign parameters to the global environment
    assignments = []
    for param in parameters_now:
        print( "%s = %s" % (param[0], param[1]) )
        globals()[param[0]] = float( param[1] )
        assignments.append( param )

    assignment_string = [str(assignments)]
    date = time.strftime( "%H_%M_%d_%m_%Y" )
    log_file.update_logs( date, assignment_string )
