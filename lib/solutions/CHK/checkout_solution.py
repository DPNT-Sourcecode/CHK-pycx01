

# noinspection PyUnusedLocal
# skus = unicode string
item_prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E":40}



def checkout(skus):
    items = [*skus]
    a_count = 0
    b_count = 0
    e_count = 0
    total = 0
    discount = 0
    for item in items:
        if item == "A": a_count+=1
        elif item == "B": b_count+=1
        elif item == "E":e_count += 1
        if item_prices.get(item):
            total += item_prices.get(item)
        else: return -1

    #apply discounts
    # A discount
    fives = a_count // 5
    discount += fives * 50
    remainder_a_count = a_count - (fives * 5)
    threes = remainder_a_count // 3
    discount += threes * 20


    # B discount
    discount += (b_count // 2) * 15

    # E discount
    free_bs = e_count // 2
    discount = min(b_count, free_bs)*30

    return total - discount

