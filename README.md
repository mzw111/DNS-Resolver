# DNS-Resolver

# Custom DNS Resolver

This project is a custom DNS resolver built in Python, designed to resolve domain names into their corresponding A records (IPv4 addresses). It features a core resolver library that attempts to build and send raw DNS packets, and a user-friendly command-line interface to run queries.

## 🚀 Features

* **Flexible Input:** Resolve domains passed as command-line arguments or via an interactive prompt.
* **Raw Socket Resolution:** On Linux systems, the resolver attempts to craft and send DNS packets from scratch using `AF_PACKET` raw sockets.
* **Fallback Mechanism:** Gracefully falls back to standard OS-level DNS resolution on systems that do not support this (e.g., Windows), or if raw socket creation fails.
* **Detailed Debugging:** Includes a `debug` flag to print detailed, step-by-step logs of the resolution process.
* **Simple Caching:** Caches results to avoid re-resolving the same domain within its TTL.

## 📦 Installation

1.  Clone this repository to your local machine.
2.  It is highly recommended to use a Python virtual environment.
    ```bash
    # Create a virtual environment
    python3 -m venv venv
    
    # Activate it
    # On macOS/Linux:
    source venv/bin/activate
    # On Windows:
    .\venv\Scripts\activate
    ```
3.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## 🖥️ How to Run

The `dnsresolver.py` script requires elevated privileges to create raw sockets.

* **On Linux/macOS:** You must run the script with `sudo`.
* **On Windows:** You must run your Command Prompt or PowerShell **as Administrator**.

There are two ways to run the script:

### 1. Interactive Mode

Run the script without any arguments to be prompted for input.

```bash
# On Linux/macOS
sudo python3 specificdomain.py

# On Windows (as Admin)
python specificdomain.py
```

It will then ask you for domains:
```
Enter the domain(s) to resolve, separated by spaces: google.com cloudflare.com
```

### 2. Argument Mode

Pass the domains you want to resolve directly as command-line arguments.

```bash
# On Linux/macOS
sudo python3 specificdomain.py youtube.com github.com

# On Windows (as Admin)
python specificdomain.py wikipedia.org
```
---
### ## Example Output (on Windows)

When running on Windows, the resolver will automatically detect that it cannot create raw sockets and will use the standard OS-level fallback. This is expected behavior.

```
PS C:\dns-project> python specificdomain.py youtube.com
DNS Resolution Results:
--------------------------------------------------

Resolving youtube.com...
Resolving domain: youtube.com
Raw socket creation failed (this is expected on Windows): module 'socket' has no attribute 'AF_PACKET'
Raw socket not available, using standard DNS
Using standard socket DNS resolution for youtube.com
Cached result for youtube.com with TTL 3600
✓ Successfully resolved youtube.com:
  - youtube.com -> 172.217.24.174 (TTL: 3600s)

DNS resolver closed
```

## 🛠️ How It Works

This project is split into two main files:

* `dnsresolver.py`: This is the core library. The `DNSResolver` class handles all the logic for socket creation (both raw and standard), building DNS query packets, sending/receiving data, parsing the raw byte responses, and caching results.
* `specificdomain.py`: This is the user-facing client. It handles parsing user input (from `sys.argv` or `input()`), imports the `DNSResolver` class, calls the `.resolve()` method for each domain, and prints the results in a human-readable format.
