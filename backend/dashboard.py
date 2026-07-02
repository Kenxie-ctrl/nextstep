from opportunity import (
    get_opportunities,
    add_opportunity,
    edit_opportunity,
    delete_opportunity,
)

from user import register_user, login_user
from employer import register_employer, login_employer


current_user = None
current_employer = None


def show_guest_menu():
    print("1. View Opportunities")
    print("2. Search Opportunities")
    print("3. Register User")
    print("4. User Login")
    print("5. Register Employer")
    print("6. Employer Login")
    print("0. Exit")


def show_user_menu():
    print("1. View Opportunities")
    print("2. Search Opportunities")
    print("3. Saved Opportunities")
    print("4. My Profile")
    print("5. Logout")
    print("0. Exit")


def show_employer_menu():
    print("1. View Opportunities")
    print("2. Search Opportunities")
    print("3. Post Opportunity")
    print("4. My Opportunities")
    print("5. Company Profile")
    print("6. Logout")
    print("0. Exit")


def view_opportunities():
    opportunities = get_opportunities()

    if not opportunities:
        print("\nNo opportunities found.")
        return

    for i, opportunity in enumerate(opportunities, start=1):
        print("-" * 50)
        print(f"{i}. {opportunity['title']}")
        print("Category:", opportunity["category"])
        print("Organization:", opportunity["organization"])
        print("Country:", opportunity["country"])

        status = (
            "✅ Verified"
            if opportunity["verified"]
            else "❌ Not Verified"
        )

        print("Status:", status)


def search_opportunities():
    category = input("\nCategory: ").lower()

    found = False

    for opportunity in get_opportunities():
        if opportunity["category"].lower() == category:
            print("-" * 50)
            print("Title:", opportunity["title"])
            print("Organization:", opportunity["organization"])
            print("Country:", opportunity["country"])
            found = True

    if not found:
        print("\nNo opportunities found.")


def main_menu():
    global current_user, current_employer

    while True:

        print("\n" + "=" * 50)
        print("        NextStep Backend v0.8.2")
        print("=" * 50)

        if current_employer:
            print(f"🏢 Logged in as Employer: {current_employer['name']}")
            print()
            show_employer_menu()

        elif current_user:
            print(f"👤 Logged in as User: {current_user}")
            print()
            show_user_menu()

        else:
            print("👋 Guest")
            print()
            show_guest_menu()

        choice = input("\nChoose an option: ")
# -------------------------
        # GUEST MENU
        # -------------------------

        if current_user is None and current_employer is None:

            if choice == "1":
                view_opportunities()

            elif choice == "2":
                search_opportunities()

            elif choice == "3":
                username = input("Username: ")
                password = input("Password: ")

                if register_user(username, password):
                    print("\n✅ Registration successful.")
                else:
                    print("\n❌ Username already exists.")

            elif choice == "4":
                username = input("Username: ")
                password = input("Password: ")

                if login_user(username, password):
                    current_user = username
                    print(f"\n✅ Welcome {username}!")
                else:
                    print("\n❌ Invalid username or password.")

            elif choice == "5":
                name = input("Company Name: ")
                email = input("Email: ")
                password = input("Password: ")

                if register_employer(name, email, password):
                    print("\n✅ Employer registered.")
                else:
                    print("\n❌ Email already exists.")

            elif choice == "6":
                email = input("Email: ")
                password = input("Password: ")

                employer = login_employer(email, password)

                if employer:
                    current_employer = employer
                    print(f"\n✅ Welcome {employer['name']}!")
                else:
                    print("\n❌ Invalid email or password.")

            elif choice == "0":
                print("\nThanks for using NextStep!")
                break

            else:
                print("\n❌ Invalid option.")

        # -------------------------
        # USER MENU
        # -------------------------

        elif current_user:

            if choice == "1":
                view_opportunities()

            elif choice == "2":
                search_opportunities()

            elif choice == "3":
                print("\n🚧 Saved Opportunities coming in Sprint 8.3")

            elif choice == "4":
                print(f"\nUsername: {current_user}")

            elif choice == "5":
                current_user = None
                print("\n✅ Logged out.")

            elif choice == "0":
                print("\nThanks for using NextStep!")
                break

            else:
                print("\n❌ Invalid option.")

        # -------------------------
        # EMPLOYER MENU
        # -------------------------

        else:

            if choice == "1":
                view_opportunities()

            elif choice == "2":
                search_opportunities()

            elif choice == "3":
                title = input("Title: ")
                category = input("Category: ")
                organization = current_employer["name"]
                country = input("Country: ")

                add_opportunity(
                    title,
                    category,
                    organization,
                    country,
                )

                print("\n✅ Opportunity posted successfully!")

            elif choice == "4":
                print("\n🚧 My Opportunities coming in Sprint 8.3")

            elif choice == "5":
                print("\nCompany:", current_employer["name"])
                print("Email:", current_employer["email"])

            elif choice == "6":
                current_employer = None
                print("\n✅ Logged out.")

            elif choice == "0":
                print("\nThanks for using NextStep!")
                break

            else:
                print("\n❌ Invalid option.")
