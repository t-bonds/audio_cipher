#!usr/bin/env python3

import sys

import encoder
import message
import settings


def main_menu():
    print("\n-----AUDITORY SHIFT CIPHER MAIN MENU-----")
    print("\n\tOptions:")
    print("\t1. Create Message")
    print("\t2. Encoder Settings")
    print("\t3. Generate Tones")
    print("\t4. Decoder Settings")
    print("\t5. Decode Message")
    print("\t6. Exit")
    try:
        menu_choice = int(input("Please Select an Option: "))
    except ValueError:
        print("\tError: Value Must Be A Number.\n")
        main_menu()
    if menu_choice == 1:
        message.main()
    elif menu_choice == 2:
        code = 0
        settings.settings_menu(code)
    elif menu_choice == 3:
        encoder.main()
    elif menu_choice == 4:
        code = 1
        settings.settings_menu(code)
    elif menu_choice == 5:
        return
    elif menu_choice == 6:
        print("Goodbye...")
        sys.exit(0)
    else:
        print("\nInvalid Option...")
        main_menu()


def main():
    main_menu()


if __name__ == '__main__':
    main()
