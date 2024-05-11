
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))



# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)




total_chars = nr_letters + nr_symbols + nr_numbers

password = [0 for i in range(total_chars)]

for i in range(nr_letters):
    placed_char = True
    while placed_char:
        index = random.randint(0, total_chars - 1)
        if(password[index] == 0):
            new_letter = letters[random.randint(0, len(letters) - 1)]
            password[index] = new_letter
            break

for i in range(nr_symbols):
    placed_char = True
    while placed_char:
        index = random.randint(0, total_chars - 1)
        if(password[index] == 0):
            new_symbol = symbols[random.randint(0, len(symbols) - 1)]
            password[index] = new_symbol
            break

for i in range(nr_numbers):
    placed_char = True
    while placed_char:
        index = random.randint(0, total_chars - 1)
        if(password[index] == 0):
            new_number = numbers[random.randint(0, len(numbers) - 1)]
            password[index] = new_number
            break

password_str = ''
for char in password:
    password_str = password_str + str(char)


print(f"Your password is: {password_str}")


# alternative: USE random.shuffle(list)

# password_list = []
#
# for char in range(1, nr_letters + 1):
#   password_list.append(random.choice(letters))
#
# for char in range(1, nr_symbols + 1):
#   password_list += random.choice(symbols)
#
# for char in range(1, nr_numbers + 1):
#   password_list += random.choice(numbers)
#
# print(password_list)
# random.shuffle(password_list)
# print(password_list)
#
# password = ""
# for char in password_list:
#   password += char
#
# print(f"Your password is: {password}")