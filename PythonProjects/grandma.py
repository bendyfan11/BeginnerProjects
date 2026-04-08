

# cookie clicker but bad

import random
import time

print("You are santa. you must retrive cookies from grandma before she gets wise.")
print("Grandma has dementia. She will forget you are there after 5 seconds.")
cookies = 0
eaten = 0
sanity = 100
delivered = 0
elf = 0
while True:
    print(f"You now have {cookies} cookies.")
    steal = input(f"Press enter to steal cookies. alternatively, you may eat a cookie. Or deliver some to the stash. You have delivered {delivered} cookies to the stash. ")
    if "deliver" in steal:
        if cookies > 0:
            delivered += cookies
            print(f"You deliver {cookies} cookies to the stash. You have delivered {delivered} cookies to the stash.")
            cookies = 0
        else:
            print("You have no cookies to deliver.")
    if steal == "":
        police = random.randint(0, 10)
        if police == 0:
            print("Grandma has caught you stealing cookies. -1 cookie.")
            if cookies > 0:
                cookies -= 1
                sanity -= 10
            else: 
                print("You have no cookies to lose.")
                print("Grandma shoots you. You Died.")
                break
        if elf > 0:
            for i in range(elf):
                stolenElf = random.randint(0, 4)
                print(f"Your elf steals {stolenElf} cookies.")
                sanity += 5
                cookies += stolenElf
        stolen = random.randint(0, 4)
        print(f"You steal a cookie. You stole {stolen} cookies.")
        sanity += 5
        cookies += stolen
        time.sleep(5)
        print("Grandma has forgotten you are there and baked more cookies. You can steal again.")
    if "eat" in steal:
        if cookies > 0:
            cookies -= 1
            eaten += 1
            sanity += 2
            print(f"You eat a cookie. You have {cookies} cookies left. Yum")
            print(f"You have eaten {eaten} cookies.")

        else:
            print("You have no cookies to eat.")
    if eaten == 500:
        print("you have obtained diabetes. you Died.")
        break
    if sanity <= 0:
        print("everything is shaking... it's all too much. You pass out.")
        break
    if delivered >= 100:
        print("you have delivered enough cookies to the stash. You win!")
        break
    if steal == "store":
        store = input(f"WELCOME TO THE STORE! You may buy sla- ... willing workers... to steal for you, for 10 cookies. you have {elf} elves. press 1 to buy an elf. or 0 to exit the store. ")
        if store == "1":
            if cookies >= 10:
                cookies -= 10
                elf += 1
                print(f"You have bought an elf. You now have {elf} elves.")
            else:
                print("You do not have enough cookies to buy an elf.")
        elif store == "0":
            print("Exiting the store.")
        else:
            print("Invalid input. Exiting the store.")