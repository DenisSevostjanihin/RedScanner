import socket

def grab_banner(ip, port):
    try:
        with socket.socket() as s:
            s.settimeout(2)
            s.connect((ip, port))
            banner = s.recv(1024)
            return banner.decode(errors="ignore").strip()
    except:
        return None
