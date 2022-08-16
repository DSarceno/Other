set terminal gif animate delay 1
set output 'output.gif'
stats 'data.dat' nooutput
set xrange [-2:2]
set yrange [-2:2]
unset key

do for [i=0:int(STATS_records)] {
   plot 'data.dat' every ::::(i-1) pt 12 ps 1  lc 2, 'data.dat' every ::i::i pt 13 ps 2  lc 4
}

do for [i=0:50]{
    plot 'data.dat' pt 12 ps 1 lc 2
}
