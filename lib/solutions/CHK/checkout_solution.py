

# noinspection PyUnusedLocal
# skus = unicode string
item_prices = {"A": 50, "B": 30, "C": 20, "D": 15,
               "E": 40, "F": 10, "G": 20, "H": 10,
               "I": 35, "J": 60, "K": 80, "L": 90,
               "M": 15, "N": 40, "O": 10, "P": 50,
               "Q": 30, "R": 50, "S": 30, "T": 20,
               "U": 40, "V": 50, "W": 20, "X": 90,
               "Y": 10, "Z": 50}





def checkout(skus):
    item_counts = {"A": 0, "B": 0, "C": 0, "D": 0,
                   "E": 0, "F": 0, "G": 0, "H": 0,
                   "I": 0, "J": 0, "K": 0, "L": 0,
                   "M": 0, "N": 0, "O": 0, "P": 0,
                   "Q": 0, "R": 0, "S": 0, "T": 0,
                   "U": 0, "V": 0, "W": 0, "X": 0,
                   "Y": 0, "Z": 0}
    items = [*skus]
    if not items:
        return 0
    total = 0
    discount = 0
    for item in items:
        if item_prices.get(item):
            total += item_prices.get(item)
        else:
            print('here')
            return -1

        item_counts[item] += 1

    #apply discounts
    # A discount
    fives = item_counts["A"] // 5
    discount += fives * 50
    remainder_a_count = item_counts["A"] - (fives * 5)
    threes = remainder_a_count // 3
    discount += threes * 20

    # E discount before b
    free_bs = item_counts["E"] // 2
    remainder_b_count = item_counts["B"] - min(item_counts["B"], free_bs)
    discount += min(item_counts["B"], free_bs)*30

    # B discount
    discount += (remainder_b_count // 2) * 15

    # F discount
    discount += (item_counts["F"] // 3) * 10

    # H discount
    ten_hs = item_counts["H"] // 10
    discount += ten_hs * 20
    remainder_h_count = item_counts["H"] - (ten_hs * 10)
    five_hs = remainder_h_count // 5
    discount += five_hs * 5

    # K discount
    discount += (item_counts["K"] // 2) * 10

    # N discount using Ms
    free_ms = item_counts["N"] // 3
    discount += min(item_counts["M"], free_ms)*15

    # P discount
    discount += (item_counts["P"] // 5) * 50

    # R discount before Q
    free_qs = item_counts["R"] // 3
    remainder_q_count = item_counts["Q"] - min(item_counts["Q"], free_qs)
    discount += min(item_counts["Q"], free_qs)*30

    # Q discount
    discount += (remainder_q_count // 3) * 10

    # U discount
    discount += (item_counts["U"] // 4) * 40

    # V discount
    three_vs = item_counts["V"] // 3
    discount += three_vs * 20
    remainder_v_count = item_counts["V"] - (three_vs * 3)
    two_vs = remainder_v_count // 2
    discount += two_vs * 10




    return total - discount





