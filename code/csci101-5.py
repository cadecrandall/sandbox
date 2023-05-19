user_string = input()

octal_integers = ['0', '1', '2', '3', '4', '5', '6', '7']
is_valid = True
for char in user_string:
    if char not in octal_integers:
        print(user_string, "is not a binary string.")
        is_valid = False
        break

if is_valid:
    x = int(user_string, 2)
    print("The binary value is", x, "in decimal.")
