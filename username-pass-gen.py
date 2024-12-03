import requests
import random
import string
import time
import sys

# List of legitimate-sounding usernames
usernames = [
    "alex_jordan", "amanda_clark", "andrew_cooper", "anna_harrison", "ben_taylor",
    "brian_lewis", "claire_morgan", "daniel_scott", "diana_hughes", "eric_evans",
    "eva_martinez", "george_roberts", "grace_anderson", "hannah_hall", "helen_carter",
    "jacob_king", "james_howard", "jason_thomas", "jennifer_moore", "joseph_wright",
    "joshua_turner", "julia_phillips", "karen_campbell", "kevin_mitchell", "kyle_hill",
    "laura_allen", "linda_torres", "lisa_baker", "mark_adams", "matthew_peterson",
    "megan_parker", "melissa_hayes", "michael_collins", "michelle_ward", "nathan_james",
    "nicole_morgan", "olivia_kelly", "patrick_hunter", "paul_bennett", "rachel_simmons",
    "rebecca_foster", "richard_reed", "robert_bryant", "samantha_bell", "sean_morris",
    "stephanie_cox", "steven_harris", "thomas_fisher", "victoria_ellis", "william_grant"
]


# List of dictionary words to include in passwords
dictionary_words = [
    "bear", "blaze", "canyon", "cloud", "comet", "coral", "crystal", "eagle", "ember", "falcon",
    "flame", "frost", "galaxy", "glacier", "hawk", "horizon", "ivy", "jaguar", "jade", "lava",
    "lightning", "lotus", "lynx", "meadow", "meteor", "mist", "moon", "moss", "nebula", "ocean",
    "onyx", "orchid", "otter", "pearl", "phoenix", "pine", "raven", "reef", "river", "shadow",
    "sky", "snow", "sparrow", "starlight", "storm", "stream", "thunder", "twilight", "willow", "wolf"
]


def generate_random_password():
    """Generate a random password with dictionary words and numbers."""
    word = random.choice(dictionary_words)  # Pick a random word from the dictionary
    number = ''.join(random.choices(string.digits, k=random.randint(2, 4)))  # Random number
    extra_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 3)))  # Extra characters
    password = word + number + extra_chars
    return password

def send_requests():
    """Send continuous GET requests with random usernames and passwords."""
    url = f"http://{target_ip}:{target_port}"
    while True:
        username = random.choice(usernames)
        password = generate_random_password()
        params = {"username": username, "password": password}
        try:
            response = requests.get(url, params=params)
            print(f"Sent request: {params}, Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error sending request: {e}")
        time.sleep(2)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python username-pass-gen.py <IP> <PORT>")
        sys.exit(1)

    target_ip = sys.argv[1]
    target_port = sys.argv[2]

    send_requests()
