"""
RC Car Keyboard Controller (Desktop Python)

This script runs on your local computer and listens for
WASD keyboard input to control a Raspberry Pi Pico W–powered RC car over Wi-Fi.

Each key press sends an HTTP GET request to the car's API, using the car's
hostname defined in a local `config.json` file.

Keys:
    W → Forward
    A → Turn left
    D → Turn right
    S → Stop (and center steering)

Configuration File:
- config.json: contains "hostname" for the target RC car

Authors: Kevin Thompson, Aidan McMillan
Date: 2025-07-23
"""

import keyboard
import requests
import time
import json
import socket
from typing import Optional

def load_config() -> dict:
    """Loads the control configuration from a local JSON file.
    
    Returns:
        Dictionary containing config values (e.g., hostname).
    """
    with open("config.json") as f:
        return json.load(f)

cfg = load_config()
SSID: str = cfg.get("SSID")
PICO_IP: str = "10.10.20.63"
DEBOUNCE_MS: int = 50

print(socket.gethostbyname(PICO_IP))

def send_command(command: str) -> None:
    """Sends a command to the RC car's API endpoint over HTTP.
    
    Args:
        command: Query string in the format "cmd=forward&turn=left"
    """
    url = f"http://{PICO_IP}/api?{command}"
    try:
        response = requests.get(url, timeout=10)
        print(f"Sent: {command} | Status: {response.status_code}")
    except Exception as e:
        print(f"Failed to send: {command} | Error: {e}")

def main() -> None:
    """Main control loop: monitors keyboard and sends commands to the Pico W."""
    last_command = None

    print("Keyboard RC Control Started")
    print("Hold W = forward, A/D = steer, S = back")

    while True:
        drive_command = 'stop'
        turn_command = 'center'

        if keyboard.is_pressed('w'):
            drive_command = "forward"
        elif keyboard.is_pressed('s'):
            drive_command = "back"
        
        if keyboard.is_pressed('a'):
            turn_command = "left"
        elif keyboard.is_pressed('d'):
            turn_command = "right"
        
        full_command = f"cmd={drive_command}&turn={turn_command}"

        if full_command != last_command:
            send_command(full_command)
            last_command = full_command
        
        time.sleep(DEBOUNCE_MS / 1000)

if __name__ == "__main__":
    main()
