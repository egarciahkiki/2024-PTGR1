#!/bin/bash

######

cpptraj << EOF
parm "dry_topology.parm7"
trajin "align_trajectorie.nc"
multidihedral BB phi psi resrange 1-660 out 01_PhiPsi.dat 
run
quit
EOF

######

sed -i '1d' 01_PhiPsi.dat
sed 's/^ *//' 01_PhiPsi.dat | cut -d" " -f2- > 01_DIH_pre.dat
awk ' { for(i=1;i<=NF;i++) $i=($i*$i); print; } ' 01_DIH_pre.dat > 01_DIH_squared.dat
cat 01_DIH_squared.dat | awk '{for(i=1;i<=NF;i++) t+=$i;print t; t=0}' > 01_sum.txt
awk '{print sqrt($1)}' 01_sum.txt > 01_DIH.dat
sed -i '1 i\#DIH' 01_DIH.dat

######

cpptraj << EOF
readdata 01_DIH.dat name DIH separate
autocorr DIH_0 out autocorr.dat
go
quit
EOF

######

awk '{print $2}' autocorr.dat > autocorrF.dat
