from time import strftime, monotonic
import pigpio
import CABmanager

class clock(object):
    """Clock"""

    def __init__( self, pigpio_pi ):
    
        if type( pigpio_pi ) is CAB_manager.CABmanager:
            self.pigpio_pi = pigpio_pi.pi
        else:
            self.pigpio_pi = pigpio_pi
    
        self.tickDiff = pigpio.tickDiff
        self.get_current_tick = pi.get_current_tick
        self.gpio_time_1 = self.get_current_tick()
        self.gpio_time_2 = 0
        self.time_now = 0

    def update( self ):
        self.gpio_time_2 = self.get_current_tick()
        self.time_now += self.tickDiff( self.gpio_time_1, self.gpio_time_2 )/1000000.0
        self.gpio_time_1 = self.gpio_time_2
        return( self.time_now )
        
    def assert_update( self, gpio_time_2 ):
        self.gpio_time_2 = gpio_time_2
        self.time_now += self.tickDiff( self.gpio_time_1, self.gpio_time_2 )/1000000.0
        self.gpio_time_1 = self.gpio_time_2
        return( self.time_now )

    def get_time( self ):
        return( self.time_now )

    def reset( self ):
        self.gpio_time_1 = self.get_current_tick()
        self.gpio_time_2 = 0
        self.time_now = 0

    def sleep( self, seconds ):
        if seconds <= 0.5:
            t1 = monotonic()
            while monotonic() - t1 < seconds:
                pass
        else:
            t1 = monotonic()
            sleep( seconds - 0.4 )
            while monotonic() - t1 < seconds:
                pass
        return( self.update() )

def get_date_dmy():
    """
    Return the date in dd.mm.yyyy format as a string.
    """
    return( strftime( "%d.%m.%Y" ) )

def get_date_hm():
    """
    Return the time in hh.mm format as a string.
    """
    return( strftime( "%H.%M" ) )

def get_date_hmdmy():
    """
    Return the time in hh_mm_dd_mm_yyy format as a string
    """
    return( strftime( "%H_%M_%d_%m_%Y" ) )