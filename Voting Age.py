numput = int(input("Enter a number: "))
if (numput % 2 == 0):
    print(f"your number is even {numput}")
else:
    print(f'your number is odd')
votingage = int(input("What is your age:"))
if (votingage >= 18):
    print('You can vote now')
else:
    print("Sorry, you cannot vote")
username = input("what is your name: ")

def My_user(username):
    print(f'Hello {username}')

My_user(username)