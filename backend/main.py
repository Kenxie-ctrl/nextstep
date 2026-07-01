import json
import os

DATA_FILE = "data/opportunities.json"

def load_opportunities():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def save_opportunities(opportunities):
    with open(DATA_FILE, "w") as file:
        json.dump(opportunities, file, indent=4)

opportunities = load_opportunities()

if len(opportunities) == 0:
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

while True:
    print("=" * 50)
    print("          NextStep Backend v0.4.0")
    print("=" * 50)

    print("\n1. View Opportunities")
    print("2. Search by Category")
    print("3. Add Opportunity")
    print("4. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        print("\nLatest Opportunities\n")

        for opportunity in opportunities:
            print("-" * 50)
            print("Title:", opportunity["title"])
            print("Category:", opportunity["category"])
            print("Organization:", opportunity["organization"])
            print("Country:", opportunity["country"])

            if opportunity["verified"]:
                print("Status: ✅ Verified")
            else:
                print("Status: ❌ Not Verified")

    elif choice == "2":
        category = input("\nEnter category: ")

        found = False

        for opportunity in opportunities:
            if opportunity["category"].lower() == category.lower():
                print("\nTitle:", opportunity["title"])
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

        new_opportunity = {
            "title": title,
            "category": category,
            "organization": organization,
            "country": country,
            "verified": False
        }

        opportunities.append(new_opportunity)
        save_opportunities(opportunities)

        print("\n✅ Opportunity added successfully!")

    elif choice == "4":
        print("\nThank you for using NextStep!")
        break

    else:
        print("\n❌ Invalid option.")
