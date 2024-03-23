# Scenario 1: The Haunted House
print("You find yourself standing in front of a spooky old house. What do you do?")
choice1 = input("ENTER THE HOUSE or TURN AROUND AND LEAVE: ").upper()

if choice1 == "ENTER THE HOUSE":
    print("You cautiously push open the creaky door and step into the dark foyer. What's your next move?")
    choice2 = input("EXPLORE THE GROUND FLOOR or HEAD UPSTAIRS: ").upper()
    
    if choice2 == "EXPLORE THE GROUND FLOOR":
        print("You wander through the dusty rooms, but find nothing of interest. Suddenly, you hear a faint noise coming from upstairs.")
    elif choice2 == "HEAD UPSTAIRS":
        print("You climb the creaky stairs, heart pounding with each step. At the top, you find a locked door.")
    else:
        print("Sorry, that's not a valid choice.")

elif choice1 == "TURN AROUND AND LEAVE":
    print("You decide it's best not to tempt fate and turn away from the house. What's your next move?")
    choice2 = input("WANDER INTO THE FOREST or RETURN HOME: ").upper()
    
    if choice2 == "WANDER INTO THE FOREST":
        print("You venture into the dark forest, feeling a sense of unease.")
    elif choice2 == "RETURN HOME":
        print("You head back home, relieved to be away from the creepy house.")
    else:
        print("Sorry, that's not a valid choice.")

else:
    print("Sorry, that's not a valid choice.")


# Scenario 2: The Enchanted Forest
print("\nYou stumble upon a mystical forest filled with strange creatures and glowing plants. What's your next move?")
choice1 = input("FOLLOW THE PATH or STRAY OFF THE PATH: ").upper()

if choice1 == "FOLLOW THE PATH":
    print("You tread carefully along the winding path, mesmerized by the beauty of the forest. Suddenly, you come to a fork. What do you do?")
    choice2 = input("TAKE THE LEFT FORK or TAKE THE RIGHT FORK: ").upper()
    
    if choice2 == "TAKE THE LEFT FORK":
        print("You follow the left fork and discover a hidden waterfall.")
    elif choice2 == "TAKE THE RIGHT FORK":
        print("You take the right fork and encounter a friendly forest spirit.")
    else:
        print("Sorry, that's not a valid choice.")

elif choice1 == "STRAY OFF THE PATH":
    print("You venture off into the unknown, curious about what secrets the forest holds. After some time, you stumble upon a hidden clearing. What do you do?")
    choice2 = input("INVESTIGATE THE CLEARING or RETURN TO THE PATH: ").upper()
    
    if choice2 == "INVESTIGATE THE CLEARING":
        print("You find a magical artifact hidden in the clearing.")
    elif choice2 == "RETURN TO THE PATH":
        print("You decide to stick to the safety of the path and continue your journey.")
    else:
        print("Sorry, that's not a valid choice.")

else:
    print("Sorry, that's not a valid choice.")


# Scenario 3: The Underground Cavern
print("\nYou discover an entrance to a dark, mysterious cavern hidden beneath the earth. What's your next move?")
choice1 = input("DESCEND INTO THE CAVERN or SEAL THE ENTRANCE AND LEAVE: ").upper()

if choice1 == "DESCEND INTO THE CAVERN":
    print("You gather your courage and begin your descent into the depths of the cavern. As you go deeper, you hear strange noises echoing from the darkness. What do you do?")
    choice2 = input("FOLLOW THE NOISES or KEEP MOVING FORWARD: ").upper()
    
    if choice2 == "FOLLOW THE NOISES":
        print("You follow the eerie sounds and come face to face with a terrifying creature.")
    elif choice2 == "KEEP MOVING FORWARD":
        print("You press on, determined to uncover the secrets of the cavern.")
    else:
        print("Sorry, that's not a valid choice.")

elif choice1 == "SEAL THE ENTRANCE AND LEAVE":
    print("You decide it's best not to risk whatever dangers lie within the cavern and seal the entrance behind you. What's your next move?")
    choice2 = input("RETURN TO THE SURFACE or EXPLORE THE SURROUNDING AREA: ").upper()
    
    if choice2 == "RETURN TO THE SURFACE":
        print("You return to the surface, grateful to have escaped the darkness of the cavern.")
    elif choice2 == "EXPLORE THE SURROUNDING AREA":
        print("You decide to explore the area around the cavern, hoping to find clues about its mysterious inhabitants.")
    else:
        print("Sorry, that's not a valid choice.")

else:
    print("Sorry, that's not a valid choice.")
