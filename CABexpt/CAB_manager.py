import experiment_reader
import os
import pigpio
from clock import get_date_hmdmy
import log_file

class CABmanager(object):
    """CAB manager"""
    
    def __init__( self, 
                 subject, 
                 parameter_file,
                 session = None,
                 session_info_file = None,
                 directory = "/home/pi/Experiment",
                 windows_test = False):
        
        os.chdir( directory )
        msg = " start experiment, subject %s, session %s" % ( subject, session )
        log_file.update_log( get_date_hmdmy(), msg, directory )
        
        if ( session_info_file != None ):
            # Logs are updated inside
            session = experiment_reader.read_session_info( subject, session_info_file, directory )
        elif ( session != None ):
            msg = " from args set session %s" % (session)
            log_file.update_log( get_date_hmdmy(), msg, directory )
        self.session = session
        
        if ( not windows_test ):
            msg = "start pigpiod"
            log_file.update_log( get_date_hmdmy(), msg, directory )
            os.system( "sudo pigpiod" )
            # Make the pigpio.pi object
            self.pi = pigpio.pi()
        
        self.subject = subject
        # Log files are updated inside read_experiment_params()
        self.parameters = experiment_reader.read_experiment_params( subject, session, parameter_file, directory )