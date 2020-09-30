import pyshark
cap = pyshark.FileCapture('http.cap', keep_packets=False)
def print_info_layer(packet): 
    print("[Protocol:] " + packet.highest_layer + " [Source IP:] " + packet.ip.src + " [ Destination IP:]")

cap.apply_on_packets(print_info_layer)

