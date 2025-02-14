from flask import Flask, jsonify
from scapy.all import sniff, IP, TCP, UDP
import threading
import time
import collections

app = Flask(__name__)

packet_list = []
metrics = {
    "packets_per_second": 0,
    "top_source_ips": {},
    "top_dest_ips": {},
    "protocol_counts": {"TCP": 0, "UDP": 0, "Other": 0},
    "most_used_ports": {},
    "average_packet_size": 0,
}

last_timestamp = time.time()
packet_count = 0
total_packet_size = 0

def packet_handler(packet):
    global last_timestamp, packet_count, total_packet_size

    if packet.haslayer(IP):  
        protocol = "TCP" if packet.haslayer(TCP) else "UDP" if packet.haslayer(UDP) else "Other"
        packet_size = len(packet)
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        # Extract ports if available
        src_port = packet[TCP].sport if packet.haslayer(TCP) else (packet[UDP].sport if packet.haslayer(UDP) else None)
        dst_port = packet[TCP].dport if packet.haslayer(TCP) else (packet[UDP].dport if packet.haslayer(UDP) else None)

        # Update global stats
        packet_count += 1
        total_packet_size += packet_size

        # Track protocol distribution
        metrics["protocol_counts"][protocol] += 1

        # Track source and destination IPs
        metrics["top_source_ips"][src_ip] = metrics["top_source_ips"].get(src_ip, 0) + 1
        metrics["top_dest_ips"][dst_ip] = metrics["top_dest_ips"].get(dst_ip, 0) + 1

        # Track most used ports
        if src_port:
            metrics["most_used_ports"][src_port] = metrics["most_used_ports"].get(src_port, 0) + 1
        if dst_port:
            metrics["most_used_ports"][dst_port] = metrics["most_used_ports"].get(dst_port, 0) + 1

        # Compute packets per second
        current_time = time.time()
        elapsed_time = current_time - last_timestamp
        if elapsed_time >= 1:
            metrics["packets_per_second"] = packet_count / elapsed_time
            last_timestamp = current_time
            packet_count = 0

        # Compute average packet size
        if len(packet_list) > 0:
            metrics["average_packet_size"] = total_packet_size / len(packet_list)

        # Store packet data
        packet_data = {
            "src_ip": src_ip,
            "dst_ip": dst_ip,
            "protocol": protocol,
            "packet_size": packet_size,
        }
        packet_list.append(packet_data)
        if len(packet_list) > 100:
            packet_list.pop(0)

def start_sniffing():
    sniff(filter="ip", prn=packet_handler, store=False)

# Start packet sniffing in a separate thread
threading.Thread(target=start_sniffing, daemon=True).start()

@app.route("/packets")
def get_packets():
    return jsonify(packet_list)

@app.route("/metrics")
def get_metrics():
    return jsonify(metrics)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
