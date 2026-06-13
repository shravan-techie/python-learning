from faker import Faker

fake = Faker()  # for generating random values

story = f"{fake.name()} once upon a time was living in {fake.country()}"

print(story)

print("First Character: " + story[0])  # accessing first character
print("Last Character: " + story[-1])  # accessing last character

# accessing the first 3 characters
print("First 3 Charas Substring: " + story[0:3])

# accessing the last 3 characters
print("Last 3 Charas Substring: " + story[-3:])

print("Copy of the String: " + story[:])   # copy of string

print(f"Length of String: {len(story)}")

# case conversion
print("Uppercase: " + story.upper())
print("Lowercase: " + story.lower())
print("Title case: " + story.title())

# search and replace
print("Contains 'once'?: " + str("once" in story))
print("First occurrence of 'once':", story.find("once"))
print("Replaced string: " + story.replace("once upon a time", "once"))

# split and join
words = story.split()
print("Words count:", len(words))
print("Joined back:", "-".join(words[:]))

# strip and character checks
sample = "   hello world   "
print("Strip sample: '" + sample.strip() + "'")
print("Starts with 'A'?:", story.startswith("A"))
print("Ends with '.'?:", story.endswith("."))
print("Count of letter 'a':", story.count("a"))
