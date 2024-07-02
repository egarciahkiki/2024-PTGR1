#!/bin/bash

mdlovofit -mapfrac A_all.pdb > rmsd_A.dat

mdlovofit -f 0.70 -t A_lovofit.pdb A_all.pdb  -atoms CA C N O -rmsf rmsf_A.dat -ntrial 10000
