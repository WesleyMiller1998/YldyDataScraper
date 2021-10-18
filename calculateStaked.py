import requests
import models

models.create_database()

assetid = 226701642
aid = 233725844
yid = 233725850

accounts = models.fetch_accounts()

total = len(accounts)

for count, account in enumerate(accounts):
    print(f"Checking account {count + 1} of {total}")
    url = f"https://algoexplorerapi.io/idx2/v2/accounts/{account[0]}"
    r = requests.get(url)
    data = r.json()

    models.set_algo_in_account(account[0], data["account"]["amount"])

    if "apps-local-state" in data["account"]:
        for app in data["account"]["apps-local-state"]:
            if app["id"] == yid and "key-value" in app:
                for count, vals in enumerate(app["key-value"]):
                    if vals["key"] == "VUE=":
                        models.set_yldy_staked(
                            account[0], vals["value"]["uint"])
                        break
            if app["id"] == aid and "key-value" in app:
                for count, vals in enumerate(app["key-value"]):
                    if vals["key"] == "VUE=":
                        models.set_algo_staked(
                            account[0], vals["value"]["uint"])
                        break
