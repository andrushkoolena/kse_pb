from data import inventory, transactions
from add_product import add_product
while True:
    action=int(input("Введіть дію:"))
    if action ==1:
        tovar=input("Який товар ви хочете додати?")
        qty=input("Яку кількість ви хочете додати?")
        inventory = add_product(inventory, tovar, qty)
    elif action==2:
        name=input("Який товар хочете придбати?")
        quantity=input("Яку кількість ви хочете додати?")
        seller_id=input("Seller id:")
        transactions=input("transactions:")
        inventory=buy_product(inventory, transactions, name, quantity, seller_id)
            
    elif action==3:
        pass
    elif action==0:
        break