cat main.py

from opportunity import (
    get_opportunities,
    add_opportunity,
    edit_opportunity,
    delete_opportunity,
)

from user import register_user, login_user
from employer import register_employer, login_employer


def main_menu():
    while True:
        print("\n" + "=" * 50)
        print("        NextStep Backend v0.7.0")
        print("=" * 50)

        print("1. View Opportunities")
        print("2. Search by Category")
        print("3. Add Opportunity")
        print("4. Edit Opportunity")
        print("5. Delete Opportunity")
        print("6. Register User")
        print("7. User Login")
        print("8. Register Employer")
        print("9. Employer Login")
        print("10. Exit")

        choice = input("\nChoose an option: ")

        if choice == "10":
            print("\nThanks for using NextStep!")
            break

        else:
            print("\nFeature coming next...")
from opportunity import (
    get_opportunities,
    add_opportunity,
    edit_opportunity,
    delete_opportunity,
)

from user import register_user, login_user
from employer import register_employer, login_employer


def main_menu():
    while True:
        print("\n" + "=" * 50)
        print("        NextStep Backend v0.7.0")
        print("=" * 50)

        print("1. View Opportunities")
        print("2. Search by Category")
        print("3. Add Opportunity")
        print("4. Edit Opportunity")
        print("5. Delete Opportunity")
        print("6. Register User")
        print("7. User Login")
        print("8. Register Employer")
        print("9. Employer Login")
        print("10. Exit")

        choice = input("\nChoose an option: ")

        if choice == "10":
            print("\nThanks for using NextStep!")
            break

        else:
            print("\nFeature coming next...")
