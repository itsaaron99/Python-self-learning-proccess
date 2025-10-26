# ------chapter 3: loops--------

# --- while loop ---

# A `for` loop is for iterating over a sequence.
# A `while` loop is for repeating as long as a condition is true.

# Example: Countdown
print("--- Countdown Example ---")
countdown = 5
while countdown > 0:
    print(f"T-minus {countdown}...")
    countdown -= 1 # This is the update step. Without it, this would be an infinite loop!
print("Blast off!\n")


# --- Practice 1: Guess the Number Game ---

secret_number = 7
guess = None # Initialize guess to a value that is not the secret number.

print("--- Guess the Number Game ---")
print("I'm thinking of a number between 1 and 10.")

# The loop will continue as long as the user's guess is not correct.
while guess != secret_number:
    user_input = input("What's your guess? ")

    # Use a try-except block to handle cases where the user doesn't enter a number.
    try:
        guess = int(user_input)
    except ValueError:
        print("That's not a valid number! Please try again.")
        continue # Skip the rest of this loop iteration and ask again.

    # Use a full if/elif/else structure to provide correct feedback.
    if guess < secret_number:
        print("Too low, try again!")
    elif guess > secret_number:
        print("Too high, try again!")

# This line will only run AFTER the loop has finished (i.e., when the user guesses correctly).
print(f"Congratulations! You guessed it. The secret number was {secret_number}.")

# --- Practice 2: Guess the Number (Limited Attempts) ---

secret_number = 7
max_attempts = 3
attempts_left = max_attempts
guess = None

print("\n--- Guess the Number Game (3 Tries) ---")

# The loop continues as long as BOTH conditions are true:
# 1. The guess is not correct.
# 2. The player still has attempts left.
while guess != secret_number and attempts_left > 0:
    print(f"You have {attempts_left} attempts left.")
    user_input = input("What's your guess? ")

    try:
        guess = int(user_input)
    except ValueError:
        print("That's not a valid number! Please try again.")
        continue

    # 1. Use a full if/elif structure to give correct hints.
    if guess < secret_number:
        print("Too low, try again!")
    elif guess > secret_number:
        print("Too high, try again!")

    # 2. Decrement the counter after each guess.
    attempts_left -= 1

# After the loop, check WHY it ended.
# 3. Use a single if/else block. If the final guess is correct, the player won.
#    Otherwise, they must have run out of attempts.
if guess == secret_number:
    print(f"You won! The secret number was indeed {secret_number}.")
else:
    print(f"You lost! The secret number was {secret_number}.")


# --- Practice 3: Building an Interactive Menu ---

print("\n--- To-Do List Application ---")

# 1. Start an infinite loop. The loop itself is the application's running state.
while True:
    # 2. Display the menu and get input *inside* the loop.
    #    This ensures the user sees the options every time they need to make a choice.
    print("\nMenu:")
    print("1: Add a to-do item")
    print("2: View to-do list")
    print("q: Quit")
    choice = input("Enter your choice: ")

    # 4. Check the user's choice.
    if choice == '1':
        print("--> Adding item...")
    elif choice == '2':
        print("--> Viewing list...")
    elif choice == 'q':
        print("Goodbye!")
        break # 5. This is the only way to exit the 'while True' loop.
    else:
        # 6. Handle invalid input and let the loop continue.
        print("--> Invalid choice, please try again.")


# --- Practice 4: Refactoring the Menu with Functions ---

def display_menu():
    menu = [
        "Menu:",
        "1: Add a to-do item",
        "2: View to-do list",
        "q: Quit",
    ]
    for item in menu:
        print(item)

def add_item(todo_list):
    new_item = str(input("please enter topics in todo list"))
    todo_list.append(new_item)
    print(f"added {new_item} into todo list...")

def view_list(todo_list):
    if not todo_list:
        print("the list is empty...")
    else:
        for index, item in enumerate(todo_list, start=1):
            print(f"{index}. {item}")


def main_todo_app():
    todo_items = [] # The list must be initialized here.

    print("\n--- To-Do List Application (Refactored) ---")

    while True:
        # TODO: Call display_menu()
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_item(todo_items)
        elif choice == "2":
            view_list(todo_items)
        elif choice == "q":
            print("Goodbye!")
            break
        else:
            print("invalid choice, exit...")
            
