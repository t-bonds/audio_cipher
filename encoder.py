#!usr/bin/env python3

import configparser
import os

import controller
import message


def init():
    settings = {}
    parser = init_parse()
    args = parser['SETTINGS']

    for i in args:
        settings[i] = args[i]

    msg = msg_parse()

    return settings, msg


def init_parse():
    parser = configparser.ConfigParser()
    parser.read("encoder_settings.ini")
    return parser


def msg_parse():
    cwd = os.getcwd()

    if not os.path.isfile(cwd + '/message.txt'):
        print("\nMessage File Not Found...")
        print("Redirecting to Message Creator")
        message.file_not_found_menu(cwd)
    with open('message.txt', 'r') as f:
        msg = f.read()
        return msg


def print_settings(settings):
    print("\n-----CURRENT ENCODER SETTINGS-----\n")
    for i in settings:
        print(i + " = " + settings[i])


def main():
    print("\n-----ENCODING-----\n")
    settings, msg = init()
    print_settings(settings)
    print("\n-----SETTINGS LOADED-----\n")

    if int(settings['shift']) == 1:
        print("-----SHIFTING-----\n")
        shift(settings, msg)


def shift(settings, msg):
    ciphertext = ''
    for char in msg:
        if char.isupper():
            ciphertext += chr((ord(char) +
                               (int(settings['key']) - 65)) % 26 + 65)
        else:
            ciphertext += chr((ord(char) +
                               (int(settings['key']) - 97)) % 26 + 97)
    print(ciphertext)
    print(print("\n-----SHIFTING COMPLETE-----\n"))


def encode():
    pass


if __name__ == '__main__':
    main()
