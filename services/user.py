from model.Login_methods import new_user
from model.Login_methods import old_user_userId

def add_new_user(username, email, password):
    new_user(username, email, password)
    
def return_old_user(username, password):
    old_user_userId(username, password)