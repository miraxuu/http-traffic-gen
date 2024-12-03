import random
import requests
import sys
import time

# Sample tables, columns, and data for SQL queries
tables = ["thread", "held", "clothes", "main", "throat", "balloon", "write", "chair", "boy", "particular", "current", "won", "motor", "rest", "door", "tomorrow", "west", "breath", "race"]
columns = ["eleven", "continued", "imagine", "furniture", "dear", "adventure", "nearby", "cake", "climate", "nation", "answer", "action", "pictured", "disease", "end", "screen", "goose", "offer", "slabs", "tomorrow", "speak", "plastic", "upper", "burst", "known", "city", "dust", "traffic", "east", "grow", "wide", "slide"]
values = ["worse", "balloon", "many", "badly", "deal", "table", "atomic", "idea", "likely", "donkey", "land", "scene", "course", "exact", "particularly", "scene", "prepare", "terrible", "far", "species", "tobacco", "small", "null", "not null", "tomorrow", "race"]

# Randomly generate SQL query types
query_types = ["SELECT", "INSERT", "UPDATE", "DELETE"]

def generate_random_query():
    """Generate a random SQL query."""
    query_type = random.choice(query_types)
    if query_type == "SELECT":
        table = random.choice(tables)
        columns_selected = random.choices(columns, k=random.randint(1, 3))
        condition = f"{random.choice(columns)} = '{random.choice(values)}'" if random.random() > 0.5 else ""
        order_by = f"ORDER BY {random.choice(columns)} {random.choice(['ASC', 'DESC'])}" if random.random() > 0.7 else ""
        return f"SELECT {', '.join(columns_selected)} FROM {table} {f'WHERE {condition}' if condition else ''} {order_by}".strip()
    elif query_type == "INSERT":
        table = random.choice(tables)
        columns_selected = random.choices(columns, k=random.randint(2, 5))
        values_selected = random.choices(values, k=len(columns_selected))
        values_formatted = ', '.join([f"'{v}'" for v in values_selected])
        return f"INSERT INTO {table} ({', '.join(columns_selected)}) VALUES ({values_formatted})"
    elif query_type == "UPDATE":
        table = random.choice(tables)
        set_clause = f"{random.choice(columns)} = '{random.choice(values)}'"
        condition = f"{random.choice(columns)} = '{random.choice(values)}'"
        return f"UPDATE {table} SET {set_clause} WHERE {condition}"
    elif query_type == "DELETE":
        table = random.choice(tables)
        condition = f"{random.choice(columns)} = '{random.choice(values)}'" if random.random() > 0.5 else ""
        return f"DELETE FROM {table} {f'WHERE {condition}' if condition else ''}"

def send_get_request(ip, port):
    """Send random SQL queries as GET requests to the specified IP and port."""
    base_url = f"http://{ip}:{port}"
    try:
        while True:
            query = generate_random_query()
            params = {"query": query}
            try:
                response = requests.get(base_url, params=params)
                print(f"Sent query: {query}, Status Code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Error sending request: {e}")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nStopped sending queries.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python sql_query_gen.py <IP> <PORT>")
        sys.exit(1)

    target_ip = sys.argv[1]
    target_port = sys.argv[2]

    send_get_request(target_ip, target_port)
