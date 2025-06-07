from data import emails
import hashlib
from data import users
user_status=False
def registration(users):
    login=input("Enter login:")
    password=input("Enter password:")
    password_hash=hashlib.sha256("{}".format(password).encode()).hexdigest()
    print(login, users)
    if login in users:
        print("Username is taken")
    else:
        users.update({login: password_hash})
    return True


def login2(users):
    name=input("Enter name")
    password=input("pasword:")
    password_hash=hashlib.sha256("{}".format(password).encode()).hexdigest()
    if name not in users:
        print("User is not registrated")
        return False
    else:
        if password_hash==users[name]:
            print("You are logged in")
            return True
    return False

def logout():
    return False

def send_email(users,emails):
    sender=input("enter sender")
    recipient=input("enetr recipient")
    subject=("enter some text")
    if recipient not in users:
        print("recipient is not registered")
    else:
        emails.append({"sender":sender, "recipient":recipient, "email":email})
    return False


while True:
    
    try:
        user_choice=int(input("Enter your choice:"))
    except Exception as e:
        print(e)
        user_choice= None
    if user_choice==0:
        break
    elif user_choice==1:
        if user_status is False:
            registration(users)
        else:
            print("You are logged in")
    elif user_choice==2:
        if user_status is False:
            user_status=login2(users)
        else:
            print("Ypu are logged in")
    elif user_choice==3:
        if user_status is True:
            send_email(users,emails)
        else:
            print("You are not logged in to send email")
    elif user_choice==4:
        if user_status is True:
            user_status=logout()
        else:
            print("You are not logged in to log out")
        print("logout")
    elif user_choice==5:
        if user_status is True:
            print(users)
    
        


