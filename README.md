# Traffic Generator

This tool simulates HTTP traffic targeting the honeypot.

## Custom Paths
To use custom paths for the traffic generator, create a `.txt` file where each line represents a path or query parameter.

Example (`paths.txt`):
```
/homepage
/information
/login
/api/data
/products
/about-us
/contact
/help
/search?q=honeypot
/documentation
```

Save your paths in `paths.txt` or another file of your choice. Specify the file using the `-f` or `--file` argument.

## Usage
Run the traffic generator with the following command:

```bash
python traffic_generator.py -H <host> -p <port> -i <interval> -f <path_to_file> -m <methods>
```

### Arguments:
- `-H` or `--host`: Target IP address (e.g., `192.168.1.10`).
- `-p` or `--port`: Target port (e.g., `8081`).
- `-m` or `--methods`: Specify the method (e.g., 'GET' or 'GET POST').
- `-i` or `--interval`: Interval between requests in seconds (default: `1.0`).
- `-f` or `--file`: Path to the file containing custom paths (default: `paths.txt`).
- `-v` or `--verbose`: Enable verbose mode.

### Example:
```bash
python traffic_generator.py -H 192.168.1.100 -p 8081 -i 0.5 -f custom_paths.txt -m GET
```
