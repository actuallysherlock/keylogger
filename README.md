# ⌨️ Keylogger
> [!CAUTION]
> This repository contains code intended solely for educational purposes. It is designed to demonstrate how keyloggers function and their potential security implications. The author does not remain accountable for any malicious activities, including but not limited to unauthorized surveillance, data theft, or cyberattacks, resulting from the use of this code.

This is a simple key-logging script developed in Python 3, by using pynput and os along with datetime to ensure user-friendly logging.

## Features
- Real-time logging.
- User friendly logging with the exact time and aliases for keys such as Space, CTRL, and Windows.
- Logs all keystrokes in a specified file (default is keylogs.log).

## Setup
> [!NOTE]
> To get started run the following commands (Make sure you have Python 3, pip and git installed on your machine)

**Clone the repository**
```bash
git clone https://github.com/saayxee/keylogger
```
**Change directory**
```bash
cd "keylogger"
```
**Install pynput**
```bash
pip install pynput
```

## Usage
**Run the file**
```bash
python keylogger.py
```
**Navigate to the logs**
```bash
cd path/to/your/configured/log/file # If you didn't change anything, you should find it beside the main keylogger script.
```

