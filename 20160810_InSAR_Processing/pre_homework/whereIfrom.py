#!/bin/bash

grd=./BayArea_DEM/dem.grd
cpt=./BayArea_DEM/topo.cpt
new_grd=./BayArea_DEM/dem_i.grd
BK_lat=37.8719
BK_lon=-122.2585

gmt makecpt -Crainbow -T-200/1200/200 -Z > $cpt
gmt grdgradient $grd -A100 -fg -G$new_grd

#
gmt grdimage $grd -I$new_grd -JM6i -P -Ba -Ctopo.cpt -K > GMT_tut_15.ps
echo "$BK_lon $BK_lat" | gmt psxy -R -J -Sa0.6 -Gred -P -K -O >> GMT_tut_15.ps
gmt pscoast -R$grd -JM6i -B5 -P -W0.1p -N2  -Df -O -K >> GMT_tut_15.ps
gmt pstext -R -J -P -O -K -F+f18p,Helvetica,red << EOF >>  GMT_tut_15.ps
-122.25 37.9 Berkeley
EOF
gmt psscale -DjTC+w5i/0.25i+h+o0/-1i -R$grd -J -C$cpt -I0.4 -By+lm -O >> GMT_tut_15.ps
