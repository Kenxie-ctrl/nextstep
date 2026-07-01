from database import load_data, save_data

OPPORTUNITY_FILE = "data/opportunities.json"


def get_opportunities():
    opportunities = load_data(OPPORTUNITY_FILE)

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

        save_data(OPPORTUNITY_FILE, opportunities)

    return opportunities


def add_opportunity(title, category, organization, country):
    opportunities = get_opportunities()

    opportunities.append({
        "title": title,
        "category": category,
        "organization": organization,
        "country": country,
        "verified": False
    })

    save_data(OPPORTUNITY_FILE, opportunities)


def edit_opportunity(index, new_title):
    opportunities = get_opportunities()

    if 0 <= index < len(opportunities):
        opportunities[index]["title"] = new_title
        save_data(OPPORTUNITY_FILE, opportunities)
        return True

    return False


def delete_opportunity(index):
    opportunities = get_opportunities()

    if 0 <= index < len(opportunities):
        deleted = opportunities.pop(index)
        save_data(OPPORTUNITY_FILE, opportunities)
        return deleted

    return None
