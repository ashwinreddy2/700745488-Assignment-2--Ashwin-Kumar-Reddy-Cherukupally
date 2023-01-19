inches = []
i = 1
z = input("enter the height in inches \n")
inches.append(z)
while z != "":
    i = i + 1
    z = input("enter height in inches\n")
    if z != "":
        inches.append(z)
    else:
        centimeter = [(int(i) * 2.54) for i in inches]
        print(centimeter)