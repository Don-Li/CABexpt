from csv import writer
from os import getcwd, system
import clock
import log_file

class event_record(object):
    """This is an event record"""

    def __init__( self, experiment_name, CABmanager = None, extra_columns = None ):
        self.event_record = []
        self.start_date = None
        self.start_time = None
        self.end_date = None
        self.end_time = None
        self.file_name = None
        self.extra_columns = extra_columns
        self.subject = None
        self.session = None
        self.parameters = None
        self.experiment_name = experiment_name
        self.directory = None
        
        if ( CABmanager != None ):
            self.subject = CABmanager.subject
            self.session = CABmanager.session
            self.directory = CABmanager.directory

    # Separate record and record_extra for speed
    def record( self, event, time ):
        """
        Append a tuple containing time and event to the event record
        """
        self.event_record.append( ( time, event ) )

    def record_extra( self, event, time, tuple_extra ):
        """
        Append a tuple containing time and event and another tuple of extra variables to the event record
        """
        event_info = ( time, event ) + tuple_extra
        self.event_record.append( event_info )

    def set_end_date( self ):
        """
        Set the end date and end time attributes of the event record as the current date and time
        """
        self.end_date = clock.get_date_dmy()
        self.end_time = clock.get_date_hm()
    
    def set_start_date( self ):
        """
        Set the start date and start time attributes of the event record as the current date and time
        """
        self.start_date = clock.get_date_dmy()
        self.start_time = clock.get_date_hm()

    def save_csv( self, directory = None, extra_array_names = None, extra_arrays = None ):
        
        if ( extra_arrays != None and extra_array_names == None ):
            raise ValueError( "Enter a list of array names associated with 'extra_arrays'.")
        if ( extra_arrays == None and extra_array_names != None ):
            raise ValueError( "Names for 'extra_arrays' entered, but no extra arrays.")
        
        ##### Make variables #####
        subject = str( self.subject )
        experiment_name = str( self.experiment_name )
        start_date = str( self.start_date )
        start_time = str( self.start_time )
        end_date = str( self.end_date )
        end_time = str( self.end_time )
        session = str( self.session )
        ###########################
        
        
        self.file_name = "%s_%s_%s_%s.csv" % ( start_date, start_time, subject, experiment_name )
        if directory != None:
            self.file_name = directory + self.file_name
        
        ##### Organise meta data and extend if needed for extra events #####
        time_event_column = [ "Time", "Event" ]
        if ( self.extra_columns != None ):
            time_event_column.append( self.extra_columns )
        
        meta_data = [
            [ "Start_date", start_date ],
            [ "Start_time", start_time ],
            [ "End_date", end_date ],
            [ "End_time", end_time ],
            [ "Subject", subject ],
            [ "Session", session ],
            [ "Experiment_name", experiment_name ],
            time_event_column
            ]

        with open( self.file_name, "w" ) as file:
            writer = writer( file, delimiter = ",", lineterminator = "\n")
            writer.writerows( meta_data )
            writer.writerows( self.event_record )
            if extra_arrays != None:
                for array in range(len(extra_array_names)):
                    writer.writerows( ((extra_array_names[array],),) )
                    writer.writerows( zip( extra_arrays[array] ) )
        
        msg = " subject %s, session %s, saved event record" % ( subject, session )
        log_file.update_log( time = clock.get_date_hmdmy(), entry = msg, directory = self.directory )

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
