for row in range(10):
    for column in range(11):
        if (row + column) % 2 == 0:
            print("*", end=" ")
        else:
            print("+", end=" ")
    print()
