queue = []

while True:
    print("Please select your choice")
    print("1. Display items")
    print("2. Push items")
    print("3. Pop items")
    print("Press 'Q/q' to exit()")

    choice = input("Please enter your choice: ")

    if choice == '1':
        if queue:
            print("Items are: ", queue)
        else:
            print('Queue is empty')

    elif choice == '2':
        item = int(input("Enter value to be insert: "))
        queue.append(item)

    elif choice == '3':
        if queue:
            print("Removed item is: ", queue.pop(0))
            print(queue)
        else:
            print("Queue is empty")

    elif choice.lower() == 'q':
        print('Thank you for being with me')
        break

    else:
        print("Invalid selection!!!")
