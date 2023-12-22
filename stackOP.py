stack = []
while True:
    print("\nPlease select any option")
    print("1: Display Stack")
    print("2: Push operation")
    print("3: Pop operation")
    print("Press 'Y/y' to exit Exit()")

    choice = input("Enter your selection: ")

    if choice == '1':
        # Display the stack
        if stack:
            print("Stack:", stack)
        else:
            print("Stack is empty")
    elif choice == '2':
        # Push operation
        value = int(input("Enter value to push: "))
        stack.append(value)
        print(value, "pushed to stack")
    elif choice == '3':
        # Pop operation
        if stack:
            popped_value = stack.pop()
            print(popped_value, "popped from stack")
        else:
            print("Stack is empty")
    elif choice.lower() == 'y':
        print("Thank you for being with me")
        break
    else:
        print("Invalid choice")
