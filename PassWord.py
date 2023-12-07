# pyperclip

# => using copy and paste

# example: 
# text = "hello"
# pyperclip.copy(text)
# paste = pyperclip.paste()
# print(paste)

# ---------------------------------------------------

# random

# => generating random numbers

# 1.Generate random float between 0 and 1

# input = random.random()
# print(input)

#  2. Random Integer within a range

# input = random.randint(1, 10)
# print(input)

#  3.Choosing random element from a sequence

# list = [1, 2, 3, 4, 5]
# input=random.choice(list)
# print(input)

#  4. Shuffling list

# list=[1, 2, 3, 4, 5]
# random.shuffle(list)
# print(list)

# 5. Generating random float within a range

# input = random.uniform(5, 10)
# print(input)

#  6. randomly choosing multiple elements

# list = [1, 2, 3, 4, 5]
# input = random.sample(list, 3)
# print(input)

# 7. Seed for reproducubillity

# random.seed(34)
# input = random.random()
# print(input)

from tkinter import *
import pyperclip
import random

root = Tk()
password_length = IntVar()
show_password = StringVar() 
def GeneratePassword():
    password_keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
                    'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
                    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
                    'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
                    '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')'
          ]
    create_password=""

    for x in range(password_length.get()):
        create_password = create_password + random.choice(password_keys)
    
    show_password.set(create_password)



def copyText():
    passwordcpy = show_password.get()
    pyperclip.copy(passwordcpy)

root.title("Password Generator")

root.geometry('600x500')

Label(root, text="Password Generator Applications", font = ("Times New Roman",25)).pack(pady=15)

Label(root, text="Enter Password Length",font=('Arial', 17)).pack(pady=15)
Entry(root, textvariable=password_length,font=35 ).pack(pady=20)

Button(root, text="Generate Password", command=GeneratePassword, font=('Times New Roman', 17)).pack(pady=18)

Entry(root, textvariable=show_password, font=('Arial', 20)).pack(pady=20)

Button(root, text="Copy to Clipbord", command=copyText, font=('Times New Roman', 17)).pack()
root.mainloop()