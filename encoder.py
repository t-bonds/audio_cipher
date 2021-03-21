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
    low = [697, 770, 852, 941]
    high = [1209, 1336, 1477, 1633]
    tones = {"1": [0, 0],
             "2": [0, 1],
             "3": [0, 2],
             "4": [1, 0],
             "5": [1, 1],
             "6": [1, 2],
             "7": [2, 0],
             "8": [2, 1],
             "9": [2, 2],
             "*": [3, 0],
             "0": [3, 1],
             "#": [3, 2]}

    # Be Advised: This is a modified alphabet accounting for the ability to send numbers as a string.
    # This is not Standard DTMF Encoding

    alphabet_key = {" ": [tones["0"], tones["0"]],
                    "!": [tones["0"], tones["1"]],
                    "\"": [tones["0"], tones["2"]],
                    "#": [tones["0"], tones["3"]],
                    "$": [tones["0"], tones["4"]],
                    "%": [tones["0"], tones["5"]],
                    "&": [tones["0"], tones["6"]],
                    "\'": [tones["0"], tones["7"]],
                    "(": [tones["0"], tones["8"]],
                    ")": [tones["0"], tones["9"]],
                    "*": [tones["1"], tones["0"]],
                    "+": [tones["1"], tones["1"]],
                    ",": [tones["1"], tones["2"]],
                    "-": [tones["1"], tones["3"]],
                    ".": [tones["1"], tones["4"]],
                    "/": [tones["1"], tones["5"]],
                    "0": [tones["1"], tones["6"]],
                    "1": [tones["1"], tones["7"]],
                    "2": [tones["1"], tones["8"]],
                    "3": [tones["1"], tones["9"]],
                    "4": [tones["2"], tones["0"]],
                    "5": [tones["2"], tones["1"]],
                    "6": [tones["2"], tones["2"]],
                    "7": [tones["2"], tones["3"]],
                    "8": [tones["2"], tones["4"]],
                    "9": [tones["2"], tones["5"]],
                    ":": [tones["2"], tones["6"]],
                    ";": [tones["2"], tones["7"]],
                    "<": [tones["2"], tones["8"]],
                    "=": [tones["2"], tones["9"]],
                    ">": [tones["3"], tones["0"]],
                    "?": [tones["3"], tones["1"]],
                    "@": [tones["3"], tones["2"]],
                    "A": [tones["3"], tones["3"]],
                    "B": [tones["3"], tones["4"]],
                    "C": [tones["3"], tones["5"]],
                    "D": [tones["3"], tones["6"]],
                    "E": [tones["3"], tones["7"]],
                    "F": [tones["3"], tones["8"]],
                    "G": [tones["3"], tones["9"]],
                    "H": [tones["4"], tones["0"]],
                    "I": [tones["4"], tones["1"]],
                    "J": [tones["4"], tones["2"]],
                    "K": [tones["4"], tones["3"]],
                    "L": [tones["4"], tones["4"]],
                    "M": [tones["4"], tones["5"]],
                    "N": [tones["4"], tones["6"]],
                    "O": [tones["4"], tones["7"]],
                    "P": [tones["4"], tones["8"]],
                    "Q": [tones["4"], tones["9"]],
                    "R": [tones["5"], tones["0"]],
                    "S": [tones["5"], tones["1"]],
                    "T": [tones["5"], tones["2"]],
                    "U": [tones["5"], tones["3"]],
                    "V": [tones["5"], tones["4"]],
                    "W": [tones["5"], tones["5"]],
                    "X": [tones["5"], tones["6"]],
                    "Y": [tones["5"], tones["7"]],
                    "Z": [tones["5"], tones["8"]],
                    "[": [tones["5"], tones["9"]],
                    "\\": [tones["6"], tones["0"]],
                    "]": [tones["6"], tones["1"]],
                    "^": [tones["6"], tones["2"]],
                    "_": [tones["6"], tones["3"]],
                    "`": [tones["6"], tones["4"]],
                    "a": [tones["6"], tones["5"]],
                    "b": [tones["6"], tones["6"]],
                    "c": [tones["6"], tones["7"]],
                    "d": [tones["6"], tones["8"]],
                    "e": [tones["6"], tones["9"]],
                    "f": [tones["7"], tones["0"]],
                    "g": [tones["7"], tones["1"]],
                    "h": [tones["7"], tones["2"]],
                    "i": [tones["7"], tones["3"]],
                    "j": [tones["7"], tones["4"]],
                    "k": [tones["7"], tones["5"]],
                    "l": [tones["7"], tones["6"]],
                    "m": [tones["7"], tones["7"]],
                    "n": [tones["7"], tones["8"]],
                    "o": [tones["7"], tones["9"]],
                    "p": [tones["8"], tones["0"]],
                    "q": [tones["8"], tones["1"]],
                    "r": [tones["8"], tones["2"]],
                    "s": [tones["8"], tones["3"]],
                    "t": [tones["8"], tones["4"]],
                    "u": [tones["8"], tones["5"]],
                    "v": [tones["8"], tones["6"]],
                    "w": [tones["8"], tones["7"]],
                    "x": [tones["8"], tones["8"]],
                    "y": [tones["8"], tones["9"]],
                    "z": [tones["9"], tones["0"]],
                    "{": [tones["9"], tones["1"]],
                    "|": [tones["9"], tones["2"]],
                    "}": [tones["9"], tones["3"]],
                    "~": [tones["9"], tones["4"]]}

    if ciphertext == '':
        ciphertext = msg

    for char in ciphertext:
        key = alphabet_key[char]
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
