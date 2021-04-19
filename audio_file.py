import os
import sys
import controller
from pydub import AudioSegment
from pydub.playback import play


def file_not_found_menu(cwd):
    ret = 0
    print("\n-----FILE NOT FOUND MENU-----")

    print("\n\tOptions:")
    print("\t1. Add Audio File")
    print("\t2. Record Audio File")
    print("\t3. Help")
    print("\t4. Return To Main Menu")
    print("\t5. Exit")
    try:
        file_not_found_menu_choice = int(input("Please Select an Option: "))
    except ValueError:
        print("\tError: Value Must Be A Number.\n")
        file_not_found_menu(cwd)
    if file_not_found_menu_choice == 1:
        input("Halting... Please Add an Audio File to the Directory.\nPress \"Enter\" To Continue...")
        main()
    elif file_not_found_menu_choice == 2:
        record(cwd, ret)
        controller.main_menu()
    elif file_not_found_menu_choice == 3:
        print("\nAn audio file must exist in the \'decode_audio\'. This folder will contain the file to be decoded. \nFrom here, you may:\n\nAdd An Audio File: The program will wait. At this point, you may add your own audio file to the directory. \nWhen you have done this, the program will prompt you to continue, and will rescan the directory for the audio file. \n\n-----NOTE: THIS PROGRAM ONLY SUPPORTS .WAV FILES.-----\n\nRecord An Audio File: The program will begin recording through your system's microphone. \nPress \"Enter\" when complete. \nYour Audio File will be stored as a .wav file. \nIf you have created an audio file through the encoder, you must manually add it to the \'decode_audio\' folder from the \'generated_audio\' folder.\n")
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
    print("\t1. Overwrite Audio File")
    print("\t2. Delete Audio File")
    print("\t3. Play Audio File")
    print("\t4. Help")
    print("\t5. Return To Main Menu")
    print("\t6. Exit")
    try:
        file_found_menu_choice = int(input("Please Select an Option: "))
    except ValueError:
        print("\tError: Value Must Be A Number.\n")
        file_found_menu(cwd)
    if file_found_menu_choice == 1:
        if len(os.listdir(cwd)) > 0:
            record(cwd, ret)
        else:
            print(
                "Error: An Audio File has been removed from the directory. \n\tResetting...")
            main()
    elif file_found_menu_choice == 2:
        print(
            "\nAttention: This Option Will Delete Your Audio File.")
        print("\n\tDo You Wish To Continue?\n\t1. Yes \n\t2. No")
        try:
            delete_choice = int(input("Please Select an Option: "))
        except ValueError:
            print("\tError: Value Must Be A Number.\n")
            file_found_menu(cwd)
        if delete_choice == 1:
            for f in os.listdir(cwd):
                os.remove(os.path.join(cwd, f))
                print("Audio File Deleted...")
            main()
        elif delete_choice == 2:
            print("Returning...")
            main()
        else:
            print("Invalid Option: Must Be 1 or 2...")
            file_found_menu(cwd)
    elif file_found_menu_choice == 3:
        for f in os.listdir(cwd):
            file_path = os.path.join(cwd, f)
        print("\n-----PLAYING AUDIO FILE-----\n")

        audio_file = AudioSegment.from_wav(file_path)
        play(audio_file)

        print("\n-----END AUDIO FILE-----\n")
        file_found_menu(cwd)
    elif file_found_menu_choice == 4:
        print("\nAn audiofile must exist in the same directory as the program. This file contains the audio to be decoded. \nFrom here, you may:\n\nOverwrite An Audio File: Take an existing audio file and overwrite its contents with new audio. \n\nDelete An Audio File: Delete an existing audio file.\n\nPlay Audio File: Play the contents of an audio file.\n")
        file_found_menu(cwd)
    elif file_found_menu_choice == 5:
        controller.main_menu()
    elif file_found_menu_choice == 6:
        print("Goodbye...")
        sys.exit(0)
    else:
        print("\nInvalid Option...")
        file_found_menu(cwd)


# def message_creator(msg):
#     with open("message.txt", 'w') as f:
#         f.write(msg)
#     print("\nMessage File Created/Overwritten. \nReturning to Main Menu...")
#     main()
#
#
# def overwrite(cwd, ret):
#     print(
#         "\nAttention: A Message File Has Been Found. Continuing Will Overwrite This File.")
#     print("\n\tDo You Wish To Continue?\n\t1. Yes \n\t2. No")
#     try:
#         overwrite_choice = int(input("Please Select an Option: "))
#     except ValueError:
#         print("\tError: Value Must Be A Number.\n")
#         overwrite()
#     if overwrite_choice == 1:
#         msg = input(
#             "This Message will be converted to a text file. \nPlease Input A Message And Press \"Enter\" To Continue: ")
#         message_creator(msg)
#     elif overwrite_choice == 2:
#         if ret == 0:
#             file_not_found_menu(cwd)
#         elif ret == 1:
#             file_found_menu(cwd)
#         else:
#             controller.main_menu()
#     else:
#         print("Invalid Option: Must Be 1 or 2...")
#         overwrite(cwd, ret)
#
#
def main():
    cwd = os.getcwd() + '/decode_audio/'
    # TODO Check if decode_audio is empty
    if os.path.exists(cwd) and not os.path.isfile(cwd):
        if not os.listdir(cwd):
            print("\nAudio File Not Found...")
            file_not_found_menu(cwd)
        else:
            if len(os.listdir(cwd)) > 1:
                print(
                    "\nERROR: Multiple Audio Files Found In \'decode_audio\' Folder. \nFolder Must Only Contain One File To Decode.")
                controller.main_menu()
            else:
                print("\nAudio File Found...")
                file_found_menu(cwd)
    else:
        print("-----ERROR: DECODE_AUDIO FOLDER NOT FOUND-----")
        sys.exit(1)
