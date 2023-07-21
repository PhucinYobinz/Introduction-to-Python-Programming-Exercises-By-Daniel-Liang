import random

# Prompt user to select a 3-digit lottery number
userLotteryNumber = int(input("Enter a 3-digit Lottery number: "))

# Generate a random 3-digit Lottery number
lotteryNumber = random.randint(100, 999)

# Convert both numbers to strings and sort their digits
user_lottery_str = sorted(str(userLotteryNumber))
lottery_str = sorted(str(lotteryNumber))

# Check if one digit matches in the lottery number
matching_digits = set(user_lottery_str).intersection(lottery_str)

print("Your lottery number:", userLotteryNumber)
print("Winning lottery number:", lotteryNumber)

if user_lottery_str == lottery_str:
    print("Winner! Lottery number has the same digits but in different order. Prize is $5,000!")
elif userLotteryNumber == lotteryNumber:
    print("Winner! Lottery number is an exact match. Prize is $10,000!")
elif matching_digits:
    print("Congratulations! One digit matches. Prize is $1,000!")
else:
    print("Sorry, no matches. Better luck next time!")
