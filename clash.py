import random as r
import time

play = True

print("Dragon Clash")

time.sleep(1)

print("Your options: fireball, lightning bolt, ice")

user_input = input()
options = ["blocked", "missed", "hit"]
randomchoic = r.choice(options)

print(f"\nYou chose {user_input}, dragon has been {randomchoic}.\n")


if user_input == "fireball":
    if randomchoic == "hit":
        print("You have defeated the dragon.")
    else:
      print("The dragon has defeated you")
elif user_input == "lightning bolt":
      if randomchoic == "hit":
          print("You have defeated the dragon.")
      else:
        print("The dragon has defeated you")
elif user_input == "ice":
      if randomchoic == "hit":
          print("You have defeated the dragon.")
      else:
          print("The dragon has defeated you")
