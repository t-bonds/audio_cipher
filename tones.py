#!usr/bin/env python3

import numpy as np
import sounddevice as sd
import time
from argparse import ArgumentParser

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

valid = ["0", "1", "2", "3", "4", "5", "6",
         "7", "8", "9", "*", "#", "A", "B", "C", "D"]

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
            " ": [tones["*"], ]}


def parse():
    parser = ArgumentParser()
    parser.add_argument("-d", "--duration", type=float,
                        help="Length of Each Tone in Seconds", default=0.5)
    parser.add_argument("-v", "--volume", type=float,
                        help="Volume of Tone in Decimal value from 0 to 1", default=0.5)
    parser.add_argument("-s", "--sample", type=int,
                        help="Sampling Rate", default=44100)
    parser.add_argument("-p", "--pause", type=float,
                        help="Length of Pause Between Tones in Seconds", default=1.0)
    parser.add_argument("-m", "--message", action="store_true",
                        help="Send an Encoded String Using DTMF Alphabet")
    arguments = parser.parse_args()
    return arguments


def listen(args, low, high, tones, valid, alphabet):

    if args.message:
        str = list(input("Enter Message:").upper().replace(" ", "#*"))
        if all(d in alphabet for d in str):
            wave(args, low, high, tones, str, alphabet, args.message)
        else:
            print("Invalid Input...")
    else:
        while True:
            digits = list(input("Enter Digits: ").replace(" ", ""))
            if all(d in valid for d in digits):
                wave(args, low, high, tones, digits, alphabet, args.message)
        else:
            print("Invalid Input...")


def wave(args, low, high, tones, value, alphabet, message):

    key = []
    tone = []
    if args.message:
        for e in value:
            key = alphabet[e]
            tone = key[0]
            freq_1 = low[tone[0]]
            freq_2 = high[tone[1]]
            sin_1 = np.sin(2 * np.pi * np.arange(args.sample *
                                                 args.duration) * freq_1 / args.sample)
            sin_2 = np.sin(2 * np.pi * np.arange(args.sample *
                                                 args.duration) * freq_2 / args.sample)

            for i in range(0, key[1]):
                sd.play(sin_1 * args.volume + sin_2 * args.volume)
                time.sleep(args.pause)

    else:
        for e in value:
            freq_1 = low[tones[e][0]]
            freq_2 = high[tones[e][1]]
            sin_1 = np.sin(2 * np.pi * np.arange(args.sample *
                                                 args.duration) * freq_1 / args.sample)
            sin_2 = np.sin(2 * np.pi * np.arange(args.sample *
                                                 args.duration) * freq_2 / args.sample)

            sd.play(sin_1 * args.volume + sin_2 * args.volume)

            time.sleep(args.pause)


def main(low, high, tones, valid, alphabet):
    args = parse()
    listen(args, low, high, tones, valid, alphabet)


if __name__ == '__main__':
    main(low, high, tones, valid, alphabet)
