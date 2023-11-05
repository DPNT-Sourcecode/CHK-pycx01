

# noinspection PyUnusedLocal
# skus = unicode string
item_prices = {"A": 50, "B": 30, "C": 20, "D": 15}



def checkout(skus):
    items = skus.split()
    a_count = 0
    b_count = 0
    total = 0
    discount = 0
    for item in items:
        if item == "A": a_count+=1
        elif item == "B": b_count+=1
        print(item)
        item_prices.get("A")
        total += item_prices.get(item)


    #apply discounts
    if a_count>=3:
        discount += (a_count // 3) * 20
    if b_count>=2:
        discount += (b_count // 2) * 15

    return total - discount


