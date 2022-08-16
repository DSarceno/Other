set terminal pdf
set output "prueba.pdf"

set multiplot

set ytics nomirror
set y2tics
set yrange[0:100]
set y2range [-1:1]
set xrange [0:2*pi]

set ylabel "Exponencial"
set y2label "Sinuoidal"

plot exp(x) axis x1y1, sin(x) axis x1y2

unset tics
set margins 0,0,0,0
set size 0.2

unset y2label

set tics
set grid
set origin 0.2,0.4
clear
set xlabel "x"
set ylabel "Cosine"
set yrange [-1:1]
set xrange [0:2*pi]
plot cos(x)
