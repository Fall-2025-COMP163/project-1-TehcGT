"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Tehcubelleh Keamu
Date: 10/29/2025

AI Usage: Mainly used AI for debugging in all functions
"""

def create_character(name, character_class):
  
    valid_classes = ["Warrior", "Mage","Rogue","Cleric"]
    if character_class not in valid_classes:
        return None
    
    character_name = ""
    if name is not None:
        character_name = name.strip()
    level = 1
    strength, magic, health = calculate_stats(character_class, level)

    
    character = {"name":character_name.strip(), "class":character_class, "level":1,"strength":strength,"magic":magic,"health":health,"gold": 100}
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


    strength += (level - 1) * 3
    magic += (level - 1) * 2
    health += (level - 1) * 10
    #purpose of the 3 codes above me is to make my character stronger after level 1
    return strength, magic, health

def save_character(character, filename): #Main purpose is to take the character's data and saves it to a text file on my hard drive
    import os
    if character == None:
        return False
    
    folder = os.path.dirname(filename)
    if folder and not os.path.exists(folder):
        return False
    
    with open(filename,"w", encoding="utf-8") as f: #I used a with because mainly because I knew I would forget to add the ".close()" function when addong all these lines of code
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
    
    f = open(filename, "r", encoding="utf-8") #encoding = "utf-8" was included because I used copilot and Gemini which told me that it handles special characters like letters with an accent line
    lines = f.readlines() #Reading the lines to a list for branching
    f.close()

    character = {}
    for line in lines:  
        if ":" not in line:
            continue

        key, value = line.strip().split(":", 1)
        key = key.strip().lower().replace("character ", "")

        value = value.strip()

        if value.isdigit():
            value = int(value)
        character[key] = value

    if len(character) == 0:
        return None
    
    return character

def display_character(character):
    print("\n=== CHARACTER SHEET ===")
    print(f"Name: {character.get("name", "")}")
    print(f"Class: {character.get("class", "")}")
    print(f"Level: {character.get("level", 0)}")
    print(f"Strength: {character.get("strength", 0)}")
    print(f"Magic: {character.get("magic", 0)}")
    print(f"Health: {character.get("health", 0)}")
    print(f"Gold: {character.get("gold", 0)}")


def level_up(character):
    character["level"] +=1
    strength,magic,health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    print(f"\n{character["name"]} leveled up to Level {character["level"]}!")



if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
