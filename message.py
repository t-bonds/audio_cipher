#!usr/bin/env python3
import os
import sys
import controller


def file_not_found_menu(cwd):
    ret = 0
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
        file_not_found_menu(cwd)
    if file_not_found_menu_choice == 1:
        input("Halting... Please Add a Message File to the Directory.\nPress \"Enter\" To Continue...")
        main()
    elif file_not_found_menu_choice == 2:
        if os.path.isfile(cwd + '/message.txt'):
            overwrite(cwd, ret)
        else:
            msg = input(
                "Please Input a Message... This Message will be converted to a text file. \nPress \"Enter\" To Continue")
            message_creator(msg)

        controller.main_menu()
    elif file_not_found_menu_choice == 3:
        print("\nA message file must exist in the same directory as the program. This file contains the message to be encoded. \nFrom here, you may:\n\nAdd A Message File: The program will wait. At this point, you may add your own message file to the directory. \nWhen you have done this, the program will prompt you to continue, and will rescan the directory for the message file. \n-----MESSAGE FILE MUST BE NAMED \"message.txt\"-----\n\nCreate A Message File: The program will create a message file for you, using input given from the command line.\nPress \"Enter\" when complete. If you message contains characters that cannot be read on a command line, \nor \"Enter\" must be pressed for any reason other than continuing, it is recommended that you add a message file created through another editor.\n")
        file_not_found_menu(cwd)
    elif file_not_found_menu_choice == 4:
        controller.main_menu()
    elif file_not_found_menu_choice == 5:
        print("Goodbye...")
        sys.exit(0)
    else:
        print("\nInvalid Option...")
        file_not_found_menu(cwd)


def file_found_menu(cwd):
    ret = 1
    print("\n-----FILE FOUND MENU-----")

    print("\n\tOptions:")
    print("\t1. Overwrite Message File")
    print("\t2. Delete Message File")
    print("\t3. Help")
    print("\t4. Return To Main Menu")
    print("\t5. Exit")
    try:
        file_found_menu_choice = int(input("Please Select an Option: "))
    except ValueError:
        print("\tError: Value Must Be A Number.\n")
        file_found_menu(cwd)
    if file_found_menu_choice == 1:
        if os.path.isfile(cwd + '/message.txt'):
            overwrite(cwd, ret)
        else:
            print(
                "Error: A Message File has been removed from the directory. \n\tReseting...")
            main()
    elif file_found_menu_choice == 2:
        print(
            "\nAttention: This Option Will Delete Message Files")
        print("\n\tDo You Wish To Continue?\n\t1. Yes \n\t2. No")
        try:
            delete_choice = int(input("Please Select an Option: "))
        except ValueError:
            print("\tError: Value Must Be A Number.\n")
            file_found_menu(cwd)
        if delete_choice == 1:
            if os.path.exists("message.txt"):
                os.remove("message.txt")
            else:
                print("Message File Not Found\n\tExiting...")
                main()
        elif delete_choice == 2:
            print("Returning...")
            main()
        else:
            print("Invalid Option: Must Be 1 or 2...")
            file_found_menu(cwd)
    elif file_found_menu_choice == 3:
        print("\nA message file must exist in the same directory as the program. This file contains the message to be encoded. \nFrom here, you may:\n\nOverwrite A Message File: Take an existing message file and overwrite its contents with a new message. \n\nDelete A Message File: Delete a existing message file.\n")
        file_found_menu(cwd)
    elif file_found_menu_choice == 4:
        controller.main_menu()
    elif file_found_menu_choice == 5:
        print("Goodbye...")
        sys.exit(0)
    else:
        print("\nInvalid Option...")
        file_found_menu(cwd)


def message_creator(msg):
    # TODO Create Function
    return


def overwrite(cwd, ret):
    print(
        "\nAttention: A Message File Has Been Found. Continuing Will Overwrite This File.")
    print("\n\tDo You Wish To Continue?\n\t1. Yes \n\t2. No")
    try:
        overwrite_choice = int(input("Please Select an Option: "))
    except ValueError:
        print("\tError: Value Must Be A Number.\n")
        overwrite()
    if overwrite_choice == 1:
        msg = input(
            "This Message will be converted to a text file. \nPlease Input A Message And Press \"Enter\" To Continue: ")
        message_creator(msg)
    elif overwrite_choice == 2:
        if ret == 0:
            file_not_found_menu(cwd)
        elif ret == 1:
            file_found_menu(cwd)
        else:
            controller.main_menu()
    else:
        print("Invalid Option: Must Be 1 or 2...")
        overwrite(cwd, ret)


def main():
    cwd = os.getcwd()

    if not os.path.isfile(cwd + '/message.txt'):
        print("\nMessage File Not Found...")
        file_not_found_menu(cwd)
    else:
        print("\nMessage File Found...")
        file_found_menu(cwd)
