import random

letters_lower = "abcdefghijklmnopqrstuvwxyz"
letters_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "1234567890"
chars = "!@#$%^&*()_+{}:;?"
password = ""

len_password = input("Please the desired password length: ")


def random_choice(sequence):
    return random.choice(sequence)


while len(password) < int(len_password):
    sequence_choice = random.randint(1, 4)
    match sequence_choice:
        case 1:
            password += random_choice(letters_lower)
        case 2:
            password += random_choice(letters_upper)
        case 3:
            password += random_choice(nums)
        case 4:
            password += random_choice(chars)

print(f"Your generated password is: {password}")
