# Encoder/Decoder Lab_6 Michael Amiot
numbers = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9",
           "0","1", "2", "3", "4", "5", "6", "7", "8", "9"]  # doubled list to remain in range
def encode(password):
    encoded_pass = ""
    shift_amount = 3  # sets shift amount
    for num in password:
        if num in numbers:
            position = numbers.index(num)  # start position in numbers list for first number in password
            new_position = position + shift_amount  # adjusts each password number by increase of 3
            encoded_pass += numbers[new_position]  # stores shifted numbers in list
    return encoded_pass  # returns encoded password


def decode(passcode):  # decoder function - Karina Ann
    password_list = list(passcode)
    for index, item in enumerate(password_list):  # iterate through each item in list and subtract 3
        password_list[index] = int(item) - 3
    final = ''  # turn password_list back into a string using final
    for index, item in enumerate(password_list):  # iterate though each item in list and turn into string
        final = final + str(password_list[index])
    return final


while True:
    print('\nMenu')
    print('-------------')
    print("\n1. Encode\n2. Decode\n3. Quit ")
    opt = input("\nPlease enter an option: ")

    if opt == "1":

        password = input('Please Enter your password to encode: ')
        print(f'Your password has been encoded and stored!')
        x = encode(password)
        print('Menu')
        print('-------------')
        print("\n1. Encode\n2. Decode\n3. Quit ")
        opt = input("\nPlease enter an option: ")

    if opt == "2":  # decode option added
        print("The encoded password is " + x + ", and the original password is " + decode(x))
        print('Menu')
        print('-------------')
        print("\n1. Encode\n2. Decode\n3. Quit ")
        opt = input("\nPlease enter an option: ")

    if opt == "3":
        print('Goodbye!')
        quit()
