import random
import string
def generate_password(length,allow_symbols):
    if allow_symbols==True:
        password=string.ascii_letters+string.digits+string.punctuation
    else:
        password=string.ascii_letters+string.digits
    password2=random.choices(password, k=length)
    return password2
print(generate_password(10,True))