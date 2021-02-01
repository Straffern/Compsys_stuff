# Pretty print binary

def print_binary(width: int, address):
    _width = width-1
    binaryColumn = ''
    columnRange = range(_width, -1, -1)
    for i in columnRange:
        length = len(str(i))-1
        if i == _width: 
            binaryColumn += '|'
        binaryColumn += f'{i:>4}'
        binaryColumn += f'{"|":>{4-length}}'
    
    binaryString = ''
    column = iter(columnRange)
    for i in range(0, width):

        length = len(str(next(column)))-1
        if i == 0:
            binaryString += '|'
        binaryString += f'{address[2+i]:>4}'
        binaryString += f'{"|":>{4-length}}'
    print('_'*len(binaryString))
    print(binaryColumn)
    print("\u203e"*len(binaryString))
    print('_'*len(binaryString))
    print(binaryString)
    print("\u203e"*len(binaryString))
    # print('_'*len(binaryString))

# WIDTH = 32
# ADDRESS = 5234161

# print_binary(WIDTH, format(ADDRESS, f'#0{WIDTH+2}b'))
