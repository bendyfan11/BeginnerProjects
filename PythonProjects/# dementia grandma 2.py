# dementia grandma 2
import random
import time

class Game:
    def __init__(self):
        self.cookies = 0
        self.sanity = 100
        self.suspicion = 0
        self.sleigh_cookies = 0
        self.eaten_cookies = 0
    def startup(self):
        print("You are santa clause.")
        time.sleep(1)
        print("Grandma has cookies.")
        time.sleep(1)
        print("And you are very hungry.")
        time.sleep(1)
        print("Steal grandma's cookies Without being caught.")
    def steal(self):
        if self.sanity - self.suspicion > random.randint(1, 100):
            stolen = random.randint(1, 5)
            self.cookies += stolen
            self.suspicion += 10
            print(f"You stole {stolen} cookies. Grandma is getting suspicious...")
            time.sleep(5)
            print("Grandma has forgotten you are there. You may steal again.")
        elif self.cookies == 0:
            print("Grandma has cought you red handed.")
            print("She pulls out a 12 gauge and shoots you in the face. You lose.")
            exit()
        else:
            self.suspicion -= 5
            self.cookies -= 1
            print("You got caught stealing a cookie! Grandma is less suspicious now. -1 cookie.")
    def shop(self):
        print("Welcome to the black market, clause.")
        print(f"you have {self.cookies} cookies.")
        print("You can buy a beer, or a mystery box. pick one.")
        choice = input(">")
        if choice == "beer" and self.cookies >= 10:
                self.cookies -= 10
                self.sanity += 20
                print("You bought a beer. Your sanity is restored.")
        elif choice == "mystery box" and self.cookies >= 20:
                self.cookies -= 20
                self.open_mystery_box()
        else:
                print("You don't have enough cookies or invalid choice. SCRAM.")
    def open_mystery_box(self):
        outcome = random.randint(1, 4)
        
        if outcome == 1:
            self.suspicion = 0
            print("The present was a distraction! Suspicion is back to 0.")
        elif outcome == 2:
            extra = random.randint(1, 15)
            self.cookies += extra
            print(f"The present was full of... cookies? You got {extra} more!")
        elif outcome == 3:
            self.suspicion += 14
            print("The present made a loud noise! Grandma is looking around...")
        else:
            lost = random.randint(1, 3)
            self.cookies = max(0, self.cookies - lost)
            print(f"A trap! A mechanical hand stole {lost} cookies from you.")
    def check_status(self):
         print(f"you pull up your stat watch. You have {self.cookies} cookies, {self.sanity} sanity, and grandma is about {self.suspicion}% suspicious of you.")
    def deliver_to_sleigh(self):
        if self.cookies > 0:
            print(f"You sneak out to the sleigh and drop off {self.cookies} cookies.")
            self.sleigh_cookies += self.cookies
            self.cookies = 0
            self.suspicion += 5
        else:
            print("you have nothing to deliver but shame... You ponder for a moment.")
            self.suspicion -= 5
            time.sleep(10)
    def eat_cookie(self):
        if self.cookies > 0:
            amt = int(input(f"How many? (Inventory: {self.cookies}): "))
            amt = min(amt, self.cookies)
            self.cookies -= amt
            self.eaten_cookies += amt
            self.sanity += (amt * 2)
            print(f"Nom nom nom. You ate {amt} cookies. Sanity restored, but your heart is racing.")
        else:
            print("No cookies to eat. You chew on your beard instead.")
    def play(self):
        self.startup()
        while True:
            if self.sleigh_cookies >= 100:
                print("Congratulations. Your infernal cookie lust has been sated. You win.")
                exit()
            if self.eaten_cookies >= 500:
                print("upon eating your 500th cookie, your blood courses with sugar. You have contracted type 9 diabetes. It kills you instantly. You lose.")
                exit()
            if self.sanity <= 0:
                print("\nYou've lost your mind. You start singing carols at the top of your lungs. Grandma hears everything. *BANG*")
                exit()
            action = input("\nWhat will you do? (steal / deliver / eat / shop / check): ").lower()           
            if action == "steal":
                    self.steal()
            elif action == "deliver":
                    self.deliver_to_sleigh()
            elif action == "eat":
                    self.eat_cookie()
            elif action == "shop":
                    self.shop()
            elif action == "check":
                self.check_status()
            else:
                    print("Santa doesn't have time for that!")

            time.sleep(1)
if __name__ == "__main__":
    game = Game()
    game.play()