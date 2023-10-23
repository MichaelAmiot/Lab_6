# Encoder/Decoder Lab_6 Michael Amiot
def encode(password):
    encoded = ''
    password_list = list(password)
    # iterate through each item in password_list and add 3
    for index, item in enumerate(password_list):
        password_list[index] = int(item) + 3
        encoded += str(password_list[index])
    return encoded


def decode(passcode):  # decoder function - Karina Ann
    password_list = list(passcode)
    for index, item in enumerate(password_list):  # iterate through each item in list and subtract 3
        password_list[index] = int(item) - 3
    final = ''  # turn password_list back into a string using final
    for index, item in enumerate(password_list):  # iterate though each item in list and turn into string
        final = final + str(password_list[index])
    return final


if __name__ == '__main__':

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
