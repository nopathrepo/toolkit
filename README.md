# toolkit
Linux command-line toolkit for Computer Science students.

## oberon.py ##
This program will check each line in each file (C/C++ source and header files) in a specified directory to see if the lines exceed
a specified amount of characters. This is especially useful if you are limited to a specific number
of characters per line (such as in a university classroom).

oberon.py also supports header guard checking (#pragma once and #ifndef) and allows the user to
customize the header guard with name, date, username, etc. for all files in a directory.

Special thanks to Matthew Rinaldi for adding and improving existing functionality to Oberon.

### How to Use ###
Run oberon.py with
```python oberon.py```

Oberon is written in Python 3 but does work and has been tested with Python 2.
