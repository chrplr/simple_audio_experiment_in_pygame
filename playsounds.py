#! /usr/bin/env python
# Time-stamp: <2015-12-29 12:42 christophe@pallier.org>
#
# This script plays a series a sound files listed in a csv file
# Licence: GNU GPL

from utils import *
import sys
import csv
import os

SOUNDSDIR = "sounds"

if len(sys.argv) != 2:
    print "Usage: " + sys.argv[0] + " list.csv "
    print ""
    print "Plays the sound files listed in the file 'list.csv'\n"
    print """The csv file must be a table with two columns:
              - the first contains onset times in milliseconds
              - the second provides the sound file name."""
    sys.exit()

# reads in the list of trials
listfile = sys.argv[1]
try:
    lists = open(listfile)
except IOError:
    sys.exit("Cannot open file " + listfile)

trials = [i for i in csv.reader(lists)]

# Initialisations
Init('results.dat', FullScreen=False)

# Preloads the sound files
sounds = {}
for t in trials:
    stim = t[1]
    wavfile = os.path.join(SOUNDSDIR, stim)
    if stim not in sounds:
        sounds[stim] = LoadSound(wavfile)

point = pygame.image.load('fixation3.bmp').convert()
Blit(point, [640 / 2 - 25, 480 / 2 - 50])
UpdateScreen()

Message("Press any key to start...")
WaitForAnyKeyPress()
ClearMessage()

# Main loop
t0 = Clock()
trialnum = 1
for t in trials:
    onset, stim = int(t[0]), t[1]  # time in column0, filename in column1
    while (Clock() - t0) < onset:
        pass
    Message("(%d/%d) %5d ms, %s" % (trialnum, len(trials), Clock() - t0, stim))
    Save("%5d\t%s\tON" % (Clock() - t0, stim))
    PlaySound(sounds[stim])
    if CheckEscape():
        break
    trialnum = trialnum + 1

Message("Waiting for 2 seconds before closing (Press 'Escape' to abort now)")
t1 = Clock()
while (Clock() - t1) < 2000 and not CheckEscape():
    Wait(500)

Quit()
