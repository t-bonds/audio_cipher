#!usr/bin/env python3

import sys
import configparser
import controller


def init_parse():
    parser = configparser.ConfigParser()
    parser.read("config.ini")
    return parser


def init():
    settings = {}
    parser = init_parse()
    args = parser['SETTINGS']

    for i in args:
        settings[i] = args[i]

    return settings


def main():

    settings = init()
    print_settings(settings)
    print("\n-----SETTINGS LOADED-----\n")


def change_settings(settings):
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
            change_settings(settings)
        parser = init_parse()
        new_setting = str(new_setting)
        parser.set('SETTINGS', setting, new_setting)
        with open('config.ini', 'w') as f:
            parser.write(f)
        settings_menu()

    elif change_settings_choice == count + 1:
        settings_menu()
    else:
        print("\nInvalid Option...")
        change_settings(settings)


def print_settings(settings):
    print("\n-----CURRENT ENCODER SETTINGS-----\n")
    for i in settings:
        print(i + " = " + settings[i])


def settings_menu():
    settings = init()
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
        change_settings(settings)
    elif settings_choice == 2:
        print("\nTone, Key, & Cipher Settings stored in 'config.ini' file.\n")
        settings_menu()
    elif settings_choice == 3:
        controller.main_menu()
    elif settings_choice == 4:
        print("Goodbye...")
        sys.exit(0)
    else:
        print("\nInvalid Option...")
        main_menu()


def shift():
    pass


def encode():
    pass


if __name__ == '__main__':
    main()
