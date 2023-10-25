import adafruit_dht
import time
import board
import psutil
import requests

for proc in psutil.process_iter():
        if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
                proc.kill()

sensor = adafruit_dht.DHT11(board.D23, use_pulseio=True)

while True:
        try:
                temp = sensor.temperature
                humidity = sensor.humidity
                print("Temperature: {}*C \nHumidity: {}%".format(temp, humidity))
								#url = "http://192.168.50.200/api/send-measurements"
								url = http://monserveur.fr/api/send-measurements
                data = {'temp' : temp, 'humidity' : humidity}
                req = requests.post(url, json=data)
                print("Envoi des donnees par requete http au serveur")
                time.sleep(5)
        except RuntimeError as error:
                print(error.args[0])
                time.sleep(20)
                continue
        except Exception as error:
                sensor.exit()
                raise error
time.sleep(3)
