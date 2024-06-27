def calculate_total_price(product_prices, discount, tax_rate=0):
    total_price = sum(price * (0.9 if discount else 1) for price in product_prices)
    return total_price * (1 + tax_rate)