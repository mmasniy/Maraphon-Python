def buy_milk(money=0):
    product = '[milk]'
    price = 25
    if money >= price:
        return product * (money // price)


def buy_bread(money=0):
    product = '[bread]'
    price = 19
    if money >= price:
        if money // price >= 3:
            return product * 3
        else:
            return product * (money // price)
