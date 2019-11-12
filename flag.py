class ArgumentError(Exception):
    pass

def flag(N):
    try:
        N = int(N)
        if N % 2 or not int:
            raise ArgumentError('The parameter is not a valid even integer number')
    except ValueError:
        raise ValueError('It\'s not integer')


    width = N * 3
    height = N * 2
    vertical_distance = N // 2    
    flag_draw = '#' * (width + 2) + '\n'

    for i in range(height):
        if i in range(vertical_distance) or i in range(height - vertical_distance, height):
            spaces = ' ' * width
            flag_draw += '#' + spaces + '#' + '\n'
        elif i == N or i == N-1:
            spaces = ' ' * N
            symbol_o = 'o'*(N-2)
            flag_draw += '#' + spaces + '*' + symbol_o + '*' + spaces + '#' + '\n'
        else:
            if i < N-1:
                spaces_count = height - 1 - i     
            else:
                spaces_count = i
            spaces = ' ' * spaces_count
            symbol_o = 'o'*(width - spaces_count*2 - 2)
            flag_draw += '#' + spaces + '*' + symbol_o + '*' + spaces + '#' + '\n'  

    flag_draw += '#' * (width + 2)
    return flag_draw 



print(flag(input('Enter digit: ')))