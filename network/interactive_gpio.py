import network
import socket
import time
import os
from machine import Pin

specs = str(os.uname()[4])
state = "Ready"

# Wi-Fi 
ssid = "WIFI"
password = "PASSWD"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    print("Waiting for connection...")
    max_wait -= 1
    time.sleep(1)

if wlan.status() != 3:
    raise RuntimeError("Network connection failed")

print("Connected")
print("IP:", wlan.ifconfig()[0])

# HTML
html = f"""
<!DOCTYPE html>
<html>

<head>
    <title>MyPicoResume</title>
</head>

<body>
    <h1>Pico Playground</h1>
    <p>Device Information: {specs}</p>
    <p>Type the GPIO Number to trigger that specfic pin.<br></p>
    <form action="/toggle" method="GET">
    <input type="text" name="cmd" placeholder="GPIO Number">
    <input type="submit" value="Toggle LED">
    </form>
    <p>{state}</p>
    <p>This is an introduction to the Raspberry Pi Pico 2W using its networking abilites.</p>
    <h3>About Me</h3>
    <p> My name is Ritvik Sharma. I am Exploring software engineering internal systems, and low-level programming.</p>
</body>

</html>
"""

addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print("Listening on", addr)

while True:
    try:
        cl, client_addr = s.accept()
        print("Client connected from", client_addr)

        request = cl.recv(1024).decode()
        request_line = request.split("\r\n")[0]
        print("Request:", request_line)

        method, path, _ = request_line.split()
        route, _, query = path.partition("?")
        params = {}

        for pair in query.split("&"):
            if "=" in pair:
                k, v = pair.split("=", 1)
                params[k] = v
        
        if "cmd" in params:
            cmd = params["cmd"].strip().lower()
            
            if cmd == "led":
                pin = Pin("LED", Pin.OUT)
                pin.toggle()
                state = "On-board LED toggled"

            else:
                try:
                    gpio = int(cmd)

                    if gpio >= 0:
                        pin = Pin(gpio, Pin.OUT)
                        pin.toggle()
                        state = f"GPIO {gpio} toggled"
                    else:
                        state = "Invalid GPIO"

                except ValueError:
                    state = "Invalid command"

        else:
            state = "No command provided"

        

        response = html.format(state)

        cl.send(b"HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\n")
        cl.send(response.encode())

        cl.close()

    except OSError as e:
        print("Connection error:", e)
        cl.close()
