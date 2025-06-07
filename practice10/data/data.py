import json

def get_data(file_path):
    with open(file_path,'r+') as f:
        content=json.load(f)
    return content
print(get_data("practice10/data/cinema_halls.json"))

def load_data(data, file_path):
    with open(file_path,'r+') as f:
        json.dump(data,f)

a={"a":1}
load_data(a,"practice10/data/cinema_halls.json")
print(get_data("practice10/data/cinema_halls.json"))


def create_hall(file_path):
    halls=get_data(file_path)
    new_hall_name=input("The name of new hall:")
    if new_hall_name in halls:
        print("Already exists")
    else:
        num_rows=int(input("Enter number of rows:"))
        num_columns=int(input("Enter number of columns:"))
        new_hall_dict={new_hall_name:[]}
        for i in range(1,num_rows+1):
            for  j in range(1,num_columns+1):
                seat_dict={f"{i}-{j}":False}
                new_hall_dict[new_hall_name].append(seat_dict)
        halls.update(new_hall_dict)
    load_data(halls,file_path)

def show_empty_seats(file_path ,hall_name):
    halls=get_data(file_path )
    hall_name=input("Hall name?")
    if hall_name not in halls:
        print("Hall doesn't exist")
    else:
        selected_hall=halls[hall_name]
        empty_seats=[]
        seats=selected_hall.values()
        for seat in selected_hall:
            if seat.values() is False:
                empty_seats.append(seat.keys())
        print(empty_seats)
show_empty_seats(file_path)



    


