def encode_password(password):
    encoded_password = ""
    for digit in password:
        shifted_digit = str((int(digit) + 3) % 10)  # shift each digit up by 3 numbers
        encoded_password += shifted_digit
    return encoded_password


def decode_password(number):
    new_num = ''

    for digit in str(number):
        if int(digit) >= 3:
            digit = int(digit) - 3
            new_num += str(digit)
        else:
            digit = int(digit) + 7
            new_num += str(digit)

    return int(new_num)


def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        choice = input("Please enter an option: ")

        if choice == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode_password(password)
            print("Your password has been encoded and stored!")
        elif choice == "2":
            if not encoded_password:
                print("Please encode a password first.")
            else:
                decoded_password = decode_password(encoded_password)
                print(
                    f"The encoded password is {encoded_password}, and the original password is {decoded_password}")
        elif choice == "3":
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == '__main__':
    main()
