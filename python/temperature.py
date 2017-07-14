from subprocess import check_output

read_temp = function():
    
    """
    Description:
        Make a command line call to read the temperature.
    Value:
        Returns a character string.
    """
    
    command = "/opt/vc/bin/vcgencmd measure_temp"
    temp = check_output( command, shell = True, universal_newlines = True )
    temp = temp.strip( "\n" )
    return( temp )
