set terminal png
set output "eval2.png"
set title ""
set xlabel "Time (Seconds)"
set ylabel "Cwnd(Bytes)"
set yrange [0:70000]
set xrange [1:12]

set key outside center below
set datafile missing "-nan"
plot "eval2.cwnd" index 0 title "" with linespoints, "eval2.cwnd" index 1 title "" with linespoints
