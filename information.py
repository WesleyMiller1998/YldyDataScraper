import models
import csv

top = models.fetch_yldy_greater_than(1)
totals = [0, 0, 0, 0]

file = open("yldyData.csv", "w+", newline="")
write = csv.writer(file)
write.writerow(["Address", "ALGO in wallet", "YLDY in wallet",
                "ALGO staked", "YLDY staked"])

for account in top:
    if account[1] is not None:
        totals[0] += account[1]
    if account[2] is not None:
        totals[1] += account[2]
    if account[3] is not None:
        totals[2] += account[3]
    if account[4] is not None:
        totals[3] += account[4]
    write.writerow([account[0],
                    account[1] / 1000000 if account[1] is not None else 0,
                    account[2] / 1000000 if account[2] is not None else 0,
                    account[3] / 1000000 if account[3] is not None else 0,
                    account[4] / 1000000 if account[4] is not None else 0])

print(
    f"Totals: \n ALGO: {totals[0] / 1000000}; YLDY: {totals[1] / 1000000}; ALGO Staked: {totals[2] / 1000000}; YLDY Staked: {totals[3] / 1000000}")

write.writerow(["Total: ", totals[0] / 1000000, totals[1] / 1000000,
                totals[2] / 1000000, totals[3] / 1000000])
