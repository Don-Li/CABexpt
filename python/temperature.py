import os

read_temp = function():
    command = "/opt/vc/bin/vcgencmd measure_temp"
    temp = os.popen(command).readlines()
    return( temp )