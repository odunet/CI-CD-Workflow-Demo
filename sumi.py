def ave():
    x = int(input("How many numbers: "))
    y = []
    for i in range(x):
     y.append(int(input("Enter number: ")))

    z = 0
    for i in y:
        z = z + i

    aver = round(z/len(y),2)
    return aver,y
