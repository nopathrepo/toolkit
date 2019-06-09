"""
OBERON v2

  Oberon using Tkinter GUI package

  Authors:  Ryan LeBoeuf
            Matthew Rinaldi
"""
import os, sys          # os.listdir(), sys.argv, sys.exit()
import re
import datetime         # datetime.datetime.now()
from tkinter import *

def get_extension(filename):
    i = 1
    while i < len(filename):
        index = len(filename) - i
        if filename[index] == '.':
            return filename[index:]
        i += 1

""" User enters information to place into files matching the extensions
    array, and the function will prepend the header comments to the
    files. The functiion DOES NOT prepend to makefiles or binaries
        (e.g. a.out, makefile, Makefile).
"""
def add_header(path, name, user, lab, class_section):
    now = datetime.datetime.now()

    date = str(now.month) + "/" + str(now.day) + "/" +str(now.year)

    for filename in os.listdir(path):

        skip = True
        for extension in extensions:
            if extension == get_extension(filename.lower()):
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

            # limits the description to 40 characters per line
            description = re.sub("(.{40})", "\\1\n", description, 0, re.DOTALL)

            # writes the information to the file
            with open(path + filename, 'w') as modified:
                modified.write("/*********************\n\n" + lab +
                "\n" + filename + "\n" + date + "\n" + name + "\n" + user + "\n" +
                class_section + "\n\n" +
                "*********************/" + "\n\n" + data)

""" Check the character length of every string in a directory's files,
    and print text if the file has any line that contains more than the specified
    amount of characters.
"""
def check_char(path, max_size):

    # get the files in path
    file_list = os.listdir(path)

    """ instantiate array for for loop
        target_files will be the array iterated through to check for character count """
    target_files = []

    """ for each file in directory, check if file extension matches specified extensions
        if so, append that file name to target_files array """
    for file in file_list:
        for extension in extensions:
            if extension == get_extension(file):
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
        if ".h" != get_extension(filename) and ".hpp" != get_extension(filename):
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

def process_input():
    target = entry1.get()
    size = entry2.get()

    check_char(target, size)

    check_head_guards(target)

    if header_yn == 1:
        #add_header(target)
        master = Tk()
        master.title("Header Information")

        Label(master, text="Full Name:").pack()
        name_entry = Entry(master)
        name_entry.pack()

        Label(master, text="User Name:").pack()
        user_entry = Entry(master)
        user_entry.pack()

        Label(master, text="Program Title:").pack()
        title_entry = Entry(master)
        title_entry.pack()

        Label(master, text="Class/Section #").pack()
        sect_entry = Entry(master)
        sect_entry.pack()

        Button(master, text="Add Headers", command=master.quit).pack()

        master.mainloop()

        add_header(target, name_entry, user_entry, title_entry, sect_entry)

### --- STARTING POINT --- ###

extensions = [ ".cpp", ".h", ".c", ".hpp" ]

root = Tk()
root.title("Oberon Tkinter")

Label(root, text="Directory:").pack()
entry1 = Entry(root)
entry1.pack()

Label(root, text="Line Size:").pack()
entry2 = Entry(root)
entry2.pack()

header_yn = IntVar()
checkbut = Checkbutton(root, text="header comments?", variable=header_yn)
checkbut.pack()

exit_button = Button(root, text="Quit", command=root.destroy)
exit_button.pack()

start_button = Button(root, text="Process", command=process_input)#.grid(row=3, column=2)
start_button.pack()

root.mainloop()
