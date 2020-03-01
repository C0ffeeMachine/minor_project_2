
class MyApp : public Application {
public:

	MyApp();
	virtual ~MyApp();

	void Setup(Ptr<Socket> socket, Address address, uint32_t packetSize, uint32_t nPackets, DataRate dataRate);
	void ChangeRate(DataRate newrate);

private:
	virtual void StartApplication(void);
	virtual void StopApplication(void);

	void ScheduleTx(void);
	void SendPacket(void);

	ns3::Ptr<Socket>     m_socket;
	ns3::Address         m_peer;
	uint32_t        m_packetSize;
	uint32_t        m_nPackets;
	ns3::DataRate        m_dataRate;
	ns3::EventId         m_sendEvent;
	bool            m_running;
	uint32_t        m_packetsSent;
};

MyApp::MyApp()
	: m_socket(0),
	m_peer(),
	m_packetSize(0),
	m_nPackets(0),
	m_dataRate(0),
	m_sendEvent(),
	m_running(false),
	m_packetsSent(0) {
}

MyApp::~MyApp() {
	m_socket = 0;
}

void
MyApp::Setup(Ptr<Socket> socket, Address address, uint32_t packetSize, uint32_t nPackets, DataRate dataRate) {
	m_socket = socket;
	m_peer = address;
	m_packetSize = packetSize;
	m_nPackets = nPackets;
	m_dataRate = dataRate;
}

void
MyApp::StartApplication(void) {
	m_running = true;
	m_packetsSent = 0;
	m_socket->Bind();
	m_socket->Connect(m_peer);
	SendPacket();
}

void
MyApp::StopApplication(void) {
	m_running = false;

	if (m_sendEvent.IsRunning()) {
		Simulator::Cancel(m_sendEvent);
	}

	if (m_socket) {
		m_socket->Close();
	}
}

void
MyApp::SendPacket(void) {
	Ptr<Packet> packet = Create<Packet>(m_packetSize);
	m_socket->Send(packet);

	if (++m_packetsSent < m_nPackets) {
		ScheduleTx();
	}
}

void
MyApp::ScheduleTx(void) {
	if (m_running) {
		Time tNext(Seconds(m_packetSize * 8 / static_cast<double> ( m_dataRate.GetBitRate() )));
		m_sendEvent = Simulator::Schedule(tNext, &MyApp::SendPacket, this);
	}
}
 
