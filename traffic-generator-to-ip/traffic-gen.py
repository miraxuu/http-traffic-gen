import argparse
import random
import time
from scapy.all import IP, TCP, send
from scapy.layers.http import HTTP, HTTPRequest

def load_paths_from_file(file_path):
    """Load paths from a text file."""
    try:
        with open(file_path, "r") as file:
            paths = [line.strip() for line in file if line.strip()]
        return paths
    except FileNotFoundError:
        print(f"Error: File {file_path} not found. Using default paths.")
        return ["/default"]

def generate_http_traffic(host, port, paths, interval):
    """Generate random HTTP traffic."""
    # Define HTTP methods and User-Agent headers
    methods = ["GET", "POST", "PUT", "DELETE"]
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)"
    ]

    print(f"Sending HTTP traffic to {host}:{port} every {interval} seconds...")

    while True:
        # Randomly select an HTTP method, path, and User-Agent
        method = random.choice(methods)
        path = random.choice(paths)
        user_agent = random.choice(user_agents)

        # Create and send the HTTP packet
        packet = (
            IP(dst=host) /
            TCP(dport=port, sport=random.randint(1024, 65535)) /
            HTTP() /
            HTTPRequest(
                Method=method.encode(),
                Path=path.encode(),
                Host=host.encode()
            )
        )

        # Display the simulated traffic
        print(f"Generated {method} request to {path} with User-Agent: {user_agent}")
        send(packet, verbose=False)

        # Wait for the specified interval
        time.sleep(interval)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate random HTTP traffic to a target.")
    parser.add_argument("-H", "--host", required=True, help="Target host IP or domain.")
    parser.add_argument("-p", "--port", type=int, required=True, help="Target port.")
    parser.add_argument("-i", "--interval", type=float, default=1.0, help="Interval between requests (in seconds).")
    parser.add_argument("-f", "--file", type=str, default="paths.txt", help="Path to the file containing HTTP paths.")

    args = parser.parse_args()

    # Load paths from file
    paths = load_paths_from_file(args.file)

    try:
        generate_http_traffic(args.host, args.port, paths, args.interval)
    except KeyboardInterrupt:
        print("\nTraffic generation stopped.")
