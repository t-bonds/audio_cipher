#!usr/bin/env python3

import sys
import configparser
import controller


def init():
    settings = {}
    parser = init_parse()
    args = parser['SETTINGS']

    for i in args:
        settings[i] = args[i]

    return settings


def init_parse():
    parser = configparser.ConfigParser()
    parser.read("encoder_settings.ini")
    return parser


def print_settings(settings):
    print("\n-----CURRENT ENCODER SETTINGS-----\n")
    for i in settings:
        print(i + " = " + settings[i])


def main():

    settings = init()
    print_settings(settings)
    print("\n-----SETTINGS LOADED-----\n")


def shift():
    pass


def encode():
    pass


if __name__ == '__main__':
    main()
