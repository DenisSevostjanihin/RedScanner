import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from banner_grabber import grab_banner
from logger import setup_logger
import argparse

logger = setup_logger()

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((ip, port))
            banner = grab_banner(ip, port)
            msg = f"Port {port} is open"
            if banner:
                msg += f" | Banner: {banner}"
            print(f"[+] {msg}")
            logger.info(f"{ip}:{port} - OPEN - Banner: {banner if banner else 'N/A'}")
            return port, True
    except:
        # Порт закрыт — не выводим в консоль
        logger.info(f"{ip}:{port} - CLOSED")
        return port, False

def scan_target(ip, port_range, threads=100):
    open_ports = []

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(scan_port, ip, port): port for port in range(port_range[0], port_range[1] + 1)}
        for future in as_completed(futures):
            port, is_open = future.result()
            if is_open:
                open_ports.append(port)

    return open_ports

def main():
    parser = argparse.ArgumentParser(description="RedScanner - Port and Service Scanner")
    parser.add_argument("target", help="IP address or domain to scan")
    parser.add_argument("-s", "--start", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("-e", "--end", type=int, default=1024, help="End port (default: 1024)")
    parser.add_argument("-t", "--threads", type=int, default=100, help="Number of threads (default: 100)")

    args = parser.parse_args()

    print(f"Scanning {args.target} from port {args.start} to {args.end} with {args.threads} threads...")
    open_ports = scan_target(args.target, (args.start, args.end), args.threads)

    print("\nScan complete!")
    if open_ports:
        print(f"Open ports: {', '.join(map(str, sorted(open_ports)))}")
    else:
        print("No open ports found.")

if __name__ == "__main__":
    main()
