import requests
import models

models.create_database()

assetid = 226701642
payload = {}  # {"currency-greater-than": 0}

url = f"https://algoexplorerapi.io/idx2/v2/assets/{assetid}/balances"

r = requests.get(url, params=payload)
data = r.json()

num_accounts = 0

while "next-token" in data:
    models.insert_yldy_balances(data["balances"])
    num_accounts += len(data["balances"])
    print(f"{num_accounts} finished")

    payload["next"] = data["next-token"]
    r = requests.get(url, params=payload)
    data = r.json()

models.insert_yldy_balances(data["balances"])
print(models.num_accounts())
