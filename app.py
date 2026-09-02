import requests
print("--- ABIR's Pro Checker V2 🔥 ---")
name = input("Tomar nam ki bebs? : ")
while True:
    link = input("\nWebsite dao (exit likhle ber hobe): ")
    if link.lower() == 'exit':
        print(f"\nBye Bye {name} bebs! 🖤")
        break
    if not link.startswith('http'):
        link = 'https://' + link
    try:
        r = requests.get(link, timeout=5)
        if r.status_code == 200:
            print(f"✅ {link} -> UP! Status: {r.status_code}")
        else:
            print(f"⚠️ {link} -> Status: {r.status_code}")
    except:
        print(f"❌ {link} -> DOWN!")
