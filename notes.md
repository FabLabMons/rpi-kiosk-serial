# Create a service

## Start the editor
sudo systemctl --force --full edit <myscript>.service

## Copy/edit this content to the file
[Unit]
Description=My script to monitor the serial port
After=multi-user.target

[Service]
WorkingDirectory=/home/<user>/
User=<user>
ExecStart=/usr/bin/python3 /home/<user>/<script.py>

[Install]
WantedBy=multi-user.target

# Enable the script
sudo systemctl enable --now <myscript>.service

# Check service status
systemctl status <myscript>.service

# (Optional) Check the script output (like print(), etc.)
journalctl -b -e

(subject to dynamic change)
shell access: CTRL-ALT-F1
desktop: CTRL-ALT-F7

# If using RpiOS Desktop
## Configure autostart to show localhost in Chromium web browser at login
`sudo nano /etc/xdg/lxsession/LXDE-pi/autostart`

## Add the following line
`@chromium-browser www.raspberrypi.org`

source: https://forums.raspberrypi.com/viewtopic.php?t=294014
