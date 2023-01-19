import serial
import time
import json

print("Waiting for serial port to open...")

ser = serial.Serial ("/dev/ttyUSB0")
# ser.timeout = 20

# Wait for serial port to be ready
while ser.is_open == False:
  time.sleep(1)

print("Serial port ready!")

while True:
  size = ser.inWaiting()

  if size:
    rawData = ser.read(size)
    data = rawData.decode("ascii").rstrip("\r\n")
    print(data)

    with open("/var/www/html/televie/score.json", "r+") as f:
      data = json.loads(f.read())

      if data is not None:
        score = int(data["value"]) + 1
        data["value"] = score
        f.seek(0)  # rewind
        f.write(json.dumps(data))
        f.truncate()

  # Software debounce (serial device is a mechanical switch which is not hardware debounced)
  time.sleep(1)

ser.close()
