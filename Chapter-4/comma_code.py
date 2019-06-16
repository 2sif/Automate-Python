def commacode(list):
    for i in range(len(list)):
        if list[i] == list[-1]:
            print(str(list[i]))
        else:
            print(str(list[i]) + ', ', end='')

spam = ['a', 4, 0, ['apple', 'orange', 'pear'], 43214, 'tousif']

# String only
'''
while True:
    if len(spam) != 0:
        print("spam = " + str(spam))
    print("Enter list value. Enter nothing to end list.")
    list_value = input()
    if list_value == '':
        break
    spam.append(list_value)
'''
commacode(spam)