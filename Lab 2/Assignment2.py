# Character Locator 

def find_indexes(string, char):
    indexes = []
    for i, c in enumerate(string):
        if c == char:
            indexes.append(i)
    return indexes

my_string = input("Enter a string: ")
char = input("Enter a character: ")

indexes = find_indexes(my_string, char)

print(indexes)
