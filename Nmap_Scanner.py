import nmap
import ipaddress

scanner = nmap.PortScanner()

print("This is a simple port scanner by A&k")
print("___________________________________________________")

ip_addr = input("Enter IP address you want to scan: ")
try: 
    print("The Ip address you entered is : ", ipaddress.ip_address(ip_addr))
    resp = input("""Enter which type of scan you want to perform
                1) SYN-ACK Scan
                2) UDP Scan
                3) Comprehensive Scan
             : """)
   
    if resp == '1' :
        print("Loading.......")
        print("Nmap Version", scanner.nmap_version())
        scanner.scan(ip_addr, '1-1024','-v -sS')
        
        print(scanner.scaninfo())
        
        ip_stat = scanner[ip_addr].state()
        print("IP Status: ", ip_stat)
        
        if ip_stat == 'up' :

            protocol = scanner[ip_addr].all_protocols()
            if protocol == []:
                print("There is no protocol in use")
                print("There is no open ports in scanned ip address")
            else:
                print("Protocol in use: ",end="")
                for i in protocol :
                    print(i,end=" ")

                ports = scanner[ip_addr]['tcp'].keys()
                print("\nOpen Ports: ", end="")
                for i in ports:
                    print(i,end=" ")

        else : 
            print("This",ip_addr,"is down and not reachable")

    elif resp == '2' :
        print("Loading.......")
        print("Nmap Version", scanner.nmap_version())
        scanner.scan(ip_addr, '137','-sU')
        
        print("Loading........")
        print(scanner.scaninfo())
        
        ip_stat = scanner[ip_addr].state()
        print("IP Status: ", ip_stat)
        
        if ip_stat == 'up' :

            protocol = scanner[ip_addr].all_protocols()
            if protocol == []:
                print("There is no protocol in use")
                print("There is no open ports in scanned ip address")
            else:
                print("Protocol in use: ",end="")
                for i in protocol :
                    print(i,end=" ")

                por = scanner[ip_addr]['udp'].keys()
                print("\nOpen Ports: ", end="")
                for i in por:
                    print(i,end=" ")
        else : 
            print("This",ip_addr,"is down and not reachable")

    elif resp == '3' :
        print("Loading.......")
        print("Nmap Version", scanner.nmap_version())
        scanner.scan(ip_addr, '10','-v -sS -sV -sC -A -O')
        
        print(scanner.scaninfo())
        
        ip_stat = scanner[ip_addr].state()
        print("IP Status: ", ip_stat)
        
        if ip_stat == 'up' :

            protocol = scanner[ip_addr].all_protocols()
            if protocol == []:
                print("There is no protocol in use")
                print("There is no open ports in scanned ip address")
            else:
                print("Protocol in use: ",end="")
                for i in protocol :
                    print(i,end=" ")

                ports = scanner[ip_addr]['tcp'].keys()
                print("\nOpen Ports: ", end="")
                for i in ports:
                    print(i,end=" ")

            host_name = scanner[ip_addr].items()
            print("HostName",host_name)

        else : 
            print("This",ip_addr,"is down and not reachable")

except ValueError:
    print("You have entered an invalid IP address")