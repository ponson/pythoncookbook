prices = {
    'ACME' : '45.23',
    'AAPL' : '612.78',
    'IBM'  : '295.35',
    'HPQ' : '37.20',
    'FB' : '10.75'
}

prices_and_names = zip(prices.values(), prices.keys())
print(type(prices_and_names))
print(min(prices_and_names))
print(max(prices_and_names))