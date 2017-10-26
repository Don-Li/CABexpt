# Functions for the log file

import os
import clock

def update_log( time, entry, directory = "/home/pi/Experiment/log.txt"):
    log_file = open( directory, "a" )
    log_message = "%s,%s\n" % (time, entry)
    log_file.write( log_message )
    log_file.close()

def make_new_log( directory = "/home/pi/Experiment/" ):
    log_file_name = "%slog.txt\n" % (directory)
    log_file = open( log_file_name, "w" )
    log_file.close()

def restart_log( directory = "/home/pi/Experiment/" ):
    log_directory = "%slog.txt\n" % (directory)
    
    date = clock.get_date_hmdmy()
    name_for_old_log = "%slog_ended_%s" % (directory, date)
    os.rename( log_directory, name_for_old_log )
    make_new_log()

