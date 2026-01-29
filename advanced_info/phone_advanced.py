import phonenumbers
from phonenumbers import geocoder, carrier, timezone

number = input("Enter phone number with country code: ")

try:
    phone = phonenumbers.parse(number)

    print("\n🔥 ADVANCED PHONE OSINT")
    print("-" * 35)
    print("✔ Valid:", phonenumbers.is_valid_number(phone))
    print("🌍 Country:", geocoder.description_for_number(phone, "en"))
    print("📡 Carrier:", carrier.name_for_number(phone, "en"))
    print("⏰ Timezone:", timezone.time_zones_for_number(phone))

except:
    print("❌ Invalid phone number")
