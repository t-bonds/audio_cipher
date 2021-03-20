#!usr/bin/env python3

import configparser
import sys

import controller


def init_parse(code):
    parser = configparser.ConfigParser()
    if code == 0:
        parser.read("encoder_settings.ini")
    elif code == 1:
        parser.read("decoder_settings.ini")
    else:
        print("System Error: Invalid Coding Option. Please Repair Script.")
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
        change_settings(settings, code)

    if change_settings_choice in range(0, count + 1):
        for i, e in enumerate(settings):
            if i == change_settings_choice - 1:
                setting = e

        new_setting = input(
            "Please Enter A New Value For \'" + setting + "\': ")

        parser = init_parse(code)
        new_setting = str(new_setting)
        parser.set('SETTINGS', setting, new_setting)
        if code == 0:
            with open('encoder_settings.ini', 'w') as f:
                parser.write(f)
        elif code == 1:
            with open('decoder_settings.ini', 'w') as f:
                parser.write(f)
        else:
            print("System Error: Invalid Coding Option. Please Repair Script.")
            sys.exit(1)
        settings_menu(code)

    elif change_settings_choice == count + 1:
        settings_menu(code)
    else:
        print("\nInvalid Option...")
        change_settings(settings, code)


def print_settings(settings, code):
    if code == 0:
        print("\n-----CURRENT ENCODER SETTINGS-----\n")
    elif code == 1:
        print("\n-----CURRENT DECODER SETTINGS-----\n")
    else:
        print("System Error: Invalid Coding Option. Please Repair Script.")
        sys.exit(1)
    for i in settings:
        print(i + " = " + settings[i])


def settings_menu(code):
    settings = init(code)
    print_settings(settings, code)
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
        settings_menu(code)
    if settings_choice == 1:
        change_settings(settings, code)
    elif settings_choice == 2:
        print("\nTone, Key, & Cipher Settings for Encoding stored in 'encoder_settings.ini' file.\nSettings for Decoding stored in 'decode_settings.ini' file.\n")
        settings_menu(code)
    elif settings_choice == 3:
        controller.main_menu()
    elif settings_choice == 4:
        print("Goodbye...")
        sys.exit(0)
    else:
        print("\nInvalid Option...")
        settings_menu(code)
