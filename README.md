# Virus Scanner

A simple cross-platform security scanner for source code.  
Supports Windows + Linux and detects suspicious patterns in multiple programming languages.

---

## Features
- Terminal UI (arrow keys, space, enter)
- Per-file JSON reports (`safe`, `maybe_safe`, `not_safe`)
- Supports: Python, C++, Shell, Go, Java, JS, TS, Rust, PHP, Ruby, C#, Kotlin, Swift, Lua
- Works on Windows & Linux

---

## Install

### Windows
```cmd
pip install readchar
python scanner.py

Linux

sudo apt install python3 python3-pip -y
sudo pip3 install --break-system-packages readchar
python3 scanner.py

Use

    Put files in input/

    Run the scanner

    Select file types in the menu

    Reports appear in out/DATE_TIME/

Example

Input: test.py
Output: test_py_safe.json
