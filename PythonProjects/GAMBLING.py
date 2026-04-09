import random
import time
Icons = ['🍔', '🍕', '🍛', '7', 'BAR']
print("WELCOME TO GAMBLING")
time.sleep(0.5)
print("Heres what's gonna happen. You're gonna press enter, and i'll spin a slot machine.")
time.sleep(0.5)
print("Heres the Key.")
time.sleep(0.5)
print("The hamburger is worth $1. The pizza is worth $2. The pancake is worth $3, and the 7 is worth... $7. Obviously.")
time.sleep(0.5)
print("A BAR is a filler, it's worth $0. You win 1x the prize for one of a symbol, 3x the prize for 2 of a symbol, and 7x the prize if you get all the same symbol.")
Playa = input("Ready? ")
if Playa == "no":
  quit
elif Playa == "yes":
  print("great. Spining...")
  time.sleep(0.5)
  roll1 = random.choice(Icons)
  print(f"Symbol 1: {roll1}")
  time.sleep(0.5)
  roll2 = random.choice(Icons)
  print(f"symbol 2: {roll2}. Current layout: {roll1}, {roll2}.")
  time.sleep(0.5)
  roll3 = random.choice(Icons)
  print(f"... {roll1}, {roll2}, {roll3}.")
  if roll1 == "🍔":
    Val1 = 1
  elif roll1 == "🍕":
    Val1 = 2
  elif roll1 == "🍛":
    Val1 = 3
  elif roll1 == "7":
    Val1 = 7
  elif roll1 == "bar":
      Val1 = 0
   int(Val1)
  if roll2 == "🍔":
    Val2 = 1
  elif roll2 == "🍕":
    Val2 = 2
  elif roll2 == "🍛":
    Val2 = 3
  elif roll2 == "7":
    Val2 = 7
  elif roll2 == "bar":
      Val2 = 0
   int(Val2)
   if roll3 == "🍔":
    Val3 = 1
  elif roll3 == "🍕":
    Val3 = 2
  elif roll3 == "🍛":
    Val3 = 3
  elif roll3 == "7":
    Val3 = 7
  elif roll3 == "bar":
      Val3 = 0
   int(Val3)
   total = Val1 + Val2 + Val3
   if Val1 == Val2 and Val2 == Val3:
       total * 7
   elif Val1 == Val2 or val2 == val3:
       total * 3
   else:
       total * 1
   print(f"you won ${total}")
