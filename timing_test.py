# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 12:55:54 2017

@author: yli877
"""

import os
os.chdir( "F:\Dropbox\Don\CABexpt\CABexpt" )
import clock
import importlib
import time
import numpy as np

importlib.reload( clock )

# Using Windows 7 for testing
# Busy timer
def busy_timer(t, rep):
    time_container = np.zeros(rep)
    for i in range(0,rep):
        t1 = time.time()
        while time.time() - t1 < t:
            pass
        t2 = time.time()
        time_container[i] = t2-t1
    return( np.median(time_container) )

#Sleep timer
def sleep_timer(t, rep):
    time_container = np.zeros(rep)
    for i in range(0,rep):
        t1 = time.time()
        time.sleep(t)
        t2 = time.time()
        time_container[i] = t2-t1
    return( np.median(time_container) )

#Hybrid timer
def hybrid_timer(t,rep):
    time_container = np.zeros(rep)
    for i in range(0,rep):
        if t <= 0.5:
            t1 = time.time()
            while time.time() - t1 < t:
                pass
            t2 = time.time()
            time_container[i] = t2-t1
        else:
            t1 = time.time()
            time.sleep( t - 0.4 )
            while time.time() - t1 < t:
                pass
            t2 = time.time()
            time_container[i] = t2-t1
    return( np.median(time_container) )

test_times = np.array( [ 0.01, 0.05, 0.1, 0.5, 1, 5, 10] )
busy_time = []
for t in test_times:
    busy_time.append( busy_timer(t, 5) )
    
sleep_time = []
for t in test_times:
    sleep_time.append( sleep_timer(t, 5) )
    
hybrid_time = []
for t in test_times:
    hybrid_time.append( hybrid_timer(t, 5) )

# Compare percentage timing differences
1- ( np.array( busy_time ) - test_times ) / test_times 

1- ( np.array( sleep_time ) - test_times ) / test_times 

1- ( np.array( hybrid_time ) - test_times ) / test_times