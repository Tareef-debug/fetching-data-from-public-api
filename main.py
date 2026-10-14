
import requests

while True:
    input("Press Enter to generate a joke...")

    api_url = "https://v2.jokeapi.dev/joke/Any?safe-mode"

    try:
        response = requests.get(api_url, timeout=10)

        if response.status_code == 200:
            joke = response.json()

            if joke["type"] == "single":
                print("\n" + joke["joke"])
            else:
                print("\n" + joke["setup"])
                print(joke["delivery"])

            print()

        else:
            print("Could not fetch a joke. Try again.")

    except requests.exceptions.RequestException as e:
        print("Connection error:", e)
