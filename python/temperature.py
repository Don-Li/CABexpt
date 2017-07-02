from subprocess import check_output

read_temp = function():
    command = "/opt/vc/bin/vcgencmd measure_temp"
    temp = check_output( command, shell = True, universal_newlines = True )
    temp = temp.strip( "\n" )
    return( temp )