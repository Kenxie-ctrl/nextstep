import json
import os

DATA_FILE = "data/opportunities.json"


def load_opportunities():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                return json.load(file)
        except:
            return []
    return []


def save_opportunities(opportunities):
    with open(DATA_FILE, "w") as file:
        json.dump(opportunities, file, indent=4)


opportunities = load_opportunities()

if not opportunities:
    opportunities = [
        {
            "title": "Mastercard Foundation Scholarship",
            "category": "Scholarship",
            "organization": "Mastercard Foundation",
            "country": "Nigeria",
            "verified": True
        },
        {
            "title": "Google Software Internship",
            "category": "Internship",
            "organization": "Google",
            "country": "Remote",
            "verified": True
        },
        {
            "title": "MTN Graduate Programme",
            "category": "Graduate Job",
            "organization": "MTN",
            "country": "Nigeria",
            "verified": False
        }
    ]
    save_opportunities(opportunities)

while True:
    print("\n" + "=" * 50)
    print("          NextStep Backend v0.5.0")
    print("=" * 50)

    print("1. View Opportunities")
    print("2. Search by Category")
    print("3. Add Opportunity")
    print("4. Edit Opportunity")
    print("5. Delete Opportunity")
    print("6. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        if not opportunities:
            print("\nNo opportunities available.")
        else:
            for i, opportunity in enumerate(opportunities, start=1):
                print("-" * 50)
                print(f"#{i}")
                print("Title:", opportunity["title"])
                print("Category:", opportunity["category"])
                print("Organization:", opportunity["organization"])
                print("Country:", opportunity["country"])
                status = "✅ Verified" if opportunity["verified"] else "❌ Not Verified"
                print("Status:", status)

    elif choice == "2":
        category = input("\nEnter category: ")

        found = False

        for opportunity in opportunities:
            if opportunity["category"].lower() == category.lower():
                print("-" * 50)
                print("Title:", opportunity["title"])
                print("Organization:", opportunity["organization"])
                print("Country:", opportunity["country"])
                found = True

        if not found:
            print("\nNo opportunities found.")

    elif choice == "3":
        print("\nAdd New Opportunity")

        title = input("Title: ")
        category = input("Category: ")
        organization = input("Organization: ")
        country = input("Country: ")

        opportunities.append({
            "title": title,
            "category": category,
            "organization": organization,
            "country": country,
            "verified": False
        })

        save_opportunities(opportunities)
        print("\n✅ Opportunity added successfully!")

    elif choice == "4":
        if not opportunities:
            print("\nNo opportunities to edit.")
            continue

        print("\nSelect an opportunity to edit:")

        for i, opportunity in enumerate(opportunities, start=1):
            print(f"{i}. {opportunity['title']}")

        number = int(input("Number: ")) - 1

        if 0 <= number < len(opportunities):
            new_title = input("New title: ")
            opportunities[number]["title"] = new_title
            save_opportunities(opportunities)
            print("\n✅ Opportunity updated!")
        else:
            print("\nInvalid selection.")

    elif choice == "5":
        if not opportunities:
            print("\nNo opportunities to delete.")
            continue

        print("\nSelect an opportunity to delete:")

        for i, opportunity in enumerate(opportunities, start=1):
            print(f"{i}. {opportunity['title']}")

        number = int(input("Number: ")) - 1

        if 0 <= number < len(opportunities):
            deleted = opportunities.pop(number)
            save_opportunities(opportunities)
            print(f"\n✅ Deleted: {deleted['title']}")
        else:
            print("\nInvalid selection.")

    elif choice == "6":
        print("\nThank you for using NextStep!")
        break

    else:
        print("\n❌ Invalid option.")
