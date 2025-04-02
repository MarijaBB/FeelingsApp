from services.authentication import username_validation, email_password_validation
from services.user import add_new_user

def signup(username,email,password):
    if username_validation(username):
        return 0 
    k = email_password_validation(username,email,password)
    if k == -1:
        return -1
    if k == -2:
        return -2
    if k == 1:
        add_new_user(username, email, password)
    
    