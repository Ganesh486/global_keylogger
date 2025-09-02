## Project Overview

This project demonstrates how attackers can use a keylogger to capture system and network information, and then exfiltrate keystrokes to a remote server.

It is built as a controlled cybersecurity lab project for Semester 3 to help understand:

How keyloggers operate.

How data exfiltration works via sockets.

How defenders can detect and mitigate such attacks.

## Features

Collects System Information (OS, CPU, RAM, Hostname).

Collects Network Information (IP address, hostname).

Captures Keystrokes using pynput.

Sends keystrokes to a remote server via sockets.

Server can run locally or be exposed globally with ngrok.

## Requirements

Install dependencies:

pip install pynput psutil

## Project Structure
.
├── server.py   # Server script (receives keystrokes)
├── client.py   # Client keylogger (sends keystrokes)
├── README.md   # Project documentation

# Usage
1. Run the Server
python3 server.py

2. (Optional) Expose with Ngrok
ngrok tcp 4444


You will get a forwarding address like:

tcp://0.tcp.ngrok.io:12345

3. Run the Client

Edit client.py and update with your server/port:

SERVER_IP = "0.tcp.ngrok.io"
SERVER_PORT = 12345


Then run:

python3 client.py

4. View Logs

Keystrokes typed on the client machine will appear on the server console.

🖼 Architecture
[Client Keylogger] --(keystrokes)--> [Server Listener] --(ngrok)--> [Researcher/Admin]

Cybersecurity Learning Points

Offensive View:
Demonstrates how attackers capture and transmit sensitive data.

Defensive View:

Monitor unusual outbound traffic.

Use Intrusion Detection Systems (Snort/Zeek/Suricata).

Employ endpoint detection to block unauthorized keyloggers.

Awareness & training for end-users.

## References

Pynput Documentation

Psutil System Info

Ngrok Official

Stallings, W. (2018). Computer Security: Principles and Practice. Pearson.

OWASP Keylogger Prevention Guide

✅ Now you can push this with your code on GitHub.
