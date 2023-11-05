

# noinspection PyUnusedLocal
# skus = unicode string
item_prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E":40}



def checkout(skus):
    items = [*skus]
    a_count = 0
    b_count = 0
    total = 0
    discount = 0
    for item in items:
        if item == "A": a_count+=1
        elif item == "B": b_count+=1
        if item_prices.get(item):
            total += item_prices.get(item)
        else: return -1

    #apply discounts
    if a_count>=3:
        discount += (a_count // 3) * 20
    if b_count>=2:
        discount += (b_count // 2) * 15

    return total - discount
