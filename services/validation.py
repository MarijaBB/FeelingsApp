import re
def is_email_good_format(email):
    if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',email):
        return True
    return False
def is_password_good_format(password):
    only_blanks = r'^[\s\r\n\t]*$'
    if re.match(only_blanks, password):
        return False
    return True
def is_username_good_format(username):
    only_blanks = r'^[\s\r\n\t]*$'
    if re.match(only_blanks, username):
        return False
    return True
