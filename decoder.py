#!usr/bin/env python3

import configparser
import os
import sys
import controller
import audio_file
import numpy as np
from pydub import AudioSegment
from pydub.playback import play
from scipy.io import wavfile

verbose = True


def init():
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

    settings = {}
    parser = configparser.ConfigParser()
    parser.read("decoder_settings.ini")
    args = parser['SETTINGS']
    for i in args:
        settings[i] = args[i]

    return low, high, tones, alphabet_key, settings


def raw_decode(file_name, settings):
    dtmf = {(697, 1209): "1", (697, 1336): "2", (697, 1477): "3", (770, 1209): "4", (770, 1336): "5", (770, 1477): "6", (852, 1209): "7", (852, 1336): "8",
            (852, 1477): "9",  (941, 1336): "0"}

    fps, data = wavfile.read(file_name)
    precision = float(settings['precision'])
    duration = len(data) / fps
    step = int(len(data) // (duration // precision))
    print("-----RAW OUTPUT-----\n")
    print("0:00 ", end='', flush=True)
    c = ""
    raw = ""
    for i in range(0, len(data) - step, step):
        signal = data[i:i + step]
        frequencies = np.fft.fftfreq(signal.size, d=1 / fps)
        amplitudes = np.fft.fft(signal)

        # Low
        i_min = np.where(frequencies > 0)[0][0]
        i_max = np.where(frequencies > 1050)[0][0]
        freq = frequencies[i_min:i_max]
        amp = abs(amplitudes.real[i_min:i_max])
        lf = freq[np.where(amp == max(amp))[0][0]]
        delta = int(settings['error_margin'])
        best = 0

        for f in [697, 770, 852, 941]:
            if abs(lf - f) < delta:
                delta = abs(lf - f)
                best = f

        lf = best

        # High
        i_min = np.where(frequencies > 1100)[0][0]
        i_max = np.where(frequencies > 2000)[0][0]
        freq = frequencies[i_min:i_max]
        amp = abs(amplitudes.real[i_min:i_max])
        hf = freq[np.where(amp == max(amp))[0][0]]
        delta = int(settings['error_margin'])
        best = 0

        for f in [1209, 1336, 1477, 1633]:
            if abs(hf - f) < delta:
                delta = abs(hf - f)
                best = f
        hf = best

        t = int(i // step * precision)

        if t > int((i - 1) // step * precision):
            m = str(int(t // 60))
            s = str(t % 60)
            s = "0" * (2 - len(s)) + s
            print("\n" + m + ":" + s + " ", end='', flush=True)
        try:
            if lf == 0 or hf == 0:
                print(".", end='', flush=True)
                raw = raw + "."
                c = ""
            else:
                c = dtmf[(lf, hf)]
                print(c, end='', flush=True)
                raw = raw + str(c)
        except KeyError:
            raw = raw + "."
    return raw


def decode(raw, settings, alphabet_key, tones):
    if settings['manual'] == 'true':
        print("\n\n-----BEGINNING MANUAL INPUT-----\n ")
        decode_values = list(input(
            "Please Input Numerical Output Values(2-digit numbers, space seperated): ").split())
        value_list = []
        msg = ""
        for value in decode_values:
            for digit in value:
                for key, value in tones.items():
                    if digit == key:
                        value_list.append(value)
        for i, values in enumerate(value_list):
            check_list = []
            if i % 2 == 0:
                check_list = [value_list[i], value_list[i + 1]]
                for key, value in alphabet_key.items():
                    if value == check_list:
                        msg = msg + str(key)
        return msg
    else:
        print("\n-----ERROR: AUTOMATIC DECODING CURRENTLY UNAVALIABLE. ISSUES WITH INTEFERENCE IN DECODING-----")
        controller.main_menu()
        # TODO: DETERMINE SOLUTION FOR AUTOMATIC DECODING
        return msg


def shift(settings, msg, alphabet_key):

    alphabet = list(alphabet_key.keys())
    plaintext = ''
    for char in msg:
        for index, character in enumerate(alphabet):
            if char == character:
                plaintext += alphabet[index - int(settings['shift_key'])]
    print('Ciphertext: ' + msg)
    print('Plaintext: ' + plaintext)
    print("\n-----SHIFTING COMPLETE-----")
    return plaintext


def main():

    low, high, tones, alphabet_key, settings = init()

    print("\n-----STARTING DECODER-----")
    print("-----CURRENT DECODER SETTINGS-----\n")
    for i in settings:
        print(i + " = " + settings[i])
    print("\n-----SETTINGS LOADED-----")
    cwd = os.getcwd() + '/decode_audio/'
    if len(os.listdir(cwd)) > 1:
        print("ERROR: MORE THAN ONE AUDIO FILE FOUND. \nEXITING...")
        sys.exit(1)
    if len(os.listdir(cwd)) == 0:
        print("\nAudio File Not Found...")
        print("Redirecting to File Creator")
        audio_file.file_not_found_menu(cwd)
    for f in os.listdir(cwd):
        file_name = (os.path.join(cwd, f))
        local_file = f
    if settings['broadcast'] == 'true':
        print("-----PLAYING AUDIO-----")
        audio = AudioSegment.from_wav(file_name)
        play(audio)

    raw = raw_decode(file_name, settings)
    msg = decode(raw, settings, alphabet_key, tones)

    if settings['shift'] == 'true':
        print("\n-----SHIFTING-----\n")
        plaintext = shift(settings, msg, alphabet_key)
    else:
        print("\n-----FINAL OUTPUT-----")
        print('Plaintext: ' + plaintext)
    if settings['file'] == 'true':
        with open(os.getcwd() + "/" + local_file + "_report.txt", 'w') as f:
            f.write("----- DECODING REPORT OF \'" + local_file +
                    "\' -----\n\n-----RAW_OUTPUT-----")
            f.write("\n\n" + raw)
            if settings['shift'] == 'true':
                f.write("\n\n-----FINAL_OUTPUT-----")
                f.write("\nCiphertext_Output: " + msg)
            f.write('\nPlaintext_Output: ' + plaintext)
        print("-----OUTPUT FILE CREATED-----")
    print("\n-----EXECUTION COMPLETE-----")
    controller.main_menu()


if __name__ == '__main__':
    main()
