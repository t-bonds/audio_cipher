#!usr/bin/env python3

import configparser
import math
import os
import struct
import time
import wave

import controller
import message
import numpy as np
from pydub import AudioSegment
from pydub.playback import play


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
    print("-----CURRENT ENCODER SETTINGS-----\n")
    for i in settings:
        print(i + " = " + settings[i])


def init_keys():

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
    return low, high, tones, alphabet_key


def main():
    print("\n-----STARTING ENCODER-----")
    settings, msg = init()
    low, high, tones, alphabet_key = init_keys()
    print_settings(settings)
    print("\n-----SETTINGS LOADED-----")
    if settings['broadcast'] == 'false' and settings['file'] == 'false':
        print("ERROR: 'broadcast' and 'file' variables are both false. This program will not generate any output.")
        controller.main_menu()
    ciphertext = ''
    if settings['shift'] == 'true':
        print("-----SHIFTING-----\n")
        ciphertext = shift(settings, msg, ciphertext, alphabet_key)
    else:
        print('Plaintext: ' + msg)
    encode(settings, msg, ciphertext, low, high, tones, alphabet_key)


def shift(settings, msg, ciphertext, alphabet_key):

    alphabet = list(alphabet_key.keys())

    for char in msg:
        for index, character in enumerate(alphabet):
            if char == character:
                ciphertext += alphabet[index + int(settings['shift_key'])]
    print('Plaintext: ' + msg)
    print('Ciphertext: ' + ciphertext)
    print("\n-----SHIFTING COMPLETE-----")
    return ciphertext


def encode(settings, msg, ciphertext, low, high, tones, alphabet_key):
    print("-----ENCODING TO AUDIO FORMAT-----")

    audio = []
    if ciphertext == '':
        ciphertext = msg

    for i, char in enumerate(ciphertext):
        key = alphabet_key[char]
        tone_1 = key[0]
        tone_2 = key[1]
        freq_1 = low[tone_1[0]]
        freq_2 = high[tone_1[1]]
        freq_3 = low[tone_2[0]]
        freq_4 = high[tone_2[1]]
        append_sin_wave(settings, freq_1, freq_2, audio)
        if not float(settings['pause']) == 0.0:
            append_pause(settings, audio)
        append_sin_wave(settings, freq_3, freq_4, audio)
        if not float(settings['pause']) == 0.0:
            append_pause(settings, audio)

    file_path = save_file(settings, audio)
    if settings['broadcast'] == 'true':
        print("-----PLAYING AUDIO-----")
        audio_file = AudioSegment.from_wav(file_path)
        play(audio_file)
    if settings['file'] == 'false':
        os.remove(file_path)
        if len(os.listdir(os.getcwd() + '/generated_audio/')) == 0:
            os.rmdir(os.getcwd() + '/generated_audio/')
    print("-----EXECUTION COMPLETE-----")
    controller.main_menu()


def append_pause(settings, audio):
    num_samples = (float(settings['pause']) * 1000) * \
        (int(settings['sample_rate']) / 1000)

    for i in range(int(num_samples)):
        audio.append(0.0)
    return


def append_sin_wave(settings, freq_1, freq_2, audio):
    num_samples = (float(settings['duration']) *
                   1000) * (int(settings['sample_rate']) / 1000)

    for i in range(int(num_samples)):
        audio.append(float(settings['volume']) * np.sin(2 * math.pi * freq_1 * (i / float(settings['sample_rate']))) + float(
            settings['volume']) * np.sin(2 * math.pi * freq_2 * (i / float(settings['sample_rate']))))
    return


def save_file(settings, audio):
    time_str = time.strftime("%Y%m%d-%H%M%S")
    file_name = time_str + ".wav"
    if not os.path.isdir(os.getcwd() + '/generated_audio/'):
        os.mkdir(os.getcwd() + '/generated_audio/')
    file_path = os.getcwd() + '/generated_audio/' + file_name
    with wave.open(file_path, 'wb') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setnframes(len(audio))
        wav_file.setframerate(int(settings['sample_rate']))
        wav_file.setcomptype("NONE", "no compression")

        for sample in audio:
            wav_file.writeframes(struct.pack('h', int(sample * 32767.0)))
    print("-----ENCODING COMPLETE-----")
    return file_path


if __name__ == '__main__':
    main()
