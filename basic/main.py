
import json
import os


with open("level_1_character.json", "r") as file:
    character = json.load(file)


character["level"] += 1
character["armor_class"] += 1


character["attributes"]["strength"] += 2
character["attributes"]["constitution"] += 1

character["skills"].append("Survival")
character["weapons"].append("Silver Dagger")


with open("level_2_character.json", "w") as file:
    json.dump(character, file, indent=4)

print("Character successfully leveled up!")
print("Updated character saved to level_2_character.json")



# Ask for the current character level
while True:
    try:
        current_level = int(input("Enter the character's current level: "))

        if current_level < 1:
            print("Level must be at least 1.")
            continue

        input_file = f"level_{current_level}_character.json"

        if not os.path.exists(input_file):
            print(f"Error: {input_file} does not exist.")
            continue

        break

    except ValueError:
        print("Invalid input. Enter a whole number.")

# Load the character
try:
    with open(input_file, "r") as file:
        character = json.load(file)

    if not isinstance(character, dict):
        raise ValueError("Character data must be a JSON object.")

    required_keys = ["level", "armor_class", "attributes", "skills", "weapons"]

    for key in required_keys:
        if key not in character:
            raise ValueError(f"Missing required field: {key}")

    if not isinstance(character["attributes"], dict):
        raise ValueError("Attributes must be a dictionary.")

    if not isinstance(character["skills"], list):
        raise ValueError("Skills must be a list.")

    if not isinstance(character["weapons"], list):
        raise ValueError("Weapons must be a list.")

    # Define the six possible attributes
    attributes = [
        "strength",
        "dexterity",
        "constitution",
        "intelligence",
        "wisdom",
        "charisma"
    ]

    # Check that the attributes exist
    for attribute in attributes:
        if attribute not in character["attributes"]:
            raise ValueError(f"Missing attribute: {attribute}")

    # Increase level and armor class
    character["level"] += 1
    character["armor_class"] += 1

    # Ask which attribute to improve
    while True:
        print("Available attributes:", ", ".join(attributes))
        chosen_attribute = input(
            "Which attribute do you want to increase? "
        ).strip().lower()

        if chosen_attribute in attributes:
            character["attributes"][chosen_attribute] += 1
            break

        print("Invalid attribute. Choose one from the list.")

    # Add a new skill
    while True:
        skill = input("Enter a new skill: ").strip()

        if skill:
            character["skills"].append(skill)
            break

        print("Skill cannot be empty.")

    # Ask whether to add a weapon
    while True:
        answer = input("Add a new weapon? (yes/no): ").strip().lower()

        if answer in ["yes", "no", "y", "n"]:
            break

        print("Invalid response. Enter yes or no.")

    if answer in ["yes", "y"]:
        while True:
            weapon = input("Enter the weapon name: ").strip()

            if weapon:
                character["weapons"].append(weapon)
                break

            print("Weapon name cannot be empty.")

    # Save using the new character level
    new_level = character["level"]
    output_file = f"level_{new_level}_character.json"

    with open(output_file, "w") as file:
        json.dump(character, file, indent=4)

    print(f"Character successfully leveled up to level {new_level}!")
    print(f"Updated character saved to {output_file}")

except (FileNotFoundError, json.JSONDecodeError, ValueError,
        TypeError, KeyError, OSError) as error:
    print(f"Error: {error}")

