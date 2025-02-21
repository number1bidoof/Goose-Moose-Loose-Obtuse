input_string = input("Enter anything that is a string :): ")

def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    print(f'there are {count} amount of vowels in this still')


count_vowels(input_string)