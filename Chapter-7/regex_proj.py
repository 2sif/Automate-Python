#! python3
# regex_proj.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(\(?\d{3}\)? ?)?-?(\d{3}-?\d{4})''')

emailRegex = re.compile(r'''''')