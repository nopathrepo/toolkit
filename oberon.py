"""
OBERON v2

  To run the program, type:
    python oberon.py
  into your terminal.

  Version 1.0:
  Simple program to check the character length of every string in a directory's files,
  and print text if the file has any line that contains more than the specified
  amount of characters.

  Version 1.1:
  Converted code to python3.

  Version 2:
  Added support for custom header comment insertion for each file in the directory.

  Authors:  Ryan LeBoeuf
            Matthew Rinaldi

"""
import os, sys          # os.listdir(), sys.argv, sys.exit()
import re
import datetime         # datetime.datetime.now()

""" prompt method to take user input and make sure a valid
    input was registered
    Precondition: is_dir is a boolean, msg is a string """
def prompt(msg, is_dir):
    ans = input(msg)

    if is_dir == True:
        print("This directory contains: ")
        for filename in os.listdir(ans):
            print(filename)

    answer = ""
    while (answer != "y" or answer != "n"):
        print(ans)
        answer = input("Is this correct (y/n)? ")
        if (answer == "y"):
            return ans
        else:
            return prompt(msg, is_dir)

""" User enters information to place into files matching the extensions
    array, and the function will prepend the header comments to the
    files. The functiion DOES NOT prepend to makefiles or binaries
        (e.g. a.out, makefile, Makefile).
"""
def add_header(path):
    now = datetime.datetime.now()

    date = str(now.month) + "/" + str(now.day) + "/" +str(now.year)
    name = input("Enter your name: ")
    user = input("Enter Clemson username: ")
    lab = input("Enter lab title: ")
    class_section = input("Enter class and section number: ")

    for filename in os.listdir(path):

        skip = True
        for extension in extensions:
            if extension in filename.lower():
                """ the file has the appropriate extension, therefore
                    do not skip prepending to the file and break from
                    the extensions loop """
                skip = False
                break

        """ if skip is true then the current file does not have
            one of the appropriate extensions """
        if skip == True:
            continue

        print(filename)
        with open(path + filename, 'r') as original:
            data = original.read()

            description = input("What does this file do? ")

            # limits the description to 40 characters per line
            description = re.sub("(.{40})", "\\1\n", description, 0, re.DOTALL)

            # writes the information to the file
            with open(path + filename, 'w') as modified:
                modified.write("/*********************\n\n" + lab +
                "\n" + filename + "\n" + date + "\n" + name + "\n" + user + "\n" +
                class_section + "\n\n" + description + "\n\n" +
                "*********************/" + "\n\n" + data)

""" Check the character length of every string in a directory's files,
    and print text if the file has any line that contains more than the specified
    amount of characters.
"""
def check_char(path):
    # prompt user for maximum character count per line
    max_size = input("Enter max char count: ")

    # get the files in path
    file_list = os.listdir(path)

    """ instantiate array for for loop
        target_files will be the array iterated through to check for character count """
    target_files = []

    """ for each file in directory, check if file extension matches specified extensions
        if so, append that file name to target_files array """
    for file in file_list:
        for extension in extensions:
            if extension in file:
                target_files.append(file)


    # iterate through target_files array
    for file in target_files:
        with open(path + file, "r") as current_file:
            current_file = current_file.read().splitlines()

            line_number = 0
            for line in current_file:
                line_number += 1

                """ if the length of the line in the file is longer than the
			        max allowed size, then print message to console """
                if len(line) > int(max_size):
                    print("\nFILE: " + file)
                    print("LINE #: " + str(line_number))
                    print("*** " + line + " ***")
                    print("<<< Contains more than " + max_size + "  characters >>>\n")

""" checks all .h files in specified path to see if they have header guards.
    if a .h file does not have a guard, then #pragma once will be prepended
    to the file. """
def check_head_guards(path):

    for filename in os.listdir(path):
        if ".h" not in filename:
            continue        # go to next file in directory

        file_has_guard = False

        with open(path + filename, 'r') as original:
            data = original.read()
            data_lines = data.splitlines()

            for line in data_lines:
                if line == "#pragma once" or "#ifndef" in line:
                    file_has_guard = True
                    break

            if file_has_guard == True:
                continue    # no need to write to the file
            else:
                with open(path + filename, 'w') as modified:
                    modified.write("#pragma once\n\n" + data);


### --- STARTING POINT --- ###

print("Welcome to OBERON!\n\n")

# specify extension parameters for the program
extensions = [ ".cpp", ".h", ".c" ]

""" if path is not specified in command line argument,
    prompt user for one """
if len(sys.argv) < 2:
    # example input
    print("Example path format: ")
    print("~/folder/")
    print("/home/USER/folder/\n")

    target_directory = prompt("Enter target directory: ", True)
else:
    # otherwise, read the path from command line
    target_directory = sys.argv[1]

# check the directory's files for lines containing more than 80 characters
#check_char(target_directory)

# check the header files for header guards
check_head_guards(target_directory)
print("Header guards have been checked.")
input("Press ENTER to continue...")

# implement header comments into files
header_yn = prompt("Would you like to implement header comments (y/n)? ", False).lower()
if header_yn == "y":
    add_header(target_directory)
else:
    input("Press ENTER to close...")
