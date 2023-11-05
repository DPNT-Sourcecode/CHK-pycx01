

# noinspection PyUnusedLocal
# skus = unicode string
item_prices = {"A": 50, "B": 30, "C": 20, "D": 15,
               "E": 40, "F": 10, "G": 20, "H": 10,
               "I": 35, "J": 60, "K": 80, "L": 90,
               "M": 15, "N": 40, "O": 10, "P": 50,
               "Q": 30, "R": 50, "S": 30, "T": 20,
               "U": 40, "V": 50, "W": 20, "X": 90,
               "Y": 10, "Z": 50}

item_counts = {"A": 0, "B": 0, "C": 0, "D": 0,
               "E": 0, "F": 0, "G": 0, "H": 0,
               "I": 0, "J": 0, "K": 0, "L": 0,
               "M": 0, "N": 0, "O": 0, "P": 0,
               "Q": 0, "R": 0, "S": 0, "T": 0,
               "U": 0, "V": 0, "W": 0, "X": 0,
               "Y": 0, "Z": 0}



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
        item_counts.update(item, )

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

    # H discount

    # K discount

    # N discount using Ms

    # P discount

    # R discount before Q

    # Q discount

    # U discount

    # V discount




    return total - discount

