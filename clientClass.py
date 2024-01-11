import time
import requests
import os 

IP = "http://192.168.0.126:48763/"

while True:
    response = requests.get(IP,timeout=1)
    print(response.text)
    if response.text != "NULL":
        timestamp = time.perf_counter()
        with open(os.path.join(os.getcwd(), f"r.{timestamp}.txt"), "w") as file:
            file.write(response.text)
    time.sleep(1)
