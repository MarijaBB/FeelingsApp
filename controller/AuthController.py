from model.LoginMethods import *
from services.validation import *

def check_email(email):
    return check_if_email_exists(email)

def check_password(email,password):
    return check_is_password_correct(email,password)

def try_to_signup(username, email, password):
    if not is_username_good_format(username):
        return 'Bad format of username'
    if check_if_username_exists(username) is not None:
        return 'Username exists'
    if not is_email_good_format(email):
        return 'Bad format of email'
    if check_if_email_exists(email) is not None:
        return'Email exists'
    if not is_password_good_format(password):
        return 'Bad format of password'
    return 1
    
    