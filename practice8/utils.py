def is_valid_price(value):
    if value<0:
        vidp=False
    else:
        vidp=True
    return vidp
print(is_valid_price(-23))

def is_valid_price(value):
    if value<0:
        vidp2=False
    else:
        vidp2=True
    return vidp2
def format_currency(amount):
    shtuka="%.2f" %amount
    return shtuka+" грн"


    