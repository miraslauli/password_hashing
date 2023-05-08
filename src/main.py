from registration import Registration

if __name__ == '__main__':
    reg = Registration()
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    reg.new_user_registration(username=username, unhashed_password=password)
    print(reg.show_database)

    username_to_check = input("Enter your username: ")
    password_to_check = input("Enter your password: ")
    print(reg.check_login(username_to_check, password_to_check))
