import time
import json

with open("/var/www/html/televie/score.json", "r+") as f:
  data = json.loads(f.read())

  if data is not None:
    data["value"] = 0
    f.seek(0)  # rewind
    f.write(json.dumps(data))
    f.truncate()

print("Score reset")

time.sleep(3)
