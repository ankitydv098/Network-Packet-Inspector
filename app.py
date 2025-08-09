# app.py
from flask import Flask, render_template, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
import os, time
import matplotlib
matplotlib.use("Agg")  
import matplotlib.pyplot as plt

from sniff import PacketSniffer

app = Flask(__name__, static_folder="static")
app.config['UPLOAD_FOLDER'] = "uploads"
app.config['CAPTURE_FOLDER'] = "captures"

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['CAPTURE_FOLDER'], exist_ok=True)
os.makedirs("static", exist_ok=True)


sniffer = PacketSniffer()
latest_pcap_path = None

@app.route("/", methods=["GET", "POST"])
def index():
    global latest_pcap_path
    error = None
    df_html = None
    chart_path = None
    total_packets = 0
    suspicious_ips = []
    duration = 0

    interfaces = PacketSniffer.list_interfaces()

    if request.method == "POST":
        
        uploaded = request.files.get("pcap_file")
        if uploaded and uploaded.filename:
            filename = secure_filename(uploaded.filename)
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            uploaded.save(save_path)
            try:
                df, suspicious = sniffer.analyze_pcap_file(save_path)
                total_packets = len(df)
                suspicious_ips = list(suspicious)
                df_html = df.head(50).to_html(classes="table table-striped", index=False) if not df.empty else None
                if not df.empty:
                    protocol_counts = df["protocol"].value_counts()
                    fig, ax = plt.subplots()
                    ax.pie(protocol_counts, labels=protocol_counts.index, autopct="%1.1f%%")
                    ax.set_title("Protocol Usage")
                    chart_path = os.path.join("static", f"protocol_{int(time.time())}.png")
                    fig.savefig(chart_path, bbox_inches="tight")
                    plt.close(fig)
                latest_pcap_path = save_path
            except Exception as e:
                error = str(e)

            return render_template("index.html", interfaces=interfaces, error=error, df=df_html, chart=chart_path,
                                   total_packets=total_packets, suspicious_ips=suspicious_ips, duration=duration)

        
        interface = request.form.get("interface") or None
        duration = int(request.form.get("duration") or 30)
        packet_limit = int(request.form.get("packet_limit") or 0)

        try:
            df, suspicious = sniffer.start_sniffing(interface=interface, timeout=duration, packet_count=packet_limit)
            total_packets = len(df)
            suspicious_ips = list(suspicious)
            df_html = df.head(50).to_html(classes="table table-striped", index=False) if not df.empty else None

            if not df.empty:
                protocol_counts = df["protocol"].value_counts()
                fig, ax = plt.subplots()
                ax.pie(protocol_counts, labels=protocol_counts.index, autopct="%1.1f%%")
                ax.set_title("Protocol Usage")
                chart_path = os.path.join("static", f"protocol_{int(time.time())}.png")
                fig.savefig(chart_path, bbox_inches="tight")
                plt.close(fig)

            # Save pcap
            pcap_fname = os.path.join(app.config['CAPTURE_FOLDER'], f"capture_{int(time.time())}.pcap")
            saved = sniffer.save_to_pcap(pcap_fname)
            if saved:
                latest_pcap_path = pcap_fname

        except Exception as e:
            
            error = str(e)

        return render_template("index.html", interfaces=interfaces, error=error, df=df_html, chart=chart_path,
                               total_packets=total_packets, suspicious_ips=suspicious_ips, duration=duration)

    # GET
    return render_template("index.html", interfaces=interfaces)


@app.route("/download")
def download():
    if latest_pcap_path and os.path.exists(latest_pcap_path):
        return send_file(latest_pcap_path, as_attachment=True)
    return redirect(url_for("index"))


if __name__ == "__main__":
    
    print("Starting Flask app. If you want to live-capture, run this script as Administrator and ensure Npcap is installed.")
    app.run(debug=True)
