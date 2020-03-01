#! /usr/bin/env python3

# Programs that are runnable.
ns3_runnable_programs = ['build/src/aodv/examples/ns3.30-aodv-debug', 'build/src/applications/examples/ns3.30-three-gpp-http-example-debug', 'build/src/bridge/examples/ns3.30-csma-bridge-debug', 'build/src/bridge/examples/ns3.30-csma-bridge-one-hop-debug', 'build/src/buildings/examples/ns3.30-buildings-pathloss-profiler-debug', 'build/src/config-store/examples/ns3.30-config-store-save-debug', 'build/src/core/examples/ns3.30-main-callback-debug', 'build/src/core/examples/ns3.30-sample-simulator-debug', 'build/src/core/examples/ns3.30-main-ptr-debug', 'build/src/core/examples/ns3.30-main-random-variable-stream-debug', 'build/src/core/examples/ns3.30-sample-random-variable-debug', 'build/src/core/examples/ns3.30-sample-random-variable-stream-debug', 'build/src/core/examples/ns3.30-command-line-example-debug', 'build/src/core/examples/ns3.30-hash-example-debug', 'build/src/core/examples/ns3.30-sample-log-time-format-debug', 'build/src/core/examples/ns3.30-test-string-value-formatting-debug', 'build/src/core/examples/ns3.30-sample-show-progress-debug', 'build/src/core/examples/ns3.30-main-test-sync-debug', 'build/src/csma/examples/ns3.30-csma-one-subnet-debug', 'build/src/csma/examples/ns3.30-csma-broadcast-debug', 'build/src/csma/examples/ns3.30-csma-packet-socket-debug', 'build/src/csma/examples/ns3.30-csma-multicast-debug', 'build/src/csma/examples/ns3.30-csma-raw-ip-socket-debug', 'build/src/csma/examples/ns3.30-csma-ping-debug', 'build/src/csma-layout/examples/ns3.30-csma-star-debug', 'build/src/dsdv/examples/ns3.30-dsdv-manet-debug', 'build/src/dsr/examples/ns3.30-dsr-debug', 'build/src/energy/examples/ns3.30-li-ion-energy-source-debug', 'build/src/energy/examples/ns3.30-rv-battery-model-test-debug', 'build/src/energy/examples/ns3.30-basic-energy-model-test-debug', 'build/src/fd-net-device/examples/ns3.30-dummy-network-debug', 'build/src/fd-net-device/examples/ns3.30-fd2fd-onoff-debug', 'build/src/fd-net-device/examples/ns3.30-realtime-dummy-network-debug', 'build/src/fd-net-device/examples/ns3.30-realtime-fd2fd-onoff-debug', 'build/src/fd-net-device/examples/ns3.30-fd-emu-ping-debug', 'build/src/fd-net-device/examples/ns3.30-fd-emu-udp-echo-debug', 'build/src/fd-net-device/examples/ns3.30-fd-emu-onoff-debug', 'build/src/fd-net-device/examples/ns3.30-fd-tap-ping-debug', 'build/src/fd-net-device/examples/ns3.30-fd-tap-ping6-debug', 'build/src/internet/examples/ns3.30-main-simple-debug', 'build/src/internet-apps/examples/ns3.30-dhcp-example-debug', 'build/src/lr-wpan/examples/ns3.30-lr-wpan-packet-print-debug', 'build/src/lr-wpan/examples/ns3.30-lr-wpan-phy-test-debug', 'build/src/lr-wpan/examples/ns3.30-lr-wpan-data-debug', 'build/src/lr-wpan/examples/ns3.30-lr-wpan-error-model-plot-debug', 'build/src/lr-wpan/examples/ns3.30-lr-wpan-error-distance-plot-debug', 'build/src/lte/examples/ns3.30-lena-cqi-threshold-debug', 'build/src/lte/examples/ns3.30-lena-dual-stripe-debug', 'build/src/lte/examples/ns3.30-lena-fading-debug', 'build/src/lte/examples/ns3.30-lena-intercell-interference-debug', 'build/src/lte/examples/ns3.30-lena-ipv6-addr-conf-debug', 'build/src/lte/examples/ns3.30-lena-ipv6-ue-rh-debug', 'build/src/lte/examples/ns3.30-lena-ipv6-ue-ue-debug', 'build/src/lte/examples/ns3.30-lena-pathloss-traces-debug', 'build/src/lte/examples/ns3.30-lena-profiling-debug', 'build/src/lte/examples/ns3.30-lena-rem-debug', 'build/src/lte/examples/ns3.30-lena-rem-sector-antenna-debug', 'build/src/lte/examples/ns3.30-lena-rlc-traces-debug', 'build/src/lte/examples/ns3.30-lena-simple-debug', 'build/src/lte/examples/ns3.30-lena-simple-epc-debug', 'build/src/lte/examples/ns3.30-lena-simple-epc-backhaul-debug', 'build/src/lte/examples/ns3.30-lena-deactivate-bearer-debug', 'build/src/lte/examples/ns3.30-lena-x2-handover-debug', 'build/src/lte/examples/ns3.30-lena-x2-handover-measures-debug', 'build/src/lte/examples/ns3.30-lena-frequency-reuse-debug', 'build/src/lte/examples/ns3.30-lena-distributed-ffr-debug', 'build/src/lte/examples/ns3.30-lena-uplink-power-control-debug', 'build/src/lte/examples/ns3.30-lena-radio-link-failure-debug', 'build/src/lte/examples/ns3.30-lena-simple-epc-emu-debug', 'build/src/mesh/examples/ns3.30-mesh-debug', 'build/src/mobility/examples/ns3.30-main-grid-topology-debug', 'build/src/mobility/examples/ns3.30-main-random-topology-debug', 'build/src/mobility/examples/ns3.30-main-random-walk-debug', 'build/src/mobility/examples/ns3.30-mobility-trace-example-debug', 'build/src/mobility/examples/ns3.30-ns2-mobility-trace-debug', 'build/src/mobility/examples/ns3.30-bonnmotion-ns2-example-debug', 'build/src/mpi/examples/ns3.30-simple-distributed-debug', 'build/src/mpi/examples/ns3.30-third-distributed-debug', 'build/src/mpi/examples/ns3.30-nms-p2p-nix-distributed-debug', 'build/src/mpi/examples/ns3.30-simple-distributed-empty-node-debug', 'build/src/netanim/examples/ns3.30-dumbbell-animation-debug', 'build/src/netanim/examples/ns3.30-grid-animation-debug', 'build/src/netanim/examples/ns3.30-star-animation-debug', 'build/src/netanim/examples/ns3.30-wireless-animation-debug', 'build/src/netanim/examples/ns3.30-uan-animation-debug', 'build/src/netanim/examples/ns3.30-colors-link-description-debug', 'build/src/netanim/examples/ns3.30-resources-counters-debug', 'build/src/network/examples/ns3.30-main-packet-header-debug', 'build/src/network/examples/ns3.30-main-packet-tag-debug', 'build/src/network/examples/ns3.30-packet-socket-apps-debug', 'build/src/nix-vector-routing/examples/ns3.30-nix-simple-debug', 'build/src/nix-vector-routing/examples/ns3.30-nms-p2p-nix-debug', 'build/src/olsr/examples/ns3.30-simple-point-to-point-olsr-debug', 'build/src/olsr/examples/ns3.30-olsr-hna-debug', 'build/src/point-to-point/examples/ns3.30-main-attribute-value-debug', 'build/src/propagation/examples/ns3.30-main-propagation-loss-debug', 'build/src/propagation/examples/ns3.30-jakes-propagation-model-example-debug', 'build/src/sixlowpan/examples/ns3.30-example-sixlowpan-debug', 'build/src/sixlowpan/examples/ns3.30-example-ping-lr-wpan-debug', 'build/src/spectrum/examples/ns3.30-adhoc-aloha-ideal-phy-debug', 'build/src/spectrum/examples/ns3.30-adhoc-aloha-ideal-phy-matrix-propagation-loss-model-debug', 'build/src/spectrum/examples/ns3.30-adhoc-aloha-ideal-phy-with-microwave-oven-debug', 'build/src/spectrum/examples/ns3.30-tv-trans-example-debug', 'build/src/spectrum/examples/ns3.30-tv-trans-regional-example-debug', 'build/src/stats/examples/ns3.30-gnuplot-example-debug', 'build/src/stats/examples/ns3.30-double-probe-example-debug', 'build/src/stats/examples/ns3.30-time-probe-example-debug', 'build/src/stats/examples/ns3.30-gnuplot-aggregator-example-debug', 'build/src/stats/examples/ns3.30-gnuplot-helper-example-debug', 'build/src/stats/examples/ns3.30-file-aggregator-example-debug', 'build/src/stats/examples/ns3.30-file-helper-example-debug', 'build/src/tap-bridge/examples/ns3.30-tap-csma-debug', 'build/src/tap-bridge/examples/ns3.30-tap-csma-virtual-machine-debug', 'build/src/tap-bridge/examples/ns3.30-tap-wifi-virtual-machine-debug', 'build/src/tap-bridge/examples/ns3.30-tap-wifi-dumbbell-debug', 'build/src/topology-read/examples/ns3.30-topology-example-sim-debug', 'build/src/traffic-control/examples/ns3.30-red-tests-debug', 'build/src/traffic-control/examples/ns3.30-red-vs-ared-debug', 'build/src/traffic-control/examples/ns3.30-adaptive-red-tests-debug', 'build/src/traffic-control/examples/ns3.30-pfifo-vs-red-debug', 'build/src/traffic-control/examples/ns3.30-codel-vs-pfifo-basic-test-debug', 'build/src/traffic-control/examples/ns3.30-codel-vs-pfifo-asymmetric-debug', 'build/src/traffic-control/examples/ns3.30-pie-example-debug', 'build/src/uan/examples/ns3.30-uan-cw-example-debug', 'build/src/uan/examples/ns3.30-uan-rc-example-debug', 'build/src/uan/examples/ns3.30-uan-raw-example-debug', 'build/src/uan/examples/ns3.30-uan-ipv4-example-debug', 'build/src/uan/examples/ns3.30-uan-ipv6-example-debug', 'build/src/uan/examples/ns3.30-uan-6lowpan-example-debug', 'build/src/virtual-net-device/examples/ns3.30-virtual-net-device-debug', 'build/src/wave/examples/ns3.30-wave-simple-80211p-debug', 'build/src/wave/examples/ns3.30-wave-simple-device-debug', 'build/src/wave/examples/ns3.30-vanet-routing-compare-debug', 'build/src/wifi/examples/ns3.30-wifi-phy-test-debug', 'build/src/wifi/examples/ns3.30-test-interference-helper-debug', 'build/src/wifi/examples/ns3.30-wifi-manager-example-debug', 'build/src/wifi/examples/ns3.30-wifi-trans-example-debug', 'build/src/wifi/examples/ns3.30-wifi-phy-configuration-debug', 'build/src/wimax/examples/ns3.30-wimax-ipv4-debug', 'build/src/wimax/examples/ns3.30-wimax-multicast-debug', 'build/src/wimax/examples/ns3.30-wimax-simple-debug', 'build/examples/udp/ns3.30-udp-echo-debug', 'build/examples/tutorial/ns3.30-hello-simulator-debug', 'build/examples/tutorial/ns3.30-first-debug', 'build/examples/tutorial/ns3.30-second-debug', 'build/examples/tutorial/ns3.30-third-debug', 'build/examples/tutorial/ns3.30-fourth-debug', 'build/examples/tutorial/ns3.30-fifth-debug', 'build/examples/tutorial/ns3.30-sixth-debug', 'build/examples/tutorial/ns3.30-seventh-debug', 'build/examples/wireless/ns3.30-mixed-wired-wireless-debug', 'build/examples/wireless/ns3.30-wifi-adhoc-debug', 'build/examples/wireless/ns3.30-wifi-clear-channel-cmu-debug', 'build/examples/wireless/ns3.30-wifi-ap-debug', 'build/examples/wireless/ns3.30-wifi-wired-bridging-debug', 'build/examples/wireless/ns3.30-multirate-debug', 'build/examples/wireless/ns3.30-wifi-simple-adhoc-debug', 'build/examples/wireless/ns3.30-wifi-simple-adhoc-grid-debug', 'build/examples/wireless/ns3.30-wifi-simple-infra-debug', 'build/examples/wireless/ns3.30-wifi-simple-interference-debug', 'build/examples/wireless/ns3.30-wifi-blockack-debug', 'build/examples/wireless/ns3.30-dsss-validation-debug', 'build/examples/wireless/ns3.30-ofdm-validation-debug', 'build/examples/wireless/ns3.30-ofdm-ht-validation-debug', 'build/examples/wireless/ns3.30-ofdm-vht-validation-debug', 'build/examples/wireless/ns3.30-wifi-hidden-terminal-debug', 'build/examples/wireless/ns3.30-ht-wifi-network-debug', 'build/examples/wireless/ns3.30-vht-wifi-network-debug', 'build/examples/wireless/ns3.30-wifi-timing-attributes-debug', 'build/examples/wireless/ns3.30-wifi-sleep-debug', 'build/examples/wireless/ns3.30-power-adaptation-distance-debug', 'build/examples/wireless/ns3.30-power-adaptation-interference-debug', 'build/examples/wireless/ns3.30-rate-adaptation-distance-debug', 'build/examples/wireless/ns3.30-wifi-aggregation-debug', 'build/examples/wireless/ns3.30-wifi-txop-aggregation-debug', 'build/examples/wireless/ns3.30-simple-ht-hidden-stations-debug', 'build/examples/wireless/ns3.30-80211n-mimo-debug', 'build/examples/wireless/ns3.30-mixed-network-debug', 'build/examples/wireless/ns3.30-wifi-tcp-debug', 'build/examples/wireless/ns3.30-80211e-txop-debug', 'build/examples/wireless/ns3.30-wifi-spectrum-per-example-debug', 'build/examples/wireless/ns3.30-wifi-spectrum-per-interference-debug', 'build/examples/wireless/ns3.30-wifi-spectrum-saturation-example-debug', 'build/examples/wireless/ns3.30-ofdm-he-validation-debug', 'build/examples/wireless/ns3.30-he-wifi-network-debug', 'build/examples/wireless/ns3.30-wifi-multi-tos-debug', 'build/examples/wireless/ns3.30-wifi-backward-compatibility-debug', 'build/examples/wireless/ns3.30-wifi-pcf-debug', 'build/examples/wireless/ns3.30-wifi-spatial-reuse-debug', 'build/examples/ipv6/ns3.30-icmpv6-redirect-debug', 'build/examples/ipv6/ns3.30-ping6-debug', 'build/examples/ipv6/ns3.30-radvd-debug', 'build/examples/ipv6/ns3.30-radvd-two-prefix-debug', 'build/examples/ipv6/ns3.30-test-ipv6-debug', 'build/examples/ipv6/ns3.30-fragmentation-ipv6-debug', 'build/examples/ipv6/ns3.30-fragmentation-ipv6-two-MTU-debug', 'build/examples/ipv6/ns3.30-loose-routing-ipv6-debug', 'build/examples/ipv6/ns3.30-wsn-ping6-debug', 'build/examples/energy/ns3.30-energy-model-example-debug', 'build/examples/energy/ns3.30-energy-model-with-harvesting-example-debug', 'build/examples/naming/ns3.30-object-names-debug', 'build/examples/matrix-topology/ns3.30-matrix-topology-debug', 'build/examples/routing/ns3.30-dynamic-global-routing-debug', 'build/examples/routing/ns3.30-static-routing-slash32-debug', 'build/examples/routing/ns3.30-global-routing-slash32-debug', 'build/examples/routing/ns3.30-global-injection-slash32-debug', 'build/examples/routing/ns3.30-simple-global-routing-debug', 'build/examples/routing/ns3.30-simple-alternate-routing-debug', 'build/examples/routing/ns3.30-mixed-global-routing-debug', 'build/examples/routing/ns3.30-simple-routing-ping6-debug', 'build/examples/routing/ns3.30-manet-routing-compare-debug', 'build/examples/routing/ns3.30-ripng-simple-network-debug', 'build/examples/routing/ns3.30-rip-simple-network-debug', 'build/examples/routing/ns3.30-global-routing-multi-switch-plus-router-debug', 'build/examples/error-model/ns3.30-simple-error-model-debug', 'build/examples/realtime/ns3.30-realtime-udp-echo-debug', 'build/examples/stats/ns3.30-wifi-example-sim-debug', 'build/examples/tcp/ns3.30-tcp-large-transfer-debug', 'build/examples/tcp/ns3.30-tcp-nsc-lfn-debug', 'build/examples/tcp/ns3.30-tcp-nsc-zoo-debug', 'build/examples/tcp/ns3.30-tcp-star-server-debug', 'build/examples/tcp/ns3.30-star-debug', 'build/examples/tcp/ns3.30-tcp-bulk-send-debug', 'build/examples/tcp/ns3.30-tcp-pcap-nanosec-example-debug', 'build/examples/tcp/ns3.30-tcp-nsc-comparison-debug', 'build/examples/tcp/ns3.30-tcp-variants-comparison-debug', 'build/examples/tcp/ns3.30-tcp-pacing-debug', 'build/examples/socket/ns3.30-socket-bound-static-routing-debug', 'build/examples/socket/ns3.30-socket-bound-tcp-static-routing-debug', 'build/examples/socket/ns3.30-socket-options-ipv4-debug', 'build/examples/socket/ns3.30-socket-options-ipv6-debug', 'build/examples/traffic-control/ns3.30-traffic-control-debug', 'build/examples/traffic-control/ns3.30-queue-discs-benchmark-debug', 'build/examples/traffic-control/ns3.30-red-vs-fengadaptive-debug', 'build/examples/traffic-control/ns3.30-red-vs-nlred-debug', 'build/examples/traffic-control/ns3.30-tbf-example-debug', 'build/examples/traffic-control/ns3.30-cobalt-vs-codel-debug', 'build/examples/udp-client-server/ns3.30-udp-client-server-debug', 'build/examples/udp-client-server/ns3.30-udp-trace-client-server-debug', 'build/scratch/subdir/ns3.30-subdir-debug', 'build/scratch/ns3.30-scratch-simulator-debug', 'build/scratch/ns3.30-test1-debug', 'build/scratch/ns3.30-eval2-debug']

# Scripts that are runnable.
ns3_runnable_scripts = ['csma-bridge.py', 'sample-simulator.py', 'wifi-olsr-flowmon.py', 'tap-csma-virtual-machine.py', 'tap-wifi-virtual-machine.py', 'first.py', 'second.py', 'third.py', 'mixed-wired-wireless.py', 'wifi-ap.py', 'simple-routing-ping6.py', 'realtime-udp-echo.py']

