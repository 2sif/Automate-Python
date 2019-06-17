#! python3

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidth = 0
    for string_list in table:
        for word in string_list:
            if len(word) > colWidth:
                colWidth = len(word)
    for i in range(len(table[0])):
        for a in range(len(table)):
            print(table[a][i].rjust(colWidth, ' '), end='')
        print('\n')

printTable(tableData)