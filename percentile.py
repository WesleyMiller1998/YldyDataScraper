import models

percentiles = [.25, .5, .75, .9, .95, .99]

top = models.fetch_yldy_greater_than(1)
total = models.sum_staked_yldy()

for percentile in percentiles:
    current = 0

    for count, account in enumerate(top):
        if account[4] is not None:
            current += account[4]

        if current / total >= percentile:
            print(f"{count} hold {percentile * 100}% of staked yieldly")
            break
