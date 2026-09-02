import requests

print("--- ABIR's Link Shortener V3 🔗 ---")

while True:
    long_url = input("\nBoro link dao (exit likhle ber hobe): ")
    
    if long_url.lower() == "exit":
        print("Bye Bye bebs! 🖤")
        break

    if not long_url.startswith("http"):
        long_url = "https://" + long_url

    try:
        api_url = f"https://is.gd/create.php?format=simple&url={long_url}"
        response = requests.get(api_url)
        
        if response.status_code == 200:
            print(f"✅ Choto link: {response.text}")
        else:
            print("❌ Link ta thik na bebs")
    except:
        print("❌ Internet check koro bebs")
