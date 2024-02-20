import random
import tkinter as tk


main_window = tk.Tk()
main_window.title("Password Generator")

# Set window size
window_width = 600
window_height = 400

# Get screen widht and height
screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()

# Get the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# Set the window to the center
main_window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

LETTERS_LOWER = "abcdefghijklmnopqrstuvwxyz"
LETTERS_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "1234567890"
EXTRA_CHARACTERS = "!@#$%^&*()_+{}:;?"

password = ""

len_password = input("Please the desired password length: ")


def random_choice(sequence):
    return random.choice(sequence)


# Randomly chooses char set to add to password
while len(password) < int(len_password):

    sequence_choice = random.randint(1, 4)

    match sequence_choice:  # Adds random char from set to password
        case 1:
            password += random_choice(LETTERS_LOWER)
        case 2:
            password += random_choice(LETTERS_UPPER)
        case 3:
            password += random_choice(NUMBERS)
        case 4:
            password += random_choice(EXTRA_CHARACTERS)

print(f"Your generated password is: {password}")
