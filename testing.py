s = "Magic invention wonder"
# Length should be 22
print(f"the length of s is {len(s)}")

# First occurrence of "a" should be at index 1
print(f"The first occurrence of the letter a = {s.index("a")}")

# Number of a's should be 1
print(f"a occurs {s.count("a")} times")

# Slicing the string into bits
print(f"The first five characters are {s[0:5]}") # Start to 5
print(f"The next five characters are {s[5:10]}") # 5 to 10
print(f"The thirteenth character is {s[12]}") # Just number 12
print(f"the characters with odd index are {s[0::2]}") #(0-based indexing)
print (f"the last five characters are {s[-5:]}")

# Convert everything to uppercase
print(f"String in uppercase: {s.upper()}")
# Convert everything to lowercase
print(f"String in lowercase: {s.lower()}")

# Check how a string starts
if s.startswith ("Mag"):
    print(f"goood job pri it started with {s[0:3]}")

# Check how a string ends
if s.endswith ("der"):
    print(f"good job ulet it ended with {s[-3:]}")

# Split the string into three separate strings,
# each containing only a word
print(f"Split the words of the string {s.split(" ")}")
