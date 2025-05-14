import requests 
import matplotlib.pyplot as plt

print("Always look on the bright side of life")

r = requests.get("https://deckofcardsapi.com/api/deck/new/draw/?count=2")
print(r.json())

time = [0, 1, 2, 3]
position = [0, 100, 200, 300]

plt.plot(time, position)
plt.xlabel('Time (hr)')
plt.ylabel('Position (km)')
plt.savefig("my_plot.png")

