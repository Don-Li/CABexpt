import pigpio
import CAB_manager

class stimulus_operandum( object ):
    """Parent class for inputs and outputs"""

    def __init__( self, definition_dict, pigpio_pi ):
        self.name_to_number = definition_dict
        self.number_to_name = {item[1]:item[0] for item in self.name_to_number.items()}
        self.status = self.name_to_number.fromkeys( self.name_to_number.keys(), 0 )
        
        if type( pigpio_pi ) is CAB_manager.CABmanager:
            self.pigpio_pi = pigpio_pi.pi
        else:
            self.pigpio_pi = pigpio_pi

class stimulus( stimulus_operandum ):
    """Outputs"""

    def __init__( self, definition_dict, pigpio_pi ):
        stimulus_operandum.__init__( self, definition_dict, pigpio_pi )
        self.setup()

    def setup( self ):
        for key, value in self.name_to_number.items():
            self.pigpio_pi.set_mode( value, pigpio.OUTPUT )

    def on( self, stimuli ):
        for stimulus in stimuli:
            if not self.status[ stimulus ]:
                stimulus_number = self.name_to_number[stimulus]
                self.pigpio_pi.write( stimulus_number, pigpio.ON )
                self.status[ stimulus ] = pigpio.ON

    def off( self, stimuli ):
        for stimulus in stimuli:
            if self.status[ stimulus ]:
                stimulus_number = self.name_to_number[stimulus]
                self.pigpio_pi.write( stimulus_number, pigpio.OFF )
                self.status[ stimulus ] =  pigpio.OFF
    
    def on1( self, stimulus ):
        if not self.status[ stimulus ]:
            stimulus_number = self.name_to_number[stimulus]
            self.pigpio_pi.write( stimulus_number, pigpio.ON )
            self.status[ stimulus ] = pigpio.ON
    
    def off1( self, stimulus ):
        if not self.statis[ stimulus ]:
            stimulus_number = self.name_to_number[stimulus]
            self.pigpio_pi.write( stimulus_number, pigpio.OFF )
            self.status[ stimulus ] = pigpio.OFF

    def read( self, stimuli ):
        return( { stimulus: self.status[stimulus] for stimulus in stimuli } )
        
    def read1( self, stimulus ):
        return( self.status[stimulus] )

    def all_off( self ):
        stimuli = self.name_to_number.keys()
        self.off( stimuli )

    def all_on( self ):
        stimuli = self.name_to_number.keys()
        self.on( stimuli )

class operandum( stimulus_operandum ):
    """
    Inputs
    Slots:
        name_to_number: A dictionary that maps response labels to their GPIO number.
        number_to_name: The reverse dictionary of name_to_number.
        pigpio_pi: A pigpio.pi() class from the pigpio library.
        status: A dictionary showing which stimuli are active. Does nothing for inputs.
        bounce: A float giving the number of microseconds for bounce corrections.
    """

    def __init__( self, definition_dict, pigpio_pi, bounce, clock ):
        stimulus_operandum.__init__( self, definition_dict, pigpio_pi )
        self.bounce = bounce
        self.monitor = self.name_to_number.fromkeys( self.name_to_number.keys(), None )
        self.key_on = None
        self.clock = None
        self.setup()
        
    def setup( self ):
        for key, value in self.name_to_number.items():
            self.pigpio_pi.set_mode( value, pigpio.INPUT )
            self.pigpio_pi.set_glitch_filter( value, self.bounce )
            self.pigpio_pi.set_pull_up_down( value, pigpio.PUD_DOWN )
            self.monitor[ key ] = self.pigpio_pi.callback( user_gpio = value, edge = pigpio.RISING_EDGE, func = self.callback )

    def teardown( self ):
        for operandum in self.monitor:
            self.monitor[operandum].cancel()

    def key_reset( self ):
        self.key_on = None

    def callback( self, gpio, level, tick ):
        self.key_on = self.number_to_name[ gpio ]
        self.clock.assert_update( tick )

    def key_pressed( self ):
        return( self.key_on != None )

    def get_key( self ):
        return( self.key_on )


