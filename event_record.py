import time
import numpy as np
import csv
import os

class event_record(object):
	"""This is an event record"""

	def __init__( self, subject, experiment_name ):
		self.event = []
		self.time = []
		self.subject = subject
		self.experiment_name = experiment_name
		self.start_date = time.strftime( "%d.%m.%Y_%H.%M" )
		self.end_date = None
		self.file_name = None

	def record( self, event, time ):
		self.event.append( event )
		self.time.append( time )

	def pretty( self ):
		times = np.round( self.time, 3 )
		return( np.vstack( ( times, self.event ) ).T )

	def set_end_date( self ):
		self.end_date = time.strftime( "%d.%m.%Y_%H.%M" )

	def save_csv( self ):
		subject = str(self.subject)
		experiment_name = str(self.experiment_name)
		start_date = self.start_date
		end_date = self.end_date
		self.file_name = start_date + "__" + end_date + "__" + subject +".csv"
		meta_data = [
			[ "Start_date", start_date ],
			[ "End_date", end_date ],
			[ "Subject", subject ],
			[ "Time", "Event" ] ]

		with open( self.file_name, "w" ) as file:
			writer = csv.writer(file)
			writer.writerows( meta_data )
			writer.writerows( self.pretty() )

	def dropbox_sync( self, upload_script ):
		file_path = os.getcwd() + "/" +self.file_name
		upload_command = upload_script + file_path + " /"
		os.system( upload_command )
		print( "Upload: " + file_path )
		print( upload_command )