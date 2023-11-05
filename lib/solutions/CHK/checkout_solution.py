

# noinspection PyUnusedLocal
# skus = unicode string
item_prices = {"A": 50, "B": 30, "C": 20, "D": 15}



def checkout(skus):
    items = skus.split()
    a_count = 0
    b_count = 0
    total = 0
    for item in items:
        if item == "A": a_count+=1
        elif item == "B": b_count+=1
        total += item_prices.get(item)

    #apply discounts
    if a_count>=3:
        
    if b_count>=2:

    raise NotImplementedError()

