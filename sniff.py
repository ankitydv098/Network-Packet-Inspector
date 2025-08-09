from scapy.all import sniff, wrpcap, rdpcap, IP, TCP, get_if_list
from collections import defaultdict
import time
import pandas as pd

class PacketSniffer:
    def __init__(self):
        self.packet_objects = []
        self.packet_metadata = []
        self.suspicious_ips = set()
        self.ip_stats = defaultdict(lambda: {"count": 0, "ports": set()})
        self.start_time = None

    @staticmethod
    def list_interfaces():
        """Return list of available interfaces (names) reported by scapy."""
        try:
            return get_if_list()
        except Exception:
            return []

    def _packet_callback(self, packet):
        """Internal callback used by scapy.sniff."""
        
        self.packet_objects.append(packet)

        
        if packet.haslayer(IP):
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            protocol = packet[IP].proto
            length = len(packet)
            t = round(time.time() - self.start_time, 4) if self.start_time else 0.0

            self.ip_stats[src_ip]["count"] += 1
            if packet.haslayer(TCP):
                self.ip_stats[src_ip]["ports"].add(packet[TCP].dport)

            
            if self.ip_stats[src_ip]["count"] > 100:
                self.suspicious_ips.add(src_ip)

            self.packet_metadata.append({
                "src_ip": src_ip,
                "dst_ip": dst_ip,
                "protocol": protocol,
                "length": length,
                "time_since_start": t
            })

    def start_sniffing(self, interface=None, timeout=30, packet_count=0):
        """
        Live sniffing. If 'interface' provided it must match get_if_list() names.
        timeout = seconds (0 or None means no timeout). packet_count = 0 unlimited.
        Returns: (pandas.DataFrame, set_of_suspicious_ips)
        """
        
        if interface:
            interfaces = self.list_interfaces()
            if interface not in interfaces:
                raise ValueError(f"Interface '{interface}' not found ! Available: {interfaces}")

        
        self.packet_objects = []
        self.packet_metadata = []
        self.suspicious_ips = set()
        self.ip_stats = defaultdict(lambda: {"count": 0, "ports": set()})
        self.start_time = time.time()

        
        sniff(iface=interface, prn=self._packet_callback,
              timeout=(timeout if timeout and timeout > 0 else None),
              count=(packet_count if packet_count and packet_count > 0 else 0),
              store=False)

        df = pd.DataFrame(self.packet_metadata)
        return df, self.suspicious_ips

    def analyze_pcap_file(self, pcap_path):
        """
        Analyze an existing pcap file (rdpcap) and fill internal structures.
        Returns (DataFrame, suspicious_ips_set)
        """
        packets = rdpcap(pcap_path)
        # reset
        self.packet_objects = list(packets)
        self.packet_metadata = []
        self.suspicious_ips = set()
        self.ip_stats = defaultdict(lambda: {"count": 0, "ports": set()})
        self.start_time = 0.0

        for pkt in packets:
            self._packet_callback(pkt)

        df = pd.DataFrame(self.packet_metadata)
        return df, self.suspicious_ips

    def save_to_pcap(self, filename="capture.pcap"):
        """Save captured packets to a pcap; returns True if saved."""
        if not self.packet_objects:
            return False
        wrpcap(filename, self.packet_objects)
        return True
