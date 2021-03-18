#!usr/bin/env python3

import sys
import configparser
import controller


def init_parse(code):
    parser = configparser.ConfigParser()
    if code == 0:
        parser.read("encoder_settings.ini")
    elif code == 1:
        parser.read("decoder_settings.ini")
    else:
        print("System Error: Invalid Coding Option")
        sys.exit(1)
    return parser


def init(code):
    settings = {}
    parser = init_parse(code)
    args = parser['SETTINGS']

    for i in args:
        settings[i] = args[i]

    return settings


def change_settings(settings, code):
    print("-----CHANGE SETTINGS MENU-----\n")
    print("\n\tOptions:")

    count = 0
    for i, e in enumerate(settings):
        count = i + 1
        print("\t" + str(count) + ". " + e)

    print("\n\t" + str(count + 1) + ". Return To Main Menu")
    try:
        change_settings_choice = int(input("Please Select an Option: "))
    except ValueError:
        print("\tError: Value Must Be A Number.\n")
        change_settings()

    if change_settings_choice in range(0, count + 1):
        for i, e in enumerate(settings):
            if i == change_settings_choice - 1:
                setting = e

        try:
            new_setting = float(
                input("Please Enter A New Value For \'" + setting + "\': "))
        except ValueError:
            print("\tError: Value Must Be A Number.\n")
            change_settings(settings, code)
        parser = init_parse(code)
        new_setting = str(new_setting)
        parser.set('SETTINGS', setting, new_setting)
        with open('config.ini', 'w') as f:
            parser.write(f)
        settings_menu()

    elif change_settings_choice == count + 1:
        settings_menu()
    else:
        print("\nInvalid Option...")
        change_settings(settings, code)


def print_settings(settings):
    print("\n-----CURRENT ENCODER SETTINGS-----\n")
    for i in settings:
        print(i + " = " + settings[i])


def settings_menu(code):
    settings = init(code)
    print_settings(settings)
    print("\n-----SETTINGS MENU-----")
    print("\n\tOptions:")
    print("\t1. Change Settings")
    print("\t2. Help")
    print("\t3. Return To Main Menu")
    print("\t4. Exit")
    try:
        settings_choice = int(input("Please Select an Option: "))
    except ValueError:
        print("\tError: Value Must Be A Number.\n")
        settings_menu()
    if settings_choice == 1:
        change_settings(settings, code)
    elif settings_choice == 2:
        print("\nTone, Key, & Cipher Settings for Encoding stored in 'encoder_settings.ini' file.\nSettings for Decoding stored in 'decode_settings.ini' file.\n")
        settings_menu()
    elif settings_choice == 3:
        controller.main_menu()
    elif settings_choice == 4:
        print("Goodbye...")
        sys.exit(0)
    else:
        print("\nInvalid Option...")
        main_menu()


if __name__ == '__main__':
    code = 99
    settings_menu(code)
