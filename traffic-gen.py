import argparse
import random
import time
import requests


def generate_traffic(host, port, interval, methods, paths, verbose):
    print(f"Sending traffic to {host}:{port} every {interval} seconds...")

    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)"
    ]

    while True:
        # Randomly select a method, path, and User-Agent
        method = random.choice(methods)
        path = random.choice(paths)
        user_agent = random.choice(user_agents)

        # Construct the URL
        url = f"http://{host}:{port}{path}"

        headers = {"User-Agent": user_agent}

        try:
            if method == "GET":
                requests.get(url, headers=headers)
            elif method == "POST":
                requests.post(url, headers=headers, data={"key": "value"})
            elif method == "PUT":
                requests.put(url, headers=headers, data={"key": "value"})
            elif method == "DELETE":
                requests.delete(url, headers=headers)

            if verbose:
                print(f"Sent {method} request to {url} with User-Agent: {user_agent}")

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

        # Wait for the specified interval
        time.sleep(interval)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate benign HTTP traffic to a target host and port.")
    parser.add_argument("-H", "--host", required=True, help="Target host IP or domain.")
    parser.add_argument("-p", "--port", type=int, required=True, help="Target port number.")
    parser.add_argument("-i", "--interval", type=float, default=1.0, help="Interval between requests (in seconds).")
    parser.add_argument("-m", "--methods", nargs="+", default=["GET", "POST", "PUT", "DELETE"],
                        help="HTTP methods to use (default: all methods).")
    parser.add_argument("-f", "--paths_file", type=str, default="paths.txt",
                        help="Path to the file containing URL paths.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output for debugging.")

    args = parser.parse_args()

    # Load paths from file
    try:
        with open(args.paths_file, "r") as file:
            paths = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: File {args.paths_file} not found.")
        exit(1)

    try:
        generate_traffic(args.host, args.port, args.interval, args.methods, paths, args.verbose)
    except KeyboardInterrupt:
        print("\nTraffic generation stopped.")
