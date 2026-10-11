#!/usr/bin/python3
import subprocess

# List visible Wi-Fi networks in Linux
profiles = subprocess.check_output("nmcli -t -f SSID dev wifi", shell=True).decode()
ssids = list(dict.fromkeys([line for line in profiles.split("\n") if line]))

for i, ssid in enumerate(ssids, 1):
    print(f"[{i}] {ssid}")

ch = int(input("\nChoose WiFi number: "))
wifi = ssids[ch - 1]

# Display details/saved key for the connection
try:
    result = subprocess.check_output(f'sudo nmcli -s -g 802-11-wireless-security.psk connection show "{wifi}"', shell=True).decode()
    print("\nPassword: " + result)
except Exception as e:
    print("\nCould not retrieve password:", e)#!/usr/bin/python3

