import random

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
