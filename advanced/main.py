
import json

while True:
    try:
        level = int(input("What level is your character? "))

        if level < 1:
            print("Enter a level above 0.")
        else:
            with open(f"level_{level}_character.json", "r") as file:
                character = json.load(file)
            break

    except ValueError:
        print("Enter a valid number.")
    except FileNotFoundError:
        print("Character file not found.")

character["level"] += 1
character["armor_class"] += 1

attributes = [
    "strength", "dexterity", "constitution",
    "intelligence", "wisdom", "charisma"
]

while True:
    attribute = input("Which attribute do you want to increase? ").lower()

    if attribute in attributes:
        character["attributes"][attribute] += 1
        break
    else:
        print("Invalid attribute.")

skill = input("Enter a new skill: ")
character["skills"].append(skill)

while True:
    answer = input("Add a weapon? (yes/no): ").lower()

    if answer == "yes":
        weapon = input("Enter the weapon name: ")
        character["weapons"].append(weapon)
        break
    elif answer == "no":
        break
    else:
        print("Enter yes or no.")

new_level = character["level"]

with open(f"level_{new_level}_character.json", "w") as file:
    json.dump(character, file, indent=4)

print("Character leveled up!")
