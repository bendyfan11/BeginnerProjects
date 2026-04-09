import random
import time

Icons = ['🍔', '🍕', '🍛', '7', 'BAR']
print("WELCOME TO GAMBLING")
time.sleep(0.5)
print("Here's what's gonna happen. You're gonna press enter, and I'll spin a slot machine.")
time.sleep(0.5)
print("Here's the Key.")
time.sleep(0.5)
print("The hamburger is worth $1. The pizza is worth $2. The pancake is worth $3, and the 7 is worth... $7. Obviously.")
time.sleep(0.5)
print("A BAR is a filler, it's worth $0. You win 1x the prize for one of a symbol, 3x the prize for 2 of a symbol, and 7x the prize if you get all the same symbol.")
Playa = input("Ready? ").lower()  # Convert input to lowercase for comparison
if Playa == "no":
  quit()  # Call the quit function
elif Playa == "yes":
  print("great. Spinning...")
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
  elif roll1 == "BAR":  # Changed to "BAR" as per Icons list
    Val1 = 0

  if roll2 == "🍔":
    Val2 = 1
  elif roll2 == "🍕":
    Val2 = 2
  elif roll2 == "🍛":
    Val2 = 3
  elif roll2 == "7":
    Val2 = 7
  elif roll2 == "BAR":  # Changed to "BAR" as per Icons list
    Val2 = 0

  if roll3 == "🍔":
    Val3 = 1
  elif roll3 == "🍕":
    Val3 = 2
  elif roll3 == "🍛":
    Val3 = 3
  elif roll3 == "7":
    Val3 = 7
  elif roll3 == "BAR":  # Changed to "BAR" as per Icons list
    Val3 = 0

  total = Val1 + Val2 + Val3
  if Val1 == Val2 and Val2 == Val3:
    total *= 7  # Assign the result back to total
  elif Val1 == Val2 or Val2 == Val3 or Val1 == Val3:  # Check all possible pairs
    total *= 3  # Assign the result back to total
  print(f"You won ${total}")
