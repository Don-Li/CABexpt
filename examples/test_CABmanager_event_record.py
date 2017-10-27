# Test some things

import importlib
importlib.reload( experiment_reader )
importlib.reload( CAB_manager )

expt_manager = CAB_manager.CABmanager( 
    subject = "testbird", session = 1, parameter_file = "parameters.csv",
    directory = "D://CABexpt//CABexpt", windows_test = True)

expt_manager = CAB_manager.CABmanager( 
    subject = "testbird", session_info_file = "session_info.csv", parameter_file = "parameters.csv",
    directory = "D://CABexpt//CABexpt", windows_test = True)

import event_record
importlib.reload( event_record )

my_events = event_record.event_record( 
    experiment_name = "test_experiment",
    CABmanager = expt_manager, extra_columns = "testcol" )

my_events.set_start_date()

my_events.record( "a", 1 )
my_events.record_extra( "b", 2, ("test",) )
my_events.record( "c", 3 )
my_events.record_extra( "d", 4, ("test",) )
my_events.record( "e", 5 )

my_events.set_end_date()

my_events.save_csv( "D://CABexpt//CABexpt", [ "testExtra", "testExtra2" ], [ list(range(10)), list(range(15)) ] )

