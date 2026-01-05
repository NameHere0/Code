from random import choice

len = int(input("Length of password: "))
all_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&/=?@_"


chars_list = list(all_chars)

password = []

for i in range(1, len):
    password.append(choice(chars_list))
    truepass = "".join(password)

print(truepass)
