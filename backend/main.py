print("=" * 45)
print("        NextStep Backend v0.2.0")
print("=" * 45)

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

print("\n🔥 Latest Opportunities\n")

for opportunity in opportunities:
    print("-" * 45)
    print("Title:", opportunity["title"])
    print("Category:", opportunity["category"])
    print("Organization:", opportunity["organization"])
    print("Country:", opportunity["country"])

    if opportunity["verified"]:
        print("Status: ✅ Verified")
    else:
        print("Status: ❌ Not Verified")

