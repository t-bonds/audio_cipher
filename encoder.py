#!usr/bin/env python3

import sys
import configparser


def init():
    settings = {}
    parser = configparser.ConfigParser()
    parser.read("config.ini")
    args = parser['SETTINGS']

    for i in args:
        settings[i] = args[i]

    return settings


def main():

    settings = init()
    print_settings()
    print("\n-----SETTINGS LOADED-----\n")


def change_settings():
    pass


def print_settings():
    print("-----CURRENT ENCODER SETTINGS-----\n")
    for i in settings:
        print(i + " = " + settings[i])


def settings_menu():
    pass


if __name__ == '__main__':
    main()
