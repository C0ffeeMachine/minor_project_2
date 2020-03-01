#include "ns3/constant-position-mobility-model.h"
#include "ns3/core-module.h"
#include "ns3/network-module.h"
#include "ns3/point-to-point-module.h"
#include "ns3/applications-module.h"
#include "ns3/internet-module.h"
#include "ns3/flow-monitor-module.h"
#include "ns3/ipv4-global-routing-helper.h"
#include "ns3/stats-module.h"
#include "ns3/global-route-manager.h"
#include "ns3/bridge-module.h"
#include "ns3/trace-helper.h"
#include "ns3/netanim-module.h"
using namespace ns3;
#include"MyApp.h"
int main(int argc, char *argv[]) {
	std::string animFile = "test.xml";  // Name of file for animation output
	CommandLine cmd;
	cmd.Parse(argc, argv);
	PointToPointHelper p2p;
	p2p.SetDeviceAttribute("DataRate", StringValue("50Mbps"));
	p2p.SetChannelAttribute("Delay", StringValue("10ms"));
	Ptr<Node> n;
	Ptr<ConstantPositionMobilityModel> loc;
	Ipv4AddressHelper ipv4;
	int nnodes=6;
	NodeContainer All;
	All.Create(nnodes);

	NodeContainer nc1_2 = NodeContainer(All.Get(1),All.Get(2));
	NetDeviceContainer ndc1_2 = p2p.Install(nc1_2);

	NodeContainer nc1_0 = NodeContainer(All.Get(1),All.Get(0));
	NetDeviceContainer ndc1_0 = p2p.Install(nc1_0);

	NodeContainer nc1_3 = NodeContainer(All.Get(1),All.Get(3));
	NetDeviceContainer ndc1_3 = p2p.Install(nc1_3);

	NodeContainer nc3_4 = NodeContainer(All.Get(3),All.Get(4));
	NetDeviceContainer ndc3_4 = p2p.Install(nc3_4);

	NodeContainer nc3_5 = NodeContainer(All.Get(3),All.Get(5));
	NetDeviceContainer ndc3_5 = p2p.Install(nc3_5);

	Ptr<RateErrorModel> em = CreateObject<RateErrorModel>();
	em->SetAttribute("ErrorRate", DoubleValue(0.00001));
	ndc1_2.Get(0)->SetAttribute("ReceiveErrorModel", PointerValue(em));
	InternetStackHelper internetStack;
	internetStack.Install(All);
	Ipv4AddressHelper address;

	address.SetBase("10.1.1.0", "255.255.255.0");
	Ipv4InterfaceContainer ifc1_2 = ipv4.Assign(ndc1_2);

	address.SetBase("10.1.2.0", "255.255.255.0");
	Ipv4InterfaceContainer ifc1_0 = ipv4.Assign(ndc1_0);

	address.SetBase("10.1.3.0", "255.255.255.0");
	Ipv4InterfaceContainer ifc1_3 = ipv4.Assign(ndc1_3);

	address.SetBase("10.1.4.0", "255.255.255.0");
	Ipv4InterfaceContainer ifc3_4 = ipv4.Assign(ndc3_4);

	address.SetBase("10.1.5.0", "255.255.255.0");
	Ipv4InterfaceContainer ifc3_5 = ipv4.Assign(ndc3_5);

	uint16_t sinkPort4 = 8080;
	Address sinkAddr4 = InetSocketAddress(ifc3_4.GetAddress(1), sinkPort4);
	PacketSinkHelper packetSinkHelper4 ("ns3::TcpSocketFactory", InetSocketAddress(Ipv4Address::GetAny(), sinkPort4));
	ApplicationContainer sink4 = packetSinkHelper4.Install(All.Get(4));
	sink4.Start(Seconds(0));
	sink4.Stop(Seconds(200.));

	Ptr<Socket> socket2 = Socket::CreateSocket(All.Get(2), TcpSocketFactory::GetTypeId());

	Ptr<MyApp> app0 = CreateObject<MyApp>();
	app0->Setup(socket2, sinkAddr4, 1040, 100000, DataRate("100Mbps"));
	All.Get(2)->AddApplication(app0);
	app0->SetStartTime(Seconds(1));
	app0->SetStopTime(Seconds(200.));

	uint16_t sinkPort5 = 8081;
	Address sinkAddr5 = InetSocketAddress(ifc3_5.GetAddress(1), sinkPort5);
	PacketSinkHelper packetSinkHelper5 ("ns3::TcpSocketFactory", InetSocketAddress(Ipv4Address::GetAny(), sinkPort5));
	ApplicationContainer sink5 = packetSinkHelper5.Install(All.Get(5));
	sink5.Start(Seconds(0));
	sink5.Stop(Seconds(200.));

	Ptr<Socket> socket0 = Socket::CreateSocket(All.Get(0), TcpSocketFactory::GetTypeId());

	Ptr<MyApp> app1 = CreateObject<MyApp>();
	app1->Setup(socket0, sinkAddr5, 1040, 100000, DataRate("100Mbps"));
	All.Get(0)->AddApplication(app1);
	app1->SetStartTime(Seconds(1));
	app1->SetStopTime(Seconds(200.));

	n = All.Get(0);
	loc = n->GetObject<ConstantPositionMobilityModel>();

	if (loc == 0) {
		loc = CreateObject<ConstantPositionMobilityModel>();
		n->AggregateObject(loc);
	}

	Vector v0(40, 25, 0);
	loc->SetPosition(v0);


	n = All.Get(1);
	loc = n->GetObject<ConstantPositionMobilityModel>();

	if (loc == 0) {
		loc = CreateObject<ConstantPositionMobilityModel>();
		n->AggregateObject(loc);
	}

	Vector v1(67, 26, 0);
	loc->SetPosition(v1);


	n = All.Get(2);
	loc = n->GetObject<ConstantPositionMobilityModel>();

	if (loc == 0) {
		loc = CreateObject<ConstantPositionMobilityModel>();
		n->AggregateObject(loc);
	}

	Vector v2(41, 17, 0);
	loc->SetPosition(v2);


	n = All.Get(3);
	loc = n->GetObject<ConstantPositionMobilityModel>();

	if (loc == 0) {
		loc = CreateObject<ConstantPositionMobilityModel>();
		n->AggregateObject(loc);
	}

	Vector v3(88, 26, 0);
	loc->SetPosition(v3);


	n = All.Get(4);
	loc = n->GetObject<ConstantPositionMobilityModel>();

	if (loc == 0) {
		loc = CreateObject<ConstantPositionMobilityModel>();
		n->AggregateObject(loc);
	}

	Vector v4(102, 16, 0);
	loc->SetPosition(v4);


	n = All.Get(5);
	loc = n->GetObject<ConstantPositionMobilityModel>();

	if (loc == 0) {
		loc = CreateObject<ConstantPositionMobilityModel>();
		n->AggregateObject(loc);
	}

	Vector v5(104, 24, 0);
	loc->SetPosition(v5);


PcapHelper pcapHelper;
p2p.EnablePcapAll("eval");
AnimationInterface anim(animFile);
anim.EnablePacketMetadata(); // Optional
anim.EnableIpv4L3ProtocolCounters(Seconds(0), Seconds(200));
Simulator::Stop(Seconds(200.0));
Simulator::Run();
std::cout << "Animation Trace file created:" << animFile.c_str() << std::endl;
Simulator::Destroy();
}
