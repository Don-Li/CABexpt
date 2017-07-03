# Dropbox uploader

import time
from log_file import update_logs
from subprocess import check_output

def dropbox_upload( remote_directory, file_path ):
    uploader_script = "dropbox_uploader upload"

    if not os.path.exists( file_path ):
        raise NameError( "File not found" )

    os_call = "%s %s %s" % (uploader_script, file_path, remote_directory )
    os_print = check_output( os_call, shell = True, universal_newlines = True )
    print( os_print )

    date = time.strftime( "%H_%M_%d_%m_%Y" )
    update_logs( date, os_print )


def upload_data( file_name ):
    local_directory = "/home/pi/Experiment/data"
    remote_directory = "/data"
    file_path = "%s%s" % ( local_directory, file_name )

    dropbox_upload( remote_directory, file_path )

def upload_log():
    local_directory = "/home/pi/Experiment/"
    remote_directory = "/log"
    file_path = "%s%s" % ( local_directory, "log.txt" )

    dropbox_upload( remote_directory, file_path )