def calculate_item_cost(item):
    if item.type == 'product':
        return item.price
    elif item.type == 'service':
        return item.price * item.duration
    elif item.type == 'discount':
        if item.is_percentage:
            return item.price * (1 - item.value / 100)
        else:
            return item.price - item.value
    else:
        raise ValueError(f"Unknown item type: {item.type}")

def apply_rush_surcharge(total_cost):
    return total_cost * 1.1

def apply_vip_surcharge(total_cost):
    return total_cost * 1.2

def calculate_total_cost(order):
    total_cost = sum(calculate_item_cost(item) for item in order.items)
    if order.is_rush:
        total_cost = apply_rush_surcharge(total_cost)
    if order.is_vip:
        total_cost = apply_vip_surcharge(total_cost)
    return total_cost