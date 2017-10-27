# External module imports
import time
import pigpio
import numpy as np
import event_record as er
import os
import input_outputs as io
import clock as c

##### Set up experiment manager #####
subject = "testsubject"
parameter_file = "parameters.csv"
session_info_file = "session_info.csv"
directory = "/home/pi/Experiment"
expt_manager = CABmanager( subject , parameter_file, session_info_file, directory )
# Pin Definitons:
output_definitions ={
    green1": 17, "red1": 16, "yellow1": 13, "blue1": 12,
    "green2": 18, "red2": 19, "yellow2": 20, "blue2": 21,
    "mag1":25
}
input_definitions = {"key1": 22, "key2": 23, "key3": 24}
# Set up stimulus class
outputs = io.stimulus( output_definitions, pi )
keylights = [ "green1", "red1", "yellow1", "blue1", "green2", "red2", "yellow2", "blue2" ]
maglight = [ "mag1" ]
# Set up operandum class
inputs = io.operandum( input_definitions, pi, 1000, pigpio.PUD_DOWN )

#### Set up event record ####
my_events = er.event_record( subject = subject, experiment_name = experiment_name )

#### Set up reinforcement ####
rft_duration = 2.5
iri = 4

#### Set up times ####
end_time = 3600 # seconds
clock = c.clock()

# Have a 0.01s delay
while clock.update() < 0.01:
inputs.key_reset()

#### Procedure ####
try:
    rft_time = clock.update() + iri
    print( "rft_time " + str(rft_time) )
    # Main procedure
    outputs.on( keylights )
    while clock.update() < end_time:
        if inputs.key_pressed():
            time_now = clock.update()
            my_events.record( event = inputs.get_key(), time = time_now )
            print( str(my_events.time[-1]) + " " + my_events.event[-1] )
            if time_now >= rft_time:
                outputs.off( keylights )
                outputs.on( maglight )
                my_events.record( event = "food", time = time_now )
                time.sleep( rft_duration )
                outputs.off( maglight )
                rft_time = clock.update() + iri
                print( "next rft" + str(rft_time) )
                inputs.key_reset()
                outputs.on( keylights )
    my_events.record( event = "session_end", time = clock.update() )
    outputs.off( maglight )

except KeyboardInterrupt:
    my_events.record( event = "session_end", time = clock.update() )
    outputs.off( maglight )
    print("")
    pass

#### Clean up gpios ####
inputs.teardown()
outputs.all_off()

#### Clean up and save event record ####
my_events.set_end_date()
my_events.save_csv()
#upload_script = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload "
#my_events.dropbox_sync( upload_script )

#### Kill ####
print( "Goodbye cruel world" )


