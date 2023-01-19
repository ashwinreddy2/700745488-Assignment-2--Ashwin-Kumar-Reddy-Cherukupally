first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
def fullname(first_name, last_name):
    global full_name
    full_name = first_name + " " + last_name
    print("your full_name is : ", full_name)
fullname(first_name, last_name)
def string_alternative(full_name):
    print("your alternative string is: ", full_name[::2])
string_alternative(full_name)