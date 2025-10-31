"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Tehcubelleh Keamu
Date: 10/29/2025

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""

def create_character(name, character_class):
  
    valid_classes = ["Warrior", "Mage","Rogue","Cleric"]
    level = 1
    strength, magic, health = calculate_stats(character_class, level)
    
    if character_class not in valid_classes:
        return None
    
    character = {"name":name.strip(), "class":character_class, "level":1,"strength":strength,"magic":magic,"health":health,"gold": 100}
    return character


def calculate_stats(character_class, level):
    
    character_class = character_class.upper()
    strength = 0
    magic = 0
    health = 50

    if character_class == "ROGUE":
        strength += 50
        magic += 45
        health += 30
    elif character_class == "CLERIC":
        strength += 55
        magic += 90
        health += 95
    elif character_class == "WARRIOR":
        strength += 95
        magic += 30
        health += 90
    elif character_class == "MAGE":
        strength += 30
        magic += 100
        health += 55
    else:
        print("invalid trope")
    return strength, magic, health

def save_character(character, filename):
    import os
    if character == None:
        return False
    
    folder = os.path.dirname(filename)
    if folder and not os.path.exists(folder):
        return False
    
    with open(filename,"w") as f:
        f.write(f"Character Name: {character["name"]}\n")
        f.write(f"Class: {character["class"]}\n")
        f.write(f"Level: {character["level"]}\n")
        f.write(f"Strength: {character["strength"]}\n")
        f.write(f"Magic: {character["magic"]}\n")
        f.write(f"Health: {character["health"]}\n")
        f.write(f"Gold: {character["gold"]}\n")
    return True

def load_character(filename):
    import os
    if not os.path.exists(filename):
        return None
    
    f = open(filename, "r")
    line = f.readlines()
    f.close()

    character = {}
    for l in line:  
        if ":" not in line:
            continue

        key,value = line.strip().split(":", 1)
        key = key.lower().replace("character ", "")
        if value.isdigit():
            value = int(value)
        character[key] = value

        if len(character) == 0:
            return None
        return character

def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    # TODO: Implement this function
    pass

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    pass

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
