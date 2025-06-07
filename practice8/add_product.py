from data import inventory
def add_product(inventory, name, quantity):
    if name in inventory:
        inventory[name][quantity]+=quantity
    else:
        price=int(input("Яка ціна вашого товару?"))
        inventory[name] = {"price":price, "quantity":quantity}
    return inventory
