# Computer Number is random
import random

random_number = random.randint(1, 100)

allowed_attempts: int = 5
user_attempt: int = 0

#2. While: Condition with break statement
while user_attempt < allowed_attempts:
    print(f"Attempts Left: {allowed_attempts - user_attempt}")
    
    # 3. Get User Number
    user_input: int = int(input("Enter a Number: "))
    user_attempt +=1

    #4. If statements for comparison
    if user_input == random_number:
        print("Congrats! The number was: ", random_number)
        break

    if user_input < random_number:
        print("Too Low")
    elif user_input > random_number:
        print("Too High")
    else:
        print("Invalid Input")

if(user_attempt == allowed_attempts):
    print("Game Over")

    # Make Hints Better