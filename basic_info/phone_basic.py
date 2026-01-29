import phonenumbers
from phonenumbers import geocoder, carrier

number = input("Enter phone number with country code (ex: +919876543210): ")

try:
    phone = phonenumbers.parse(number)

    print("\n📞 BASIC PHONE INFORMATION")
    print("-" * 30)
    print("✔ Valid Number:", phonenumbers.is_valid_number(phone))
    print("🌍 Country:", geocoder.description_for_number(phone, "en"))
    print("📡 Carrier:", carrier.name_for_number(phone, "en"))

except:
    print("❌ Invalid phone number")
