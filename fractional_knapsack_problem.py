def fractional_knapsack(price, price_wt, capacity):
    n = len(price)
    items = [(price[i], price_wt[i], price[i] / price_wt[i]) for i in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            if items[i][2] < items[j][2]:
                items[i], items[j] = items[j], items[i]

    profit = 0.0

    for item_price, item_wt, perKgPrice in items:
        if capacity >= item_wt:
            capacity -= item_wt
            profit += item_price
        else:
            profit += capacity * perKgPrice
            break

    print("Total Profit =", profit)


price = [24, 21, 12, 10]
price_wt = [7, 3, 4, 5]

capacity = int(input("inter the kncapsack wait :"))

fractional_knapsack(price, price_wt, capacity)
