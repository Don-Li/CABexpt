# Dropbox downloader

import time
from log_file import update_logs
from subprocess import check_output


def dropbox_download( remote_file_path, local_directory ):
    uploader_script = "dropbox_uploader download"
    
    if not os.path.exists( local_directory ):
        raise NameError( "Local directory not found" )

    os_call = "%s %s %s" % (uploader_script, remote_file_directory, local_directory)
    os_print = check_output( os_call, shell = True, universal_newlines = True )
    print( os_print )

    os.system( os_call )
def param_download( param_file ):
    local_directory = "/home/pi/Experiment"
    remote_directory = ""
    file_path = "%s%s" % ( remote_directory, param_file )

    dropbox_download( remote_file_path, local_directory )
