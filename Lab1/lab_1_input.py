def calculate_total_cost(order):
    total_cost = 0
    for item in order.items:
        if item.type == 'product':
            total_cost += item.price
        elif item.type == 'service':
            if item.duration <= 1:
                total_cost += item.price
            else:
                total_cost += item.price * item.duration
        elif item.type == 'discount':
            if item.is_percentage:
                total_cost *= (1 - item.value / 100)
            else:
                total_cost -= item.value
    if order.is_rush:
        total_cost *= 1.1
    if order.is_vip:
        total_cost *= 1.2
    return total_cost