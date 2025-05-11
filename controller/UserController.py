from model.LoginMethods import new_user,check_is_password_correct
from services.hash_password import hashing_password

def add_new_user_and_login(username, email, password):
    password_hash = hashing_password(password)
    new_user(username, email, password_hash)
    return check_is_password_correct(email,password)