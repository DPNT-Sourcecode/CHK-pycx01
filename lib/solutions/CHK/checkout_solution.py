

# noinspection PyUnusedLocal
# skus = unicode string
item_prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10}



def checkout(skus):
    items = [*skus]
    if not items:
        return 0
    a_count = 0
    b_count = 0
    e_count = 0
    f_count = 0
    total = 0
    discount = 0
    for item in items:
        if item == "A": a_count+=1
        elif item == "B": b_count+=1
        elif item == "E":e_count += 1
        elif item == "F":f_count += 1
        if item_prices.get(item):
            total += item_prices.get(item)
        else:
            print('here')
            return -1

    #apply discounts
    # A discount
    fives = a_count // 5
    print(fives)
    discount += fives * 50
    remainder_a_count = a_count - (fives * 5)
    print(remainder_a_count)
    threes = remainder_a_count // 3
    print(threes)
    discount += threes * 20

    # E discount before b
    free_bs = e_count // 2
    remainder_b_count = b_count - min(b_count, free_bs)
    discount += min(b_count, free_bs)*30

    # B discount
    discount += (remainder_b_count // 2) * 15

    # F discount
    discount += (f_count // 3) * 10



    return total - discount


