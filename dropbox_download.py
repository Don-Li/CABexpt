import os



def dropbox_download( remote_file_directory, local_directory ):

    uploader_script = "dropbox_uploader download"


    if not os.path.exists( local_directory ):

        raise NameError( "Local directory not found" )


    os_call = "%s %s %s" % (uploader_script, remote_file_directory, local_directory)

    print( os_call )

    os.system( os_call )

    print( "File downloaded" )
