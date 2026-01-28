import time
import requests

website = input("Enter website URL (example: https://google.com): ")

try:
    start_time = time.time()
    response = requests.get(website)
    end_time = time.time()

    if response.status_code == 200:
        print("✅ Website is UP")
        print("Response Time:", round(end_time - start_time, 2), "seconds")
    else:
        print("⚠️ Website returned status:", response.status_code)

except requests.exceptions.RequestException:
    print("❌ Website is DOWN or unreachable")
