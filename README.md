# toolkit
Linux command-line toolkit for Computer Science students.

## oberon.py ##
This program will check each line in each file (C/C++ source and header files) in a specified directory to see if the lines exceed
a specified amount of characters. This is especially useful if you are limited to a specific number
of characters per line (such as in a university classroom).

oberon.py also supports header guard checking (both ```#pragma once``` and ```#ifndef```) and allows the user to
customize the header comments with name, date, username, etc. for all files in a directory. If a header guard is not found in a file, then ```#pragma once``` will be prepended to the file contents.

Special thanks to Matthew Rinaldi for adding and improving existing functionality to Oberon.

### How to Use ###
Run oberon.py with
```python oberon.py```

Oberon is written in Python 3 but does work and has been tested with Python 2.

## oberon-tkinter.py
GUI version of oberon using tkinter libraries. oberon-tkinter has only been tested with tkinter for Python 3. The functionality is the same, however all user input is taken from a GUI rather than the command line. Tkinter is available on almost all Linux distributions and is in several distro repos.

### How to Use
```python oberon-tkinter.py```
Any errors or invalid input will not crash the application. You can simply fix the errors and then click Process again. 
