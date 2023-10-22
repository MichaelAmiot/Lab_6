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

while True:
    print('\nMenu')
    print('-------------')
    print("\n1. Encode\n2. Decode\n3. Quit ")
    opt = input("\nPlease enter an option: ")

    if opt == "1":
        # staying under option 1 will keep return value from encode function in local scope for decode function
        password = input('Please Enter your password to encode: ')
        print(f'Your password has been encoded and stored!')
        x = encode(password)
        print('Menu')
        print('-------------')
        print("\n1. Encode\n2. Decode\n3. Quit ")
        opt = input("\nPlease enter an option: ")





