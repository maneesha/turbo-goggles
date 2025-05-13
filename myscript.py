import requests 

print("Always look on the bright side of life")

r = requests.get("https://deckofcardsapi.com/api/deck/new/draw/?count=2")
print(r.json())

