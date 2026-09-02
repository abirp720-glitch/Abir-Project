print("--- ABIR's Password Checker 🔐 ---")
password = input("Ekta password dao bebs: ")

length = len(password)
has_number = any(char.isdigit() for char in password)
has_big = any(char.isupper() for char in password)

print(f"\nTomar password er length: {length}")

if length < 6:
    print("❌ Onek choto! Weak Password")
elif length < 8:
    print("⚠️ Medium, arektu boro koro")
else:
    if has_number and has_big:
        print("✅ Strong Password bebs! 🔥")
    else:
        print("⚠️ Thik ache, kintu number ar Boro hater okkhor dao")
