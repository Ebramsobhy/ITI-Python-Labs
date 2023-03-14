# Bonus:You can make a function like replace Fn. but takes list of strings instead of one string. 

def removeVowles(word):
    vowels = ['a', 'e', 'i', 'o']
    brief = word
    for letter in vowels:
        brief = brief.replace(letter, '')
    return brief

word = input("Enter a word: ")
print("Result:", removeVowles(word))