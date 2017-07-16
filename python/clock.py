import time
import pigpio

class clock(object):
    """Clock"""

    def __init__( self, pi ):
        self.pi = pi
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

    def get_time( self ):
        return( self.time_now )

    def reset( self ):
        self.gpio_time_1 = self.get_current_tick()
        self.gpio_time_2 = 0
        self.time_now = 0

    def sleep( self, seconds ):
        if seconds <= 0.5:
            t1 = time.monotonic()
            while time.monotonic() - t1 < seconds:
                pass
        else:
            t1 = time.monotonic()
            time.sleep( seconds - 0.4 )
            while time.monotonic() - t1 < seconds:
                pass
        return( self.update() )

def get_date_dmy():
    """
    Return the date in dd.mm.yyyy format as a string.
    """
    return( time.strftime( "%d.%m.%Y" ) )

def get_date_hm():
    """
    Return the time in hh.mm format as a string.
    """
    return( time.strftime( "%H.%M" ) )

def get_date_hmdmy():
    """
    Return the time in hh_mm_dd_mm_yyy format as a string
    """
    return( time.strftime( "%H_%M_%d_%m_%Y" ) )