# to make requests in Python we need the "requests" module.
import requests

url = "https://icanhazdadjoke.com/search"
term = input("what joke do you want to hear? ")

# we can pass three arguments to get() method:
# 1. the url of the data we want
# 2. the headers which in our case is requesting json
# 3. the params that we want to pass. in our case it is term for search
resp = requests.get(
    url, 
    headers = {"accept" : "application/json"},
    params = {"term" : term}
    ).json() 

# above line we are calling json() method on the request in order to
# to convert json into python dictionary. 
# we could call json() method seperatly on the resp varaible as resp.json()

data = resp["results"]

for joke in data:
    print(joke["joke"] + "\n") 