import time
import identity
import parameter_reader
import experiment_reader
import input_outputs as io
import os
import pigpio
import clock

class CABmanager(object):
    """CAB manager"""
    
    def __init__( self, subject_name ):
        
        expt_local_directory = "/home/pi/Experiment"
        
        os.system( "sudo pigpiod" )
        
        # Get the subject name
        self.subject_name = subject_name
        
        # Download files in the "experiment" remote directory
        experiment_reader.clone_experiment_folder( expt_local_directory )
        # Get details from the *.expt file
        experiment_details = experiment_reader.read_experment( expt_local_directory )
        self.experiment_file_name = experiment_details[ "Experiment" ]
        self.parameter_file_name = experiment_details[ "Parameters" ]
        parameter_file_directory = expt_local_directory + "/" + self.parameter_file_name

        self.parameters = parameter_reader.parameter_manager()
        self.parameters.read_params( self.subject_name, parameter_file_directory )
        self.parameters.set_param_now()
        # Log file is updated with assignments
        self.parameters.assign_params()
        
        self.stimulus = None
        self.operandum = None
        self.event_record = None
        
        # Make the pigpio.pi object
        self.pi = pigpio.pi()
        # Set up a clock slot
        self.clock = None
        
    def setup_stimuli( self, definition_dict ):
        self.stimulus = io.stimulus( definition_dict, self.pi )
        return( self.stimulus )

    def setup_opernada( self, definition_dict ):
        self.operandum = io.operandum( definition_dict, 
                                      self.pi, 
                                      bounce = 1000, 
                                      PUD = pigpio.PUD_DOWN,
                                      clock = self.clock )
        return( self.operandum )

    def setup_clock( self ):
        self.clock = clock.__init__( self.pi )
        if self.operandum.clock == None:
            self.operandum.clock = self.clock
        return( self.clock )

def get_subject_name():
    return( identity.read_identity["Subject"] )

