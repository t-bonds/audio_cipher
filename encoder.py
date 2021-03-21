#!usr/bin/env python3

import configparser
import os
import time

import controller
import message
import numpy as np
import sounddevice as sd


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
    ciphertext = ''
    if int(settings['shift']) == 1:
        print("-----SHIFTING-----\n")
        ciphertext = shift(settings, msg, ciphertext)

    encode(settings, msg, ciphertext)


def shift(settings, msg, ciphertext):
    for char in msg:
        if char.isupper():
            ciphertext += chr((ord(char) +
                               (int(settings['key']) - 65)) % 26 + 65)
        else:
            ciphertext += chr((ord(char) +
                               (int(settings['key']) - 97)) % 26 + 97)
    print('Plaintext: ' + msg)
    print('Ciphertext: ' + ciphertext)
    print("\n-----SHIFTING COMPLETE-----\n")
    return ciphertext


def encode(settings, msg, ciphertext):
    print("\n-----ENCODING TO AUDIO FORMAT-----\n")
    key = []
    tone = []
    low = [697, 770, 852, 941]
    high = [1209, 1336, 1477, 1633]
    tones = {"1": [0, 0],
             "2": [0, 1],
             "3": [0, 2],
             "A": [0, 3],
             "4": [1, 0],
             "5": [1, 1],
             "6": [1, 2],
             "B": [1, 3],
             "7": [2, 0],
             "8": [2, 1],
             "9": [2, 2],
             "C": [2, 3],
             "*": [3, 0],
             "0": [3, 1],
             "#": [3, 2],
             "D": [3, 3]}

    # Be Advised: This is a modified alphabet accounting for the ability to send numbers as a string.

    alphabet = {"1": [tones["1"], 1],
                "2": [tones["2"], 1],
                "A": [tones["2"], 2],
                "B": [tones["2"], 3],
                "C": [tones["2"], 4],
                "3": [tones["3"], 1],
                "D": [tones["3"], 2],
                "E": [tones["3"], 3],
                "F": [tones["3"], 4],
                "4": [tones["4"], 1],
                "G": [tones["4"], 2],
                "H": [tones["4"], 3],
                "I": [tones["4"], 4],
                "5": [tones["5"], 1],
                "J": [tones["5"], 2],
                "K": [tones["5"], 3],
                "L": [tones["5"], 4],
                "6": [tones["6"], 1],
                "M": [tones["6"], 2],
                "N": [tones["6"], 3],
                "O": [tones["6"], 4],
                "7": [tones["7"], 1],
                "P": [tones["7"], 2],
                "Q": [tones["7"], 3],
                "R": [tones["7"], 4],
                "S": [tones["7"], 5],
                "8": [tones["8"], 1],
                "T": [tones["8"], 2],
                "U": [tones["8"], 3],
                "V": [tones["8"], 4],
                "9": [tones["9"], 1],
                "W": [tones["9"], 2],
                "X": [tones["9"], 3],
                "Y": [tones["9"], 4],
                "Z": [tones["9"], 5],
                "*": [tones["*"], 1],
                "#": [tones["#"], 1],
                " ": [tones["#"], 2]}

    valid = ["0", "1", "2", "3", "4", "5", "6",
             "7", "8", "9", "*", "#", "A", "B", "C", "D"]
    if ciphertext == '':
        ciphertext = msg

    for char in ciphertext:
        key = alphabet[char.upper()]
        tone = key[0]
        freq_1 = low[tone[0]]
        freq_2 = high[tone[1]]
        sin_1 = np.sin(2 * np.pi * np.arange(int(settings['sample_rate']) * float(
            settings['duration'])) * freq_1 / int(settings['sample_rate']))
        sin_2 = np.sin(2 * np.pi * np.arange(int(settings['sample_rate']) * float(
            settings['duration'])) * freq_2 / int(settings['sample_rate']))
        sd.play(sin_1 + sin_2)
        time.sleep(float(settings['pause']))
        # TODO Change to write to .wav. format, then play .wav file.


if __name__ == '__main__':
    main()
