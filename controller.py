#!usr/bin/env python3

import sys

import encoder
import message
import settings
import audio_file


def main_menu():
    print("\n-----AUDITORY SHIFT CIPHER MAIN MENU-----")
    print("\n\tOptions:")
    print("\t1. Create Message")
    print("\t2. Encoder Settings")
    print("\t3. Generate Tones")
    print("\t4. Create Audio File")
    print("\t5. Decoder Settings")
    print("\t6. Decode Message")
    print("\t7. Exit")
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
        audio_file.main()
    elif menu_choice == 5:
        code = 1
        settings.settings_menu(code)
    elif menu_choice == 6:
        return
    elif menu_choice == 7:
        print("Goodbye...")
        sys.exit(0)
    else:
        print("\nInvalid Option...")
        main_menu()


def main():
    main_menu()


if __name__ == '__main__':
    main()
