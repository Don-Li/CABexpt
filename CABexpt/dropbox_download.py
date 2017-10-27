# Dropbox downloader

import time
from log_file import update_log
from subprocess import check_output
import clock


def dropbox_download( remote_file_path, local_directory ):
    uploader_script = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh download"
    
    if not os.path.exists( local_directory ):
        error_message = "Cannot download " + remote_file_path
        date = clock.get_date_hm()
        log_file.update_logs( date, error_message )
        raise NameError( "Local directory not found" )

    os_call = "%s %s %s" % (uploader_script, remote_file_directory, local_directory)
    os_print = check_output( os_call, shell = True, universal_newlines = True )
    print( os_print )

    os.system( os_call )