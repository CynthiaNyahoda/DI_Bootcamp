
def replace_symbols(matrix):
    result = []
    for row in matrix:
        new_row = ''
        in_group = False
        for char in row:
            if char.isalpha():
                in_group = False
                new_row += char
            elif not in_group:
                in_group = True
                new_row += ' '
        result.append(new_row)
    return result

matrix = ['7i3', 'Tsi', 'h%x', 'i #', 'sM ', '$a ', '#t%', '^r!']
secret_message = replace_symbols(matrix)
print('Secret message:')
for row in secret_message:
    print(row)
