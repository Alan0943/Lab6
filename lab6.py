#Alan Skrypek
def encoder(x):
    new_pass = ""
    for i in x:
        if int(i) + 3 > 10:
            new_pass += str((int(i) + 3) % 10)
        else:
            new_pass = new_pass + str((int(i) + 3))
    return x

def decoder(y):
    new_string = ""
    for i in y:
        if int(i) - 3 < 0:
            new_string += str(int(i) + 10 - 3)
        else:
            new_string += str(int(i) - 3)
    return new_string

while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

    option_input = input("Please enter an option: ")

    if option_input == 3:
        quit()

    elif option_input == 1:
        pass_input = encoder(input("Please enter your password to encode: "))
        print("Your password has been encoded and stored!")

    elif option_input == 2:
        pass
