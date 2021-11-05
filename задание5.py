def show_price(items, show_delim=True):
    for price in items:
        price = int(round(price * 100))
        rubles = price // 100
        cent = price % 100
        print(f'{rubles:02d} руб {cent:02d} коп', end=',')
    if show_delim:
        print()

prices = [89.2, 25.21, 65.45, 48.5, 48, 97.78, 78.15, 87.7, 98.25, 34.5]
show_price(prices)
prices.sort()
show_price(prices)
prices_desc = sorted(prices, reverse=True)
show_price(prices_desc)
show_price(prices_desc[4::-1], False)