#! /usr/bin/env python
# Time-stamp: <2014-01-31 19:39 christophe@pallier.org>
#
# This script plays a series a sound files listed in a csv file

from utils import *
import sys, csv, os

if len(sys.argv) != 2:
    print "Usage: " + sys.argv[0] + " subXX_runY "
    print ""
    print "Launch the stimulation for WP1 experiment."
    print "XX from 01 to 10, Y from 1 to 4"
    sys.exit()

# reads in the list of trials
session = sys.argv[1]
stimfile = os.path.join("lists", session + ".csv")

try:
    file = open(stimfile)
except IOError:
    sys.exit("Cannot open file " + stimfile)

trials = [ i for i in csv.reader(file) ]


# Initialisations
Init('results.dat', FullScreen=False)
Save("# " +  session)

# Preloads the sound files
sounds = {}
for t in trials:
    stim = t[1]
    wavfile = os.path.join("stimuli", stim)
    if not sounds.has_key(stim):
        sounds[stim] = LoadSound(wavfile)


point = pygame.image.load('fixation3.bmp').convert()
Blit(point, [ 640/2 - 25, 480/2 - 50 ])
UpdateScreen()

Message("Press any key to start...")
WaitForAnyKeyPress()
ClearMessage()


# Main loop
t0 = Clock()
trialnum = 1
for t in trials:
    onset,  stim = int(t[0]), t[1] # the filename is the 2nd column
    while (Clock() - t0) < onset:
        pass
    Message(" %s : %dms -- %d/%d  : %s" % (session, Clock()-t0, trialnum, len(trials), stim))
    PlaySound(sounds[stim])
    Save(str(Clock()) + '\t' + stim)
    if CheckEscape(): 
        break
    trialnum = trialnum + 1

Message("Waiting 15 seconds before closing (Press 'Escape' to abort now)")
t1 = Clock() 
while (Clock() - t1) < 15000 and not CheckEscape():
    Wait(500)

Quit()
