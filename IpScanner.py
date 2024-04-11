import socket

target_ip = input('Place the Ip you want to scan here ex. 192.168.1.')

for i in range(1,255):
    ip = target_ip + str(i)
    try:
        host_name = socket.gethostbyaddr(ip)
        print(f"Host{ip} is active, hostname: {host_name[0]}")
    except socket.herror:
        pass
    except:
        print(f"Error occured while scanning {ip}")
        pass
    else:
        print(f"No hostname found for {ip}")
        print(f"Host {ip} is active")
    print(f"Host {ip} is inactive")
