# Functions for the log file

import os
import time

def update_log( time, entry ):
    log_file = open( "/home/pi/Experiment/log.txt", "a" )
    log_message = "%s,%s" % (time, entry)
    log_file.write( log_message )
    log_file.close()

def make_new_log():
    directory = "/home/pi/Experiment/"
    log_file_name = "%slog.txt" % (directory)
    log_file = open( log_file_name, "w" )
    log_file.close()

def restart_log():
    directory = "/home/pi/Experiment/"
    log_directory = "%slog.txt" % (directory)
    
    date = time.strftime( "%H_%M_%d_%m_%Y" )

    name_for_old_log = "%slog_ended_%s" % (directory, date)

    os.rename( log_directory, name_for_old_log )
    make_new_log()

