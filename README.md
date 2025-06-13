# RC Car Control System (Raspberry Pi Pico W + Python)

This project provides a complete system for controlling RC cars over Wi-Fi using Raspberry Pi Pico W microcontrollers. Each car is configured individually, connects to a shared wireless network, and is controlled from a host computer using real-time keyboard input.

## 🚗 Project Components

### 🧠 On the RC Car (Pico W):
- Reads PWM config from `config.json`
- Connects to Wi-Fi using `networkinfo.json`
- Listens for HTTP control commands (`/api?cmd=...&turn=...`)
- Drives an ESC (motor) and servo (steering) using MicroPython

### 💻 On the Control Host (Mac or PC):
- `control_rc_car.py` script
- Sends commands via HTTP using WASD keyboard input
- Uses `.local` mDNS hostnames for multi-car control

---

## 📦 File Structure
rc-car-control/
├── main.py               # Pico W control script
├── control_rc_car.py     # Mac/PC keyboard controller
├── config.json           # Pico hardware & hostname config
├── networkinfo.json      # Pico Wi-Fi credentials
├── requirements.txt      # Python dependencies for host control
└── README.md             # You’re here

---

## 🛠️ Setup Instructions

### 🔧 1. Flashing the Pico W

1. Flash MicroPython to the Pico W (https://micropython.org/download/rp2-pico-w/)
2. Use [Thonny](https://thonny.org/) to connect to the Pico
3. Upload `main.py`, `config.json`, and `networkinfo.json`
4. Save `main.py` directly on the Pico (not your computer)

### 📡 2. Configuring Wi-Fi and Hostname

Example `config.json` (on the Pico):
```json
{
  "hostname": "rc1",
  "esc_pin": 16,
  "servo_pin": 17
}


Example `networkinfo.json` (on the Pico and the computer):
```json
{
  "SSID": "YourWiFiNetwork",
  "PASSWORD": "YourWiFiPassword"
}

⌨️ 3. Running the Host Control Script

Install dependencies:
```bash
pip install -r requirements.txt

Run the control script:
```bash
python control_rc_car.py

You can now control the car using:
	•	W = Forward
	•	S = Stop
	•	A/D = Left/Right steering

---

🚙 Multi-Car Setup

You can run multiple RC cars simultaneously on the same network by:
	1.	Giving each car a unique hostname in its config.json (e.g., rc1, rc2, rc3, …)
	2.	Updating your control script to point to different cars via hostname (rc2.local, etc.)

---

🧪 Testing
	•	Press W while connected to verify motor spin
	•	Watch onboard LED:
	•	Fast blink while connecting to Wi-Fi
	•	Solid once connected
	•	Use ping `rc1.local` to test mDNS resolution

---

📋 Requirements
	•	Raspberry Pi Pico W
	•	GoolRC ESC + Brushless Motor
	•	Servo motor (3-wire)
	•	URGENEX 7.4V 2000mAh battery
	•	Python 3.9+ on control host

---

🤝 Contributing
	1.	Fork the repo
	2.	Create a feature branch (git checkout -b feature/my-feature)
	3.	Commit changes and push
	4.	Open a pull request
