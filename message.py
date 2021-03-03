#!usr/bin/env python3
import os
import sys
import controller


def file_not_found_menu():

    print("\n-----FILE NOT FOUND MENU-----")

    print("\n\tOptions:")
    print("\t1. Add Message File")
    print("\t2. Create Message File")
    print("\t3. Help")
    print("\t4. Return To Main Menu")
    print("\t5. Exit")
    try:
        file_not_found_menu_choice = int(input("Please Select an Option: "))
    except ValueError:
        print("\tError: Value Must Be A Number.\n")
        file_not_found_menu()
    if file_not_found_menu_choice == 1:
        return
    elif file_not_found_menu_choice == 2:
        return
    elif file_not_found_menu_choice == 3:
        print("\nA message file must exist in the same directory as the program. This file contains the message to be encoded. \nFrom here, you may:\n\nAdd A Message File: The program will wait. At this point, you may add your own message file to the directory. \nWhen you have done this, the program will prompt you to continue, and will rescan the directory for the message file. \n-----MESSAGE FILE MUST BE NAMED \"message.txt\"-----\n\nCreate A Message File: The program will create a message file for you, using input given from the command line.\nPress \"Enter\" when complete. If you message contains characters that cannot be read on a command line, \nor \"Enter\" must be pressed for any reason other than continuing, it is recommended that you add a message file created through another editor.\n")
        file_not_found_menu()
    elif file_not_found_menu_choice == 4:
        controller.main_menu()
    elif file_not_found_menu_choice == 5:
        print("Goodbye...")
        sys.exit(0)
    else:
        print("\nInvalid Option...")
        file_not_found_menu()


def message_creator():

    pass


def main():
    cwd = os.getcwd()

    if not os.path.isfile(cwd + '/message.txt'):
        print("\nMessage File Not Found...")
        file_not_found_menu()
