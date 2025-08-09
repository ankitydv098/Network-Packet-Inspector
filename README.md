# 🕵️‍♂️ PacketSniffer Pro

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3.2-green.svg?style=for-the-badge&logo=flask&logoColor=white)
![Scapy](https://img.shields.io/badge/Scapy-2.6.1-red.svg?style=for-the-badge&logo=wireshark&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

**🔍 A powerful, web-based network packet analyzer with real-time monitoring and threat detection**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Screenshots](#-screenshots) • [Contributing](#-contributing)

---

</div>

## 🌟 Features

### 📊 **Real-time Network Analysis**
- 🔴 **Live packet capture** from any network interface
- 📈 **Interactive protocol distribution charts** 
- 🕒 **Configurable capture duration** and packet limits
- 💾 **Export captures** to PCAP format

### 🛡️ **Security Monitoring**
- 🚨 **Automatic threat detection** (suspicious IP identification)
- 🔍 **Deep packet inspection** with metadata extraction
- 📋 **Detailed packet analysis** with source/destination tracking
- ⚡ **Real-time anomaly detection**

### 🖥️ **User-friendly Web Interface**
- 🎨 **Clean, responsive Bootstrap UI**
- 📁 **Drag & drop PCAP file analysis**
- 📊 **Visual protocol statistics** with pie charts
- 📱 **Mobile-responsive design**

### 🔧 **Advanced Capabilities**
- 🌐 **Multi-interface support** with auto-detection
- 💿 **PCAP file import/export**
- 📝 **Comprehensive logging** and error handling
- ⚙️ **Configurable capture parameters**

---

## 🚀 Installation

### Prerequisites

> ⚠️ **Administrator/Root privileges required** for live packet capture

- 🐍 **Python 3.7+**
- 🔧 **Npcap** (Windows) or **libpcap** (Linux/macOS)
- 🌐 Modern web browser

### 📦 Quick Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/packetsniffer-pro.git
cd packetsniffer-pro
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
# For live capture (requires admin privileges)
sudo python app.py  # Linux/macOS
# or
# Right-click -> "Run as Administrator" on Windows
python app.py
```

4. **Access the web interface**
```
🌐 Open http://localhost:5000 in your browser
```

---

## 💻 Usage

### 🎯 Live Packet Capture

1. 🖱️ **Select Network Interface**: Choose from available interfaces
2. ⏱️ **Set Duration**: Configure capture time (default: 30 seconds)  
3. 📊 **Set Packet Limit**: Optional packet count limit
4. ▶️ **Start Capture**: Click "Start Sniffing" to begin analysis

### 📁 PCAP File Analysis

1. 📂 **Upload File**: Drag & drop or select PCAP file
2. 🔍 **Automatic Analysis**: View results instantly
3. 📈 **View Statistics**: Protocol distribution and packet details
4. 💾 **Download Results**: Export analyzed data

### 🛡️ Security Features

- 🚨 **Threat Detection**: Automatically flags IPs with >100 packets
- 📊 **Traffic Analysis**: Protocol usage breakdown
- 🔍 **Packet Inspection**: Detailed metadata for each packet
- 📋 **Suspicious IP List**: Real-time security alerts

---

## 📸 Screenshots

### 🏠 Main Dashboard
*Clean interface with capture options and results display*

### 📊 Analysis Results  
*Protocol distribution charts and packet statistics*

### 🚨 Security Alerts
*Suspicious IP detection and threat monitoring*

---

## 🛠️ Technical Details

### 📚 Core Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| 🌶️ **Flask** | 2.3.2 | Web framework |
| 🔍 **Scapy** | 2.6.1 | Packet manipulation |
| 🐼 **Pandas** | 2.3.1 | Data analysis |
| 📈 **Matplotlib** | 3.10.5 | Visualization |
| 📦 **dpkt** | 1.9.8 | Packet parsing |

### 🏗️ Architecture

```
📁 Project Structure
├── 🐍 app.py              # Flask web application
├── 🔍 sniff.py            # Packet capture engine  
├── 📋 requirements.txt    # Dependencies
├── 📁 templates/          # HTML templates
├── 📁 static/            # CSS, JS, images
├── 📁 uploads/           # Uploaded PCAP files
└── 📁 captures/          # Generated captures
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### 🐛 Bug Reports
- 📝 Use GitHub Issues
- 🔍 Include system info and error logs
- 📋 Provide reproduction steps

### 💡 Feature Requests  
- 🎯 Clear description of proposed feature
- 📊 Use case examples
- 🔄 Consider backwards compatibility

### 🔧 Pull Requests
1. 🍴 Fork the repository
2. 🌿 Create feature branch (`git checkout -b feature/amazing-feature`)
3. 💾 Commit changes (`git commit -m 'Add amazing feature'`)
4. 📤 Push to branch (`git push origin feature/amazing-feature`)
5. 🔄 Open Pull Request

---

## ⚖️ License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🚨 Security Notice

> **⚠️ Important**: This tool is designed for **authorized network analysis only**. 
> 
> - 🔒 Only use on networks you own or have explicit permission to analyze
> - 🏢 Ensure compliance with local laws and regulations  
> - 🛡️ Use responsibly for security research and network troubleshooting

---

## 📞 Support

### 🆘 Getting Help
- 📚 Check the [Wiki](https://github.com/yourusername/packetsniffer-pro/wiki)
- 🐛 Report issues on [GitHub Issues](https://github.com/yourusername/packetsniffer-pro/issues)
- 💬 Join our [Discussion Forum](https://github.com/yourusername/packetsniffer-pro/discussions)

### 🔧 Common Issues
- **Permission Denied**: Run with administrator/root privileges
- **Interface Not Found**: Check available interfaces with `scapy`
- **Npcap Issues**: Reinstall Npcap with WinPcap compatibility

---

<div align="center">

### 🌟 Star this repo if you found it helpful!

**Made with ❤️ by the PacketSniffer Pro team**

![Visitors](https://visitor-badge.laobi.icu/badge?page_id=yourusername.packetsniffer-pro)

</div>
