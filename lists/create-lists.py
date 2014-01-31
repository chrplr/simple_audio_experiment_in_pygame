#! /usr/bin/env python
# Time-stamp: <2014-01-31 18:40 christophe@pallier.org>

import os, glob, random, csv

stims = [ os.path.split(f)[1] for f in glob.glob(os.path.join("..","stimuli","*.wav")) ]
    
sub = 10
runs = 4

for s in range(1, sub+1):
    for r in range(1, runs+1):
        random.shuffle(stims)
        with open("sub%02d_run%d.csv" % (s, r), "w") as csvfile:
            out = csv.writer(csvfile)
            for i in range(len(stims)):
                out.writerow([1000 + i * 3000, stims[i]])


    
    
