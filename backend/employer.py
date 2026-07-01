from database import load_data, save_data

EMPLOYER_FILE = "data/employers.json"


def get_employers():
    return load_data(EMPLOYER_FILE)


def register_employer(name, email, password):
    employers = get_employers()

    for employer in employers:
        if employer["email"] == email:
            return False

    employers.append({
        "name": name,
        "email": email,
        "password": password,
        "verified": False
    })

    save_data(EMPLOYER_FILE, employers)

    return True


def login_employer(email, password):
    employers = get_employers()

    for employer in employers:
        if employer["email"] == email and employer["password"] == password:
            return employer

    return None
