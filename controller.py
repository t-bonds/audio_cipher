#!usr/bin/env python3

import sys
from argparse import ArgumentParser
import message
import encoder


def parse():
    parser = ArgumentParser()
    # parser.add_argument("-d", "--duration", type=float,
    #                     help="Length of Each Tone in Seconds", default=0.5)
    # parser.add_argument("-v", "--volume", type=float,
    #                     help="Volume of Tone in Decimal value from 0 to 1", default=0.5)
    # parser.add_argument("-s", "--sample", type=int,
    #                     help="Sampling Rate", default=44100)
    # parser.add_argument("-p", "--pause", type=float,
    #                     help="Length of Pause Between Tones in Seconds", default=1.0)
    parser.add_argument("-o", "--option", type=int,
                        dest="menu_choice",  help="Set Menu Option", default=0)
    arguments = parser.parse_args()
    return arguments


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
        encoder.settings_menu()
    elif menu_choice == 3:
        return
    elif menu_choice == 4:
        return
    elif menu_choice == 5:
        return
    elif menu_choice == 6:
        print("Goodbye...")
        sys.exit(0)
    else:
        print("\nInvalid Option...")
        main_menu()


def main():
    if len(sys.argv) > 1:
        args = parse()
        menu_choice = args.menu_choice
        if menu_choice == 1:
            message.main()
        elif menu_choice == 2:
            encoder.settings()
        elif menu_choice == 3:
            return
        elif menu_choice == 4:
            return
        elif menu_choice == 5:
            return
        elif menu_choice == 6:
            print("Goodbye...")
            sys.exit(0)
        else:
            print("\nInvalid Option...")
            main_menu()
    else:
        print("Command Line Arguments Not Detected...\nEntering User Interface.")
        main_menu()


if __name__ == '__main__':
    main()
