numbers = [1,2,3,4,5,6,7,8,9]

def find_highest_number(x):
    highest = x[0]
    for i in x:
        if i > highest:
            highest = i
    print(f"The highest number is: {find_highest_number(numbers)}")


find_highest_number(numbers)