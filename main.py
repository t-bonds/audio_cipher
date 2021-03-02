#!usr/bin/env python3

import sys
from argparse import ArgumentParser


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

    def menu():
        pass


def main():
    if len(sys.argv < 1)
    args = parse()
    else:
        print("Command Line Arguments Not Detected...\n\tEntering User Interface.")
        menu()


if __name__ == '__main__':
    main()
