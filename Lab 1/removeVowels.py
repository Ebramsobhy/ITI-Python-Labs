# Write a program that remove all vowels from the input word and generate a brief version of it.

string = "Ebram"

vowels = ['a', 'e', 'i', 'o']
result = ""

for char in string:
    if char not in vowels:
        result = result + char

print("After removing Vowels: ", result)
          
       