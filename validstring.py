"""
Question
- Accept a String input
- Accept a String of valid chars
- Remove all the characters that are not present in the valid chars from the input string
- Print the cleansed String and the count of characters removed
Eg. If the String input is
The name of my dog is #2#Tiger
and the valid chars is abcdefghijklmnopqrstuvwxyz
then the output should be as below
The name of my dog is Tiger
2 # was removed
1 2 was removed

"""

print("Enter a String:")
s = input()
print("Enter string of valid characters: ")
valid = set(input())        # set uses hashing so faster search

for char in valid.copy():
    valid.add(char.upper()) # Add upper cases of provided chars
    valid.add(char.lower()) # Add lower cases of provided chars
valid.add(" ")  # Apparently , Space is always considered valid
removeCount = {}        #dictionary to store count of removed characters

newstr = ""     #new string with only valid characters
for char in s:          #in this loop each character input string is compared with valid string 
    if char in valid:   #if char belongs to valid , it is added to result string
        newstr+=char
    else:               #if not the removecount dictionary is updated by 1
        if char in removeCount.keys():
            removeCount[char]+=1
        else:
            removeCount[char]=1

print(newstr)
for char in removeCount.keys():
    print("{} times {} was removed".format(removeCount[char],char))
