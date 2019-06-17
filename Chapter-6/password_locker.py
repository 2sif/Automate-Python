#! python3
# password_locker.py - An insecure password locker program

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python password_locker.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   # first command line arg is the account name

if account.lower() in PASSWORDS:
    pyperclip.copy(PASSWORDS[account.lower()])
    print('Password for ' + account.lower() + ' copied to clipboard.')
else:
    print('There is no account name ' + account)