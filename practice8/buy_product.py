def buy_product(inventory, transactions, name, quantity, seller_id):
    if name in inventory:
        inventory[name]["quantity"] -= quantity
        transactions.apppend({"product":name, "quantity":quantity, "seller_id": seller_id})
    return inventory
