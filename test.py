
f = open("common_words.txt")

common_passwords = f.readlines()
clean_passwords = []

for password in common_passwords:
    password = password.replace("\n", "")
    clean_passwords.append(password)

if 'hiiiiii' in clean_passwords:
    print("Yes")
else:
    print("No")

f.close()

