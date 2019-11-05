#! python3
# regex_proj.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re
text = str(pyperclip.paste())
emails_raw = []
phones_raw = []
matches = []

phoneRegex = re.compile(r'''(\(?\d{3}\)? ?)?-?(\d{3}-?\d{4})''')
emailRegex = re.compile(r'''(\w+)(@\w+\.\w+)''')

for groups in emailRegex.findall(text):
    emails_raw.append(groups)
for email_tuple in emails_raw:
    matches.append(''.join(email_tuple))

for groups in phoneRegex.findall(text):
    phones_raw.append(groups)
for phone_tuple in phones_raw:
    matches.append(''.join(phone_tuple))

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No email addresses or phone numbers found.')