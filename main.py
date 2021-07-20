#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for nr_letter in range(1,nr_letters+1):
  nr_letter = random.randint(0,25)
  # print(letters[nr_letter])
  password = password + letters[nr_letter]
for nr_symbol in range(1,nr_symbols+1):
  nr_symbol = random.randint(0,8)
  # print(symbols[nr_symbol])
  password += symbols[nr_symbol]
for nr_number in range(1,nr_numbers+1):
  nr_number = random.randint(0,9)
  password += numbers[nr_number]
print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []
for nr_letter in range(1,nr_letters+1):
  nr_letter = random.randint(0,25)
  # print(letters[nr_letter])
  password_list.append(letters[nr_letter])
for nr_symbol in range(1,nr_symbols+1):
  nr_symbol = random.randint(0,8)
  # print(symbols[nr_symbol])
  password_list.append(symbols[nr_symbol])
for nr_number in range(1,nr_numbers+1):
  nr_number = random.randint(0,9)
  password_list.append(numbers[nr_number])
print(password_list)
random.shuffle(password_list)
print((password_list))
password = ""
for elem in password_list:
  password = password + elem
print(password)