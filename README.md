<h1 align="center">🛡️ Virus Scanner</h1>
<p align="center">
A fast, cross-platform source code security scanner for developers.  
Detects suspicious, malicious, or unsafe patterns in multiple programming languages.  
</p>

<p align="center">
  <img src="https://img.shields.io/badge/platform-Windows%20%7C%20Linux-blue" />
  <img src="https://img.shields.io/badge/status-active-success" />
  <img src="https://img.shields.io/badge/license-MIT-green" />
</p>

---

## 🚀 Overview

**Virus Scanner** analyzes source code files and identifies potentially unsafe or malicious behavior.  
It provides **per-file security reports**, supports many programming languages, and works on both **Windows and Linux**—all without external tools.

The built-in interactive terminal UI makes scanning extremely simple.

---

## ✨ Features

- ✔ **Cross-platform:** Windows & Linux  
- ✔ **Interactive UI:** Arrow keys, Space, Enter  
- ✔ **Multi-language scanning:**  
  Python, C++, Shell, Go, Java, JavaScript, TypeScript, Rust, PHP, Ruby, C#, Kotlin, Swift, Lua  
- ✔ **Per-file JSON reports**  
- ✔ **Suspicious line logging**  
- ✔ **Timestamped output folders**  
- ✔ **No external antivirus engine needed**

---

## 📁 Project Structure

VirusScanner/
├── scanner.py # main scanner
├── detectors/ # language-based detectors
├── utils/ # logging + file loader
├── input/ # files to scan
└── out/ # generated reports


---

## 🔧 Installation

### Windows

```cmd
pip install readchar
python scanner.py

Linux

sudo apt update
sudo apt install python3 python3-pip -y
sudo pip3 install --break-system-packages readchar
python3 scanner.py

🖥️ Usage
1. Add files you want to scan

Place them in:

input/

Example:

input/script.py
input/main.cpp
input/run.sh

2. Run the scanner

Windows:

python scanner.py

Linux:

python3 scanner.py

3. Select file types

Use the terminal UI:
Key	Action
↑ / ↓	Move selection
SPACE	Select file type
ENTER	Start scanning
ESC	Exit
4. View Reports

Reports are saved in automatically created folders:

out/YYYY-MM-DD_HH-MM-SS/

Each file gets its own JSON report:

script_py_safe.json
main_cpp_not_safe.json
run_sh_maybe_safe.json

🧪 Example Files

Safe:

print("Hello")

Maybe suspicious:

data="dGVzdA=="

Not safe:

std::string url = "https://discord.com/api/webhooks/123/abc";

🔒 Detection Categories
✔ SAFE

No suspicious content found.
⚠️ MAYBE SAFE

Patterns that might be unsafe depending on context.

Examples:

    Encoded strings

    Suspicious variables

    High-entropy tokens

❌ NOT SAFE

Clearly malicious patterns.

Examples:

    Discord/Slack Webhooks

    Reverse shell commands

    eval, exec, subprocess misuse

    Encoded malware payloads

🧩 Tech Stack

    Python 3.10+

    readchar for terminal UI

    Pure Python — no external antivirus engines

📜 License

This project is licensed under the MIT License.
🤝 Contributing

Contributions, issues, and feature requests are welcome.
🌟 Star This Project

If you find this project useful, please consider giving it a ⭐ on GitHub — it helps a lot!
