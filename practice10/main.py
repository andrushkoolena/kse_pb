from data.data import get_data, load_data
while True:
    user_choice=int(input("Your choice:"))
    if user_choice==0:
        break
    elif user_choice==1:
        print("add_hall")
        create_hall(file_path)
    elif user_choice==2:
        print("Show empty seats")
        pass
    elif user_choice==3:
        print("Book the seat")
        pass
    elif user_choice==4:
        print("Decline reserve")
        pass
    

