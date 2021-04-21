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

    print("\n\t" + str(count + 1) + ". Return To Menu")
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


def help_menu(code):
    if code == 0:
        print("\n-----CURRENT ENCODER SETTINGS-----\n")
        print("duration: length of each tone in seconds. (float)")
        print("\nvolume: volume of tones on a scale from 0 to 1. (float)")
        print("\nsample rate: sample rate of tones. RECOMMEND NOT CHANGING. (int)")
        print("\npause: length of silence between each tone in seconds. (float)")
        print("\nshift: set to true to create shift cipher of message. (boolean)")
        print(
            "\nshift_key: if shift enabled, determines number of letters to shift by. (int)")
        print("\nbroadcast: if set to true, will play tones as they are created. (boolean)")
        print("\nfile: if set to true, will create a .wav audio file of the generated tones. (boolean)")
        print("\n\n -----NOTES-----\n\n")
        print("If both \'broadcast\' and \'file\' are both set to false, then this program will produce no visible output. At least one of these settings must be set to true.")
        print("\nIf \'duration\' and \'pause\' are both set to be very small, it will be difficult for audio decoding. For example, if duration = 0.1 and pause = 0.01, then the decoder output will be difficult to read. \'precision\' in the decoder may be decreased to increase the frequency in which tones are analyzed. However, decreasing this value below 0.025 can cause errors in decoder output.")
    if code == 1:
        print("\n-----CURRENT DECODER SETTINGS-----\n")
        print("shift: set to true to create reverse a shift cipher of message. (boolean)")
        print("\nshift_key: if shift enabled, determines number of letters to reverse shift by. (int)")
        print("\nbroadcast: if set to true, will play tones as they are created. (boolean)")
        print("\nfile: if set to true, will create a .wav audio file of the generated tones. (boolean)")
        print(
            "\nprecision: frequency of time in seconds the decoder analyzes tones. (float)")
        print(
            "\nerror margin: margin of error in Hz to match each tone to a frequency. (int)")
        print("\nmanual: allows user to read output and provide values manually. (boolean)")
        print("\n\n -----NOTES-----\n\n")
        print("\'shift\' and \'shift_key\' reverses a shift cipher, so the value for shift cipher must be given here as it is given in the encoder, and it will be subtracted automatically.")

        print("\'manual\' may be needed if there is high interference within tones, or if \'pause\' and \'duration\' are very small.")
        print("\'If decoder output is scrambled, \'duration\' and \'pause\' settings in the encoder may needed to be increased. Alternatively, \'precision\' may be decreased. However it is not recommend to set \'precision\' lower than 0.025, as any lower can cause errors in decoder output.")


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
        help_menu(code)
        settings_menu(code)
    elif settings_choice == 3:
        controller.main_menu()
    elif settings_choice == 4:
        print("Goodbye...")
        sys.exit(0)
    else:
        print("\nInvalid Option...")
        settings_menu(code)
