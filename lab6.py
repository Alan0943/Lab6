pass_input = input("What is your password? ")

new_pass = ""

for i in pass_input:
    inc_val = int(i) + 3
    new_pass = new_pass+ str(inc_val)
print(new_pass)