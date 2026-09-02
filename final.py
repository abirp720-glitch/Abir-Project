import requests
from datetime import datetime

print("--- ABIR's Final Pro Tool V4 👑 ---")
print("Ei tool diye client ke report deya jay!")

website = input("\nClient er website dao bebs: ")
if not website.startswith("http"):
    website = "https://" + website

try:
    r = requests.get(website, timeout=5)
    status = f"UP ({r.status_code})" if r.status_code == 200 else f"DOWN ({r.status_code})"
except:
    status = "DOWN / Problem"

try:
    short_api = f"https://is.gd/create.php?format=simple&url={website}"
    short_link = requests.get(short_api).text
except:
    short_link = "Short kora jay nai"

now = datetime.now().strftime("%d-%m-%Y %H:%M")

report = f"""
--- Website Audit Report ---
By: ABIR
Date: {now}

1. Website: {website}
2. Status: {status}
3. Short Link: {short_link}
4. Security Note: Password must be Strong (8+ char, Number, Capital)
5. Recommendation: Website is {status}. Use short link for sharing.

Thank you!
"""

print(report)

# file save
with open("client_report.txt", "w") as f:
    f.write(report)

print("✅ Report save hoye gese: client_report.txt")
