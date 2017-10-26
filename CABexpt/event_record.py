import time
import csv
import os
import clock

class event_record(object):
    """This is an event record"""

    def __init__( self, subject, experiment_name, extra_events = None ):
        self.event_record = []
        self.subject = subject
        self.experiment_name = experiment_name
        self.start_date = None
        self.start_time = None
        self.end_date = None
        self.end_time = None
        self.file_name = None
        self.extra_events = extra_events

    # Separate record and record_extra for speed
    def record( self, event, time ):
        self.event_record.append( ( time, event ) )

    def record_extra( self, event, time, tuple_extra ):
        event_info = ( time, event ) + tuple_extra
        self.event_record.append( event_info )

    def set_end_date( self ):
        self.end_date = clock.get_date_dmy()
        self.end_time = clock.get_date_hm()
    
    def set_start_date( self ):
        self.start_date = clock.get_date_dmy()
        self.start_time = clock.get_date_hm()

    def save_csv( self, extra_array_names = None, extra_arrays = None ):
        
        if ( extra_arrays != None and extra_array_names == None ):
            raise ValueError( "Enter a list of array names assocaited with 'extra_arrays'.")
        if ( extra_arrays == None and extra_array_names != None ):
            raise ValueError( "Names for 'extra_arrays' entered, but no extra arrays.")
        
        ##### Make variables #####
        subject = str( self.subject )
        experiment_name = str( self.experiment_name )
        start_date = str( self.start_date )
        start_time = str( self.start_time )
        end_date = str( self.end_date )
        end_time = str( self.end_time )
        ###########################
        
        self.file_name = "%s_%s_%s_%s.csv" % ( start_date, start_time, subject, experiment_name )
        
        ##### Organise meta data and extend if needed for extra events #####
        meta_data = [
            [ "Start_date", start_date ],
            [ "Start_time", start_time ],
            [ "End_date", end_date ],
            [ "End_time", end_time ],
            [ "Subject", subject ],
            [ "Experiment_name", experiment_name ],
            [ "Time", "Event" ]
            ]
        # Add additional columns for extra events
        if self.extra_events != None:
            for data in meta_data:
                if data[0] != "Time":
                    data.extend( [""] * len( self.extra_events ))
                else:
                    data.extend( self.extra_events )
        #####################################################################

        with open( self.file_name, "w" ) as file:
            writer = csv.writer( file, delimiter = ",", lineterminator = "\n")
            writer.writerows( meta_data )
            writer.writerows( self.event_record )
            if extra_arrays != None:
                for array in range(0, len(extra_arrays)):
                    writer.writerows( ((extra_array_names[array],),) )
                    writer.writerows( zip( extra_arrays[array] ) )

    def dropbox_sync( self ):
        upload_script = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload "
        file_path = os.getcwd() + "/" +self.file_name
        upload_command = upload_script + file_path + " /"
        os.system( upload_command )
        print( "Upload: " + file_path )
        print( upload_command )

    def delete( self, index = None ):
        """
        Delete an entry from the event record at 'index'.
        index: The index of the event record to be deleted. Defaults to "None" which deletes the last entry in the event record.
        """
        if index != None:
            del self.event.record[index]
        else:
            del self.event_record[ len( self.event_record )-1 ]
