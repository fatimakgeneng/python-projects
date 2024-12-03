# Constants
PROMPT: str = "What do you want? "
JOKE: str = "Here is a joke for you! Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'."
SORRY: str = "Sorry, I only tell jokes."

# Define Function
def joke_bot():
    # 1. Get User Input
    user_input = input(PROMPT)

    # 2. If-else statements
    if user_input.lower() == "joke":
        print(JOKE)
    else:
        print(SORRY)

# Run the function
joke_bot()
