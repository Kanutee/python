# Mad Libs program with additional words and "a" or "an" usage

# Ask the user for words
adjective = input("Enter an adjective: ")
animal = input("Enter an animal: ")
verb_one = input("Enter a verb: ")
exclamation = input("Enter an exclamation: ")
verb_two = input("Enter the second verb: ")
verb_three = input("Enter the third verb: ")

# Additional creative addition: Ask the user for a color
color = input("Enter a color: ")

# Display the story with user's words
output = f'''The other day, I was really in trouble. It all started when I saw a very
    {adjective} {animal} {verb_one} down the hallway. "{exclamation}!" I yelled. But all
    I could think to do was to {verb_two} over and over. Miraculously,
    that caused it to stop, but not before it tried to {verb_three} right in front of my family.
    The whole scene looked even more chaotic with splashes of {color} everywhere.'''

print("\nYour Creative Mad Libs story:\n")
print(output)
