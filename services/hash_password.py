import bcrypt
def hashing_password(password):
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password.encode(), salt)
    return password_hash.decode()