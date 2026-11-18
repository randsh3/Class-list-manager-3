# Class List Manager - Group 3
# MIS 211 Bonus Assignment (GitHub Teamwork)
names = ["Sara", "Noura", "Lama", "Reem", "Amal", "Lama"]
# ===== Each student adds her function BELOW this line =====

# Written by: Rand (task 1)
def count_names(names):
    return len(names)
    
    # Written by: Rand (task 2)
def search_name(names, name):
    for student in names:
        if student.lower() == name.lower():
            return True
    return False
    
# Written by: Rand (task 3)
def sort_names(names):
    return sorted(names)

# Written by: Rand (task 4)
def longest_name(names):
    longest = names[0]
    for name in names:
        if len(name) > len(longest):
            longest = name
    return longest

# Written by: Rand (task 5)
def names_starting_with(names, letter):
    result = []
    for name in names:
        if name.lower().startswith(letter.lower()):
            result.append(name)
    return result
    
# Written by: Rand (task 6)
def to_upper(names):
    result = []
    for name in names:
        result.append(name.upper())
    return result
    
# Written by: Rand (task 7)
def count_vowels(name):
    count = 0
    for letter in name.lower():
        if letter in "aeiou":
            count += 1
    return count
    
# Written by: Rand (task 8)
def remove_duplicates(names):
    unique_names = []
    for name in names:
        if name not in unique_names:
            unique_names.append(name)
    return unique_names

def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    print("Number of names:", count_names(names))
    print("Is Noura in the list?", search_name(names, "Noura"))
    print("Names in alphabetical order:", sort_names(names))
    print("Longest name:", longest_name(names))
    print("Names starting with L:", names_starting_with(names, "L"))
    print("Names in uppercase:", to_upper(names))
    print("Number of vowels in Sara:", count_vowels("Sara"))
    print("List without duplicates:", remove_duplicates(names))



main()
