def login(username, password):
    admin_password = "admin123"

    if username == "admin" and password == admin_password:
        return True

    return False
