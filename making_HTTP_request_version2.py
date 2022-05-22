# to make requests in Python we need the "requests" module.
import requests
from random import choice 

url = "https://icanhazdadjoke.com/search"

while True: 
    print("Enter 'Quit' to stop:")
    term = input("what joke do you want to hear? ").lower()
    if term == "quit":
        print("Goodbye")
        break 

    resp = requests.get(
        url, 
        headers = {"accept" : "application/json"},
        params = {"term" : term}
        ).json() 

    data = resp["results"]
    if len(data) == 0:
        print(f"I am sorry. I have no jokes about {term}")
    else:
        print(f"I have {len(data)} jokes for you about {term}. here's one:")
        print(choice(data)["joke"]) 

   