#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: python mcb.pyw save <keyword> - Saves clipboard to keyword.
#        python mcb.pyw <keyword> - Loads keyword to clipboard.
#        python mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys, os

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif sys.argv[1].lower() == 'delete':
    if sys.argv[2] in mcbShelf:
        del mcbShelf[sys.argv[2]]
    elif sys.argv[2] == 'ALL':
        os.remove('mcb')
    else:
        print("Invalid argument or keyword")
# List keywords and load content.
elif sys.argv[1].lower() == 'list':
    pyperclip.copy(str(list(mcbShelf.keys())))
elif sys.argv[1] in mcbShelf:
    pyperclip.copy(mcbShelf[sys.argv[1]])
else:
    print("Invalid argument or keyword.")


mcbShelf.close()