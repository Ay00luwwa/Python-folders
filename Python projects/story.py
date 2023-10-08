print("Please fill in the blanks to complete the story:\n")

name = input("Enter your name: ")
age = input("Enter your age: ")
hobby = input("Enter a hobby: ")
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
verb1 = input("Enter a verb: ")
noun1 = input("Enter a noun: ")
city = input("Enter a city: ")
verb2 = input("Enter a verb in past tense: ")
adverb = input("Enter an adverb: ")
noun2 = input("Enter a noun: ")
emotion = input("Enter an emotion: ")

story = f"\nMy name is {name} and I am {age} years old.\nIn my free time, I love to {hobby}.\nI am a/an {adjective1} and {adjective2} person who likes to {verb1} and spend time with my {noun1}.\nOne day, I decided to take a trip to {city} to {verb2} the sights.\nAs I was walking through the city, I {adverb} heard a loud noise coming from a nearby {noun2}.\nFeeling {emotion}, I went to investigate and discovered a group of people playing music.\nThat moment made me realize that sometimes the most beautiful things in life come when we least expect it."

print(story)