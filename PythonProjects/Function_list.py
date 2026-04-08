import random
import time
import sys
import os

def speak(text, delay=0.05):
    """
    Prints text to the terminal letter-by-letter.
    :param text: The string to be printed.
    :param delay: Seconds between each character (default 0.05).
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def clear_screen():
    """Clears the terminal screen based on the OS."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_choice(prompt, options):
    """
    Forces the user to pick from a specific list of options.
    :param prompt: The question to ask.
    :param options: A list of valid string responses.
    """
    while True:
        user_input = input(f"{prompt} ({'/'.join(options)}): ").lower().strip()
        if user_input in options:
            return user_input
        print(f"Invalid input. Please choose from: {', '.join(options)}")

def loading_spinner(duration, text="loading"):
    """
    Displays a simple spinning line for a set duration.
    :param text: The text to be displayed.
    :param duration: Duration in seconds.
    """
    chars = ['|', '/', '-', '\\']
    end_time = time.time() + duration
    while time.time() < end_time:
        for char in chars:
            sys.stdout.write(f'\r{text} {char}')
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write('\rDone!     \n')

def RTD(amount, sides, modifier=0):
    """
    Rolls the dice. [0] = Total, [1] = Amount, [2] = Sides, [3] = Modifier
    :param amount: The amount of dice to roll.
    :param sides: The number of sides each die has.
    :param modifier: An optional integer to add or subtract to the roll.
    """
    total = 0
    for i in range(amount):
        roll = random.randint(1, sides)
        total += roll
    
    final_result = total + modifier
    return final_result, amount, sides, modifier
        

    
if __name__ == "__main__":
    speak("Utility Test")
    speak("Testing the speak function...")
    time.sleep(2)
    clear_screen()
    speak("Testing the clear_screen function... You'll know if it worked.")
    get_choice = get_choice ("Does this work?", ["yes", "no", "mayhaps"])
    speak (f"{get_choice}? Okay sounds about right.")
    speak(f"Please wait while we definitly upload things...")
    loading_spinner(6, "uploading")
    speak("okay lets test RTD")
    val = RTD (6,15,1)
    speak(f"Rolling {val[1]}d{val[2]} + {val[3]} ...")
    speak(f"{val[0]}")