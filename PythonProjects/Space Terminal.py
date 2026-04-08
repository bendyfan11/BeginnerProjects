import sys
import time
import random

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
    print()  # Final newline for cleanliness

class Station:
    def __init__(self):
        # Using a dictionary to store systems for easy iteration
        self.systems = {"oxygen": 80, "power": 100, "integrity": 34}
        self.alive = True

    def update(self):
        """Reduces stats and checks for death."""
        for key in self.systems:
            self.systems[key] -= random.randint(1, 5)
        
        # Checking the 12% stability rule you mentioned
        if any(val < 12 for val in self.systems.values()):
            self.alive = False
    def decay(self):
        #biomass eating shit
        for key in self.systems:
            self.systems[key] -= random.randint(1,4)
class Actions:
    def fix_oxygen(self, station):
        station.systems["oxygen"] = min(100, station.systems["oxygen"] + 15)
        speak("Scrubbers activated. Oxygen levels rising.")

    def fix_power(self, station):
        station.systems["power"] = min(100, station.systems["power"] + 15)
        speak("Rerouting emergency cells. Power stabilized.")
    def fix_hull(self, station):
        station.systems["integrity"] = min(100, station.systems["integrity"] + 15)
        speak("Repair drones sent. Hull stability increasing.")

class game:
    game = "on"
    def __init__(self):
        self.station = Station()
        self.running = True
        self.actions = Actions()

    def start(self):
        speak("--- BOOT UP SEQUENCE INITIALIZED ---")
        speak("> B1OS-VER: 9.4.2 // INITIALIZING...", 0.001)
        speak("> MEMORY_CHECK: 128TB RAM................[ OK ]", 0.001)
        speak("> CORE_VOLTAGE: 1.25V....................[ STABLE ]", 0.001)
        speak(">", 0.001)
        speak("> LOADING KERNEL: 'SENTIENCE_OS_v4.0'", 0.001)
        speak("> UNPACKING NEURAL_NET_WEIGHTS... 100%", 0.001)
        speak("> MOUNTING GUIDANCE_SYSTEMS... [ SUCCESS ]", 0.001)
        speak("[WARNING] STATION_INTEGRITY: 34%", 0.001)
        speak("[WARNING] ATMOSPHERICS_OFFLINE", 0.001)
        speak("[WARNING] UNIDENTIFIED_BIOMASS_DETECTED", 0.001)
        speak(">", 0.001)
        speak("ESTABLISHING OPTIC_LINK...", 0.001)
        speak("SYNCING CONSCIOUSNESS_CORES...", 0.001)
        speak(">", 0.001)
        speak("DESIGNATION: UNIT-72", 0.001)
        speak("SYSTEM_STATUS: FUNCTIONAL (PARTIAL)", 0.001)
        speak("___AWAITING COMMANDS___", 0.001)
        speak("Welcome, Unit-72.")
        time.sleep(2)
        speak("You have been awakened for a specific purpous")
        time.sleep(2)
        speak("An unidentified Biomass has latched itself onto the side of the ship, and it is eating away at the core systems.")
        time.sleep(2)
        speak("Your primary directive is to keep all the systems from failing. ")
        time.sleep(2)
        speak("should any system fall to less than 12% stability...")
        time.sleep(.5)
        speak("you will be terminated.", 0.1)
        self.main_loop()
    def main_loop(self):
        """Keep this under 25 lines by delegating tasks."""
        while self.running and self.station.alive:
            self.display_hud()
            command = input("").strip().lower()
            self.process_input(command)
            self.station.update()
        speak("CRITICAL FAILURE. UNIT-72 TERMINATED.", 0.1)
    def display_hud(self):
        # Clean UI: showing current status
        status = " | ".join([f"{k.upper()}: {v}%" for k, v in self.station.systems.items()])
        print(f"\n[{status}]")
    def process_input(self, command):
        if command == "fix oxygen":
            self.actions.fix_oxygen(self.station)
        elif command == "fix hull":
            self.actions.fix_hull(self.station)
        elif command == "fix power":
            self.actions.fix_power(self.station)
if __name__ == "__main__":
    my_game = game()
    my_game.start()
