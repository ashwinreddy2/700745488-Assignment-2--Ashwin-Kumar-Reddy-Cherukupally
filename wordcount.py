def count_word():
        file1 = open("input.txt", "r")
        info = file1.readlines()
        file2 = open("output.txt","w")
        file2.writelines(info)
        file2.write("\n count :")
        dict = {}
        for i in info:
            x = i.strip().split(" ")
            for y in x:
                z ="\n"+ y + " " + str(x.count(y))
                file2.write(z)
count_word()