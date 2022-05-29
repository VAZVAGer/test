index = 0


class Client:
    name = None
    address = None
    phone_number = None
    order_list = None
    client_index = 0

    def __init__(self, name, address, phone_number):
        global index
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.client_index = index
        index += 1


class Order:
    name = None
    price = None

    def __init__(self, name, price):
        self.name = name
        self.price = price


list_clients = []
while True:
    client_name = input("name")
    client_address = input("address")
    client_number = input("number")
    client = Client(client_name, client_address, client_number)
    client.order_list = list()
    list_clients.append(client)
    while True:
        order_name = input("order name")
        order_price = input("order price")
        order = Order(order_name, order_price)
        client.order_list.append(order)
        command = input("continue ordering? Y/N")
        if command == "N":
            break
    exit_command = input("continue? Y/N")
    if exit_command == "N":
        break

with open("my_order.txt", "w", encoding='UTF-8') as file:
    for client in list_clients:
        file.write("index:" + str(client.client_index)+"\n")
        file.write("name:" + client.name+"\n")
        file.write("address:" + client.address+"\n")
        file.write("phone_number:" + client.phone_number+"\n")
        print("index:" + str(client.client_index))
        print("name:" + client.name)
        print("address:" + client.address)
        print("phone_number:" + client.phone_number)
        file.write("---------------"+"\n")
        for order in client.order_list:
            file.write("order:" + order.name+"\n")
            file.write("price:" + str(order.price)+"\n")
            print("order:" + order.name)
            print("price:" + str(order.price))
        print("=======")
        file.write("=======\n")
