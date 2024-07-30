import nmap

def scan_network(network):
    nm = nmap.PortScanner()
    nm.scan(hosts=network, arguments='-sP')
    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
    for host, status in hosts_list:
        print(f'Host: {host} - Status: {status}')

if __name__ == "__main__":
    network = '192.168.1.0/24'  # Replace with your network
    scan_network(network)