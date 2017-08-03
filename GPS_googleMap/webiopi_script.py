# Imports
import webiopi
import time
import os, sys #mkdir(path)

# Enable debug output
#webiopi.setDebug()

global allGpsData
allGpsData = []

# Called by WebIOPi at script loading
def setup():
    try:
        global refreshTimeInterval
        refreshTimeInterval = 0

    except Exception as Err:
        webiopi.debug('%s' % Err)

# Looped by WebIOPi
def loop():
    global refreshTimeInterval
    global allGpsData

    try:
        webiopi.info('Read:%s' % getAllGpsData())

    except Exception as Err:
        webiopi.debug('%s' % Err)
    finally:
        # Cyclic Period
        webiopi.sleep(1)
        #refreshTimeInterval += 1

# Called by WebIOPi at server shutdown
def destroy():
    try:
        webiopi.debug("Script with macros - Destroy")
    except Exception as Err:
        webiopi.debug('%s' % Err)

@webiopi.macro
def SetAllGpsData(gpsData):
    #webiopi.debug('SetAllGpsData')
    global allGpsData
    allGpsData = gpsData
    #webiopi.debug('set : %s' % allGpsData)

@webiopi.macro
def getAllGpsData():
    global allGpsData
    return allGpsData
