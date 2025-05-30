f = open("common_passwords.txt")

common_passwords = f.readlines()
clean_passwords = []

for password in common_passwords:
    password = password.replace("\n", "")
    clean_passwords.append(password)

if "" in clean_passwords:
    print("Yes")
else:
    print("No")

f.close()