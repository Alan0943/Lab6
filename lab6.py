pass_input = input("What is your password? ")

new_pass = ""

for i in pass_input:
    if int(i) + 3 > 10:
        new_pass += str((int(i) + 3) % 10)
    else:
        new_pass = new_pass + str((int(i) + 3))

print(new_pass)
print("new changes")