import requests
import datetime

# Obtener precio del Bitcoin
response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
price = response.json()["bitcoin"]["usd"]

# Guardar en un archivo
with open("prices.csv", "a") as f:
    f.write(f"{datetime.datetime.now()},{price}\n")