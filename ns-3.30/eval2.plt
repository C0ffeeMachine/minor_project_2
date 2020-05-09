set terminal png
set output "eval2.png"
set title "Packet Byte Count vs. Time \n\nTrace Source Path: /NodeList/*/$ns3::Ipv4L3Protocol/Tx"
set xlabel "Time (Seconds)"
set ylabel "Packet Byte Count"

set key outside center below
set datafile missing "-nan"
plot "eval2.cwnd" index 0 title "Packet Byte Count-0" with linespoints
