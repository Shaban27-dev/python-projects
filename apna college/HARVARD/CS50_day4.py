# LIBRARIES
# modules
# import random
"""coin = random.choice(["heads", "tails"])
print(coin)"""


"""num = random.randint(1, 10)
if num > 0 and num < 5:
    print(f"num is {num} Heads")
else:
    print(f"num is {num} Tails")"""


"""cards = ["jack", "queen", "king"]
random.shuffle(cards)
print(cards)"""


"""import statistics
mean = statistics.mean([80, 88, 79])
print(mean)"""


# import sys
"""try:    
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguements")"""

"""if len(sys.argv) < 2:
    sys.exit("Too few arguements")

for arg in sys.argv[1:-1]:
    print("hello, my name is", arg)"""


# COWSAY
"""import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])"""


"""import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
print(json.dumps(response.json(), indent=2))

o = response.json()
for result in o["results"]:
    print(result["trackName"])"""

"""def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

if __name__ == "__main__":
    main()"""