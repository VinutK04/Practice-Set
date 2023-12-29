items = []
orders = []

def add_item():
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    item = {"name": name, "price":price}
    items.append(item)
    print("Item added Successfully!!!")

def view_items():
    if items:
        print("Items: ")
        for i, item in enumerate(items):
            print(f"{i+1}. {item['name']} - ${item['price']}")
    else:
        print("No items available.")

def take_order():
    items_list = []
    total_price = 0
    while True:
        view_items()
        item_index = input("Enter item number to add (or 'q' to quit): ")
        if item_index.lower() == 'q':
            break
        try:
            item_index = int(item_index)-1
            item = items[item_index]
            items_list.append(item['name'])
            total_price += item['price']
        except (ValueError, IndexError):
            print("Invalid item number...")

    order = {"items": items_list, "total_price": total_price}
    orders.append(order)
    print("Order placed Sucessfully!!!")
    for ele in orders:
        for key, value in ele.items():
            print(f"{key}: {value}")

while True:
    print("\nBakery Management System")
    print("1. Add item")
    print("2. View items")
    print("3. Take order")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_item()
    elif choice == '2':
        view_items()
    elif choice == '3':
        take_order()
    elif choice == '4':
        break
    else:
        print("Invalid choice!")
