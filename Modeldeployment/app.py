s = []
top = -1
limit = int(input("Enter limit of stack. "))

print("Choose operation:\n1.Push \n2.Pop \n3.Display \n4.Peek \n5.Exit")
op = 0
while (op != 5):
    op = int(input("Enter operation: "))
    if (op == 1):
        if (top == (limit)):
            print("Stack is full.")
        else:
            e = int(input("Insert element: "))
            top += 1
            s.insert(top, e)


    elif (op == 2):
        if (top == -1):
            print("Stack is empty.")
        else:
            i = (s[top])
            top -= 1
            print("Popped element is: ", i)

    elif (op == 3):
        if (top == -1):
            print("Stack is empty.")
        else:
            for i in range(top + 1):
                print(s[top - i])

    elif (op == 4):
        if (top == -1):
            print("Stack is empty.")
        else:
            print(s[top])

