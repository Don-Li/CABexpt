import experiment_reader
from os import chdir, system
import pigpio
from clock import get_date_hmdmy
import log_file
from time import sleep

class CABmanager(object):
    """CAB manager"""
    
    def __init__( self, 
                 subject, 
                 parameter_file,
                 session = None,
                 session_info_file = None,
                 directory = "/home/pi/Experiment",
                 windows_test = False):
        
        chdir( directory )
        self.directory = directory
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
            msg = " start pigpiod"
            log_file.update_log( get_date_hmdmy(), msg, directory )
            system( "sudo pigpiod" )
            sleep( 0.1 )
            
            msg = " make pigpio.pi"
            log_file.update_log( get_date_hmdmy(), msg, directory )
            # Make the pigpio.pi object
            self.pi = pigpio.pi()
        
        self.subject = subject
        # Log files are updated inside read_experiment_params()
        self.parameters = experiment_reader.read_experiment_params( subject, session, parameter_file, directory )
        
        # Slots
        # self.directory
        # self.session
        # self.pi
        # self.subject
        # self.parameters
    
    def teardown( self ):
        msg = "stop pigpio.pi"
        log_file.update_log( get_date_hmdmy(), msg, self.directory )
        self.pi.stop()
        
        msg = "stop pigpiod"
        system( "sudo killall pigpiod" )
        log_file.update_log( get_date_hmdmy(), msg, self.directory )
        
        msg = " stop experiment, subject %s, session %s" % ( self.subject, self.session )
        log_file.update_log( get_date_hmdmy(), msg, self.directory )
        