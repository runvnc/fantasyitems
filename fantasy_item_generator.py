import random
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Lists for item generation
item_types = ['Sword', 'Staff', 'Amulet', 'Ring', 'Potion', 'Scroll', 'Wand', 'Bow', 'Shield', 'Armor']
materials = ['Mithril', 'Dragonbone', 'Elven Silver', 'Dwarven Gold', 'Shadowsteel', 'Celestial Bronze', 'Fae Wood']
magical_properties = ['Flaming', 'Frost', 'Thunderous', 'Venomous', 'Radiant', 'Ethereal', 'Vampiric', 'Arcane', 'Mystic']

def generate_fantasy_item():
    item_type = random.choice(item_types)
    material = random.choice(materials)
    property = random.choice(magical_properties)
    
    # Color mapping for magical properties
    color_map = {
        'Flaming': '\033[38;5;196m',  # bright red
        'Frost': '\033[38;5;51m',    # lighter blue
        'Thunderous': '\033[38;5;226m',  # yellow
        'Venomous': '\033[38;5;46m',  # green
        'Radiant': '\033[38;5;255m',  # brighter white
        'Ethereal': '\033[38;5;81m',  # light cyan
        'Vampiric': '\033[38;5;52m',  # dark red
        'Arcane': '\033[38;5;201m',   # magenta
        'Mystic': '\033[38;5;93m'    # purple
    }
    
    return f"{color_map[property]}{property} {Fore.YELLOW}{material} {Fore.MAGENTA}{item_type}{Style.RESET_ALL}"

print(Fore.GREEN + "=== Magical Item Generator ===")
for i in range(5):
    print(f"{Fore.WHITE}Item {i+1}: {generate_fantasy_item()}")
