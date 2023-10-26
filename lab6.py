#Alan Skrypek
def encoder(x):
    new_pass = ""
    for i in x:
        if int(i) + 3 > 10:
            new_pass += str((int(i) + 3) % 10)
        else:
            new_pass = new_pass + str((int(i) + 3))
    return x
pass_input = encoder(input("What is your password? "))

print(pass_input)
print("new changes")