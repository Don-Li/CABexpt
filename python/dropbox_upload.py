# Dropbox uploader

import os
import time
from log_file import update_logs
import subprocess

def dropbox_upload( remote_directory, file_path ):
    uploader_script = "dropbox_uploader upload"

    if not os.path.exists( file_path ):
        raise NameError( "Local directory not found" )
    os_call = "%s %s %s" % (uploader_script, file_path, remote_directory )
    print( os_call )
    os_print = subprocess.check_output( os_call, shell = True, universal_newlines = True )
    print( os_print )

    date = time.strftime( "%H_%M_%d_%m_%Y" )
    update_logs( date, os_print )


def data_upload( file_name ):
    uploader_script = "dropbox_uploader upload"
    local_directory = "/home/pi/Experiment/"
    remote_directory = "/data"
    
    os_call = "%s %s%s %s" % (uploader_script, local_directory, file_name, remote_directory )
    print( os_call )
    os_print = subprocess.check_output( os_call, shell = True, universal_newlines = True )
    print( os_print )

    date = time.strftime( "%H_%M_%d_%m_%Y" )
    update_logs( date, os_print )

def log_upload():
    uploader_script = "dropbox_uploader upload"
    local_directory = "/home/pi/Experiment/"
    remote_directory = "/log"

    os_call = "%s" % (uploader_script, local_directory, "log.txt", remote_directory)
    print( os_call )
    os_print = subprocess.check_output( os_call, shell = True, universal_newlines = True )
    print( os_print )

