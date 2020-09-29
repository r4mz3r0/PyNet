import pyshark 
cap = pyshark.FileCapture('http.cap', display_filter="dns")
for pkt in cap: 
    print(pkt.highest_layer) 
