from model.Login_methods import check_if_email_exists,check_if_username_exists,check_is_password_correct,new_user,old_user_userId
def username_validation(username):
    if check_if_username_exists(username)>0:
        print('That username already exists. Try again...') # pazi gde printas
        return 1      # u input_username se vrti petlja
    return 0           # prelazimo na sledeci korak, ubacivanje mejla i password

def email_password_validation(username, email, passwordhash):
    if check_if_email_exists(email)>0:
        print('Email already exists')  # pazi gde printas
        return -1
    # email exists, is password correct?
    userId = check_is_password_correct(email,passwordhash)
    if userId < 1:
        print('Wrong email or password') # pazi gde printas
        return -2
    new_user(username,email, passwordhash)
    return 1

def old_user_validation(username, passwordhash):
    userId = old_user_userId(username,passwordhash)
    if userId > 0:
        return userId
    else:
        return -1
