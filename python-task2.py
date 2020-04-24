import random

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
email = input("Enter your email address: ")

password = first_name[:2] + last_name[-2:] + str(random.randint(10000, 99999))
# password = first_name[0:2]
confirm_password = input(f"Here is your new password: {password}. Confirm if you are satisfied with it. Press 'Y' for yes or any other key for no: ")

if confirm_password.upper() != "Y":
    while True:
        password = input("Enter your preffered password: ")
        if len(password) < 7:
            print("Password must be greater than seven characters")
            continue
        else:
            #print out user details
            break

user_data = {
    'first name': first_name,
    'last name': last_name,
    'email': email,
    'password': password
}

for key, value in user_data.items():
    print(f"{key}: {value}")