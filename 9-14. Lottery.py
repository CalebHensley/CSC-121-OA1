import random

lottery_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

lottery_numbers = random.sample(lottery_choices, 4) + random.sample(lottery_choices[10:], 1)

user_input = input("Enter 4 numbers and a letter from A and E to enter the lottery:")

if list(user_input) == lottery_numbers:
    print("Congratulations! You are a winner!")
else:
    print("Sorry, you did not win.")