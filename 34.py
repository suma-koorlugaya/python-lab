def Identity(size):
    for row in range(0, size):
        for col in range(0, size):


            if (row == col):
                print("1 ", end=" ")
            else:
                print("0 ", end=" ")
        print()

size = 5
Identity(size)
