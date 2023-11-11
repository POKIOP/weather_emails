OPTIONS = {"1":"delete", "2":"create", "3":"update", "4":"send_email" }

def get_user_option():
    user_choice = input("Enter your option: ")
    return OPTIONS[user_choice]

