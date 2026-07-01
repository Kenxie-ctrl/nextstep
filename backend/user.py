from database import load_data, save_data

USER_FILE = "data/users.json"


def get_users():
    return load_data(USER_FILE)


def register_user(username, password):
    users = get_users()

    for user in users:
        if user["username"] == username:
            return False

    users.append({
        "username": username,
        "password": password
    })

    save_data(USER_FILE, users)
    return True


def login_user(username, password):
    users = get_users()

    for user in users:
        if user["username"] == username and user["password"] == password:
            return True

    return False
