"""stock_price = []
with open("stock_price.csv","r") as f :
    for line in f:
        token = line.split(',')
        day = token[0]
        price = float(token[1])
        stock_price.append([day,price])
print(stock_price)
"""

stock_price = {}
with open("stock_price.csv","r") as f :
    for line in f:
        token = line.split(',')
        day = token[0]
        price = float(token[1])
        stock_price[day] = price 
print(stock_price["March 1"])

