import base64
import string
import time
import traceback
from os import system, name
from string import ascii_lowercase

LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)}
or2 = "Please respond with '1' or '2'\n"
enter = "Enter your massage: "


def encode_or_decode():
    while True:
        an = input("\nDo you want to decode(1) Or encode(2) (1/2/): ")
        if an == "1":
            if name == "nt":
                system('cls')
                time.sleep(0)
                decode()

            else:
                system('clear')
                time.sleep(0)
                decode()

        elif an == '2':
            if name == 'nt':
                system('cls')
                encode()

            else:
                system('clear')
                encode()

        else:
            print(or2)


def decode():
    while True:
        an = input("\nDo you want to cipher-decode(1) Or base64_decode(2) (1/2/): ")
        if an == "1":
            if name == "nt":
                system('cls')
                time.sleep(0)
                cipher_decode()

            else:
                system('clear')
                time.sleep(0)
                cipher_decode()

        elif an == '2':
            if name == 'nt':
                system('cls')
                time.sleep(0)
                base64_decode()

            else:
                system('clear')
                time.sleep(0)
                base64_decode()

        else:
            print(or2 + "3")


def cipher_decode():
    alphabet = string.ascii_lowercase
    encrypted_message = input("Enter the message you would like to decrypt: ").strip()
    key = int(input("Enter key to decrypt: "))

    decrypted_message = ""

    for c in encrypted_message:

        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position - key) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c

    print(decrypted_message)
    clear()


def base64_decode():
    base64_decode_message = input("base64 decode: ")
    base64_bytes = base64_decode_message.encode("ascii")
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    print('decoding')
    print(message)
    clear()


def encode():
    while True:
        an = input("\n[Do you want to cipher-encode(1)], [base64-encode(2)] or "
                   "[Cipher-encode And base64-encode(3)] (1/2/3): ")
        if an == "1":
            if name == "nt":
                system('cls')
                time.sleep(0)
                cipher_encode()

            else:
                system('clear')
                time.sleep(0)
                cipher_encode()

        elif an == '2':
            if name == 'nt':
                system('cls')
                time.sleep(0)
                base64_encode()

            else:
                system('clear')
                time.sleep(0)
                base64_encode()

        elif an == '3':
            if name == 'nt':
                system('cls')
                time.sleep(0)
                b64_cipher_encode()
            else:
                system('clear')
                time.sleep(0)
                b64_cipher_encode()
        else:
            print(or2)


def base64_encode():
    message = input(enter)
    message_bytes = message.encode("ascii")
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    print("base64 =", base64_message)
    clear()


def alphabet_position(text):
    text = text.lower()
    numbers = [LETTERS[character] for character in text if character in LETTERS]
    return numbers


def caesar_me(string, shift):
    shift_key = shift
    numbers_list = alphabet_position(string)
    caesar_numbers = []

    for number in numbers_list:
        new_num = 0
        if int(number) + shift_key > 26:
            new_num = (int(number) + shift_key) - 26
        else:
            new_num = int(number) + shift_key
        caesar_numbers.append(new_num)
    return caesar_numbers


def number_position(string, shift):
    num_list = caesar_me(string, shift)
    new_word = []
    for num in num_list:
        string_num = str(num)
        for key, value in LETTERS.items():
            if string_num == value:
                new_word.append(key)
    caesar_word = ''.join(new_word)
    return caesar_word


def caesar_string(wordlist, shift):
    new_string = []
    for word in wordlist:
        new_string.append(number_position(word, shift))
    final_string = ""
    for i in new_string:
        final_string = final_string + i + " "

    return final_string


def cipher_encode():
    user_input = input(enter)
    user_string = user_input.split()
    chosen_shift = int(input("Enter a Positive Integer for the Cipher: "))
    message = caesar_string(user_string, chosen_shift)
    print("Cipher =", message)
    clear()


def b64_cipher_encode():
    user_input = input(enter)
    user_string = user_input.split()
    chosen_shift = int(input("Enter a Positive Integer for the Cipher: "))
    message = caesar_string(user_string, chosen_shift)
    message_bytes = message.encode("ascii")
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    print("base64 =", base64_message)
    clear()


def close():
    time.sleep(0)
    print('\nBye')
    time.sleep(1)
    exit()


def clear():
    while True:
        ans = input("\nDo you want to start again? (y/n) ")
        if ans.lower() == "y":
            if name == "nt":
                system('cls')
                time.sleep(0)
                encode_or_decode()

            else:
                system('clear')
                time.sleep(0)
                encode_or_decode()

        elif ans.lower() == 'n':
            if name == 'nt':
                system('cls')
                close()

            else:
                system('clear')
                close()
        else:
            print("Please respond with 'Yes' or 'No'\n")


if __name__ == '__main__':
    # noinspection PyBroadException
    try:
        encode_or_decode()
    except KeyboardInterrupt:
        print('\nInterrupted')
        while True:
            clear()
    except Exception:
        with open("log.txt", "w") as log:
            traceback.print_exc(file=log)
            print('\nError is printed to log.txt')
            close()
