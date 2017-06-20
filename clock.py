import time

class clock(object):
    """Clock"""

    def __init__( self ):
        self.start_time = time.time()
        self.time_now = 0

    def update( self ):
        self.time_now = time.time() - self.start_time
        return( self.time_now )

    def get_time( self ):
        return( self.time_now )

    def reset( self ):
        self.start_time = time.time()
        self.time_now = 0

    def sleep( self, seconds ):
        if seconds <= 0.5:
            t1 = time.time()
            while time.time() - t1 < seconds:
                pass
        else:
            t1 = time.time()
            time.sleep( seconds - 0.4 )
            while time.time() - t1 < seconds:
                pass
        return( self.update() )