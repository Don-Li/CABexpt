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