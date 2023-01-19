# Raspberry Pi Kiosk Sample
This project is a simple kiosk/serial sample project which shows a value on a web page, taken from a `json` file. This value is increased when we receive any value on the serial port.

## Description
We have a serial device which sends a line of data whenever it wants. We listen to this device and count every line of data we receive.
The counter is initialized by the script `init.py`. To listen to the serial port, we use `connect.py`.
For convenience, a service is created to run this script when the RPi is started (see notes.md to set up the service).
We use RPiOS desktop to have all required stuff for the kiosk mode built-in.

## Setup
1. Set up a RPi with the desktop image and do the basic configuration as advised by this guide https://www.raspberrypi.com/documentation/computers/getting-started.html
2. Copy the Python file to the home directory (`service/init.py` and `service/connect.py`)
3. Create a directory which will contain the web page files and copy the files from `web` directory there.
4. Configure autostart to show localhost in Chromium web browser at login:
    1. `sudo nano /etc/xdg/lxsession/LXDE-pi/autostart`
    2. Add the following line: `@chromium-browser localhost/path/to/index.html`
5. Create the service to automatically connect to the serial port
    1. `sudo systemctl --force --full edit <myscript>.service`
    2. Copy the content of the code snippet in appendix a. into this file
    3. Enable the script: `sudo systemctl enable --now <myscript>.service`
    4. Check service status: `systemctl status <myscript>.service`
    5. (Optional) Check the script output (like print(), etc.): `journalctl -b -e`
  
## Appendix
### a. Service file contents
  ```
  [Unit]
  Description=My script to monitor the serial port
  After=multi-user.target

  [Service]
  WorkingDirectory=/home/<user>/
  User=<user>
  ExecStart=/usr/bin/python3 /home/<user>/connect.py

  [Install]
  WantedBy=multi-user.target
  ```
