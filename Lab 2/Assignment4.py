"""
Write a program convert a list of names into sorted dictionary which key is the Alpha.
and value is a list of names corresponding to this alpha.

"""
def sort_names(names):
    dict = {}
    for name in names:
        first_letter = name[0]
        if first_letter in dict:
            dict[first_letter].append(name)
        else:
            dict[first_letter] = [name]
    dict = {k: sorted(v) for k, v in dict.items()}
    return dict

input_str = input("Enter a list of names")
names = [name.strip() for name in input_str.split(",")]

sorted_names = sort_names(names)
print(sorted_names)