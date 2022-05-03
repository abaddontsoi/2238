from argparse import ArgumentParser


parser = ArgumentParser()

parser.add_argument('-o', '--odd', help='Using odd parity', action='store_true')
parser.add_argument('-e', '--even', help='Using even-parity', action='store_true')
parser.add_argument('-v', '--validate', help='Checking whether the bitstream is correct.', action='store_true')
parser.add_argument('-c', '--encode', help='Encode the bit stream', action='store_true')

args = parser.parse_args()



two_DP = input('Enter bits, separate in space: ')

two_DP_list = two_DP.split(' ')

err_row = []
err_col = []

def encode(data: str, mod: int):
    ones = data.count('1')
    if mod == 2 and ones%2 == 1:
        data += '1'
    if mod == 1 and ones%2 == 0:
        data += '1'
    if mod == 2 and ones%2 == 0:
        data += '0'
    if mod == 1 and ones%2 == 1:
        data += '0'

    return data


ans_string = ''
if args.encode and args.even:
    for i in two_DP_list:
        ans_string += encode(i, 2)
        ans_string += ' '
    print(ans_string)

if args.encode and args.odd:
    for i in two_DP_list:
        ans_string += encode(i, 1)
        ans_string += ' '
    print(ans_string)

# print(two_DP_list[-1])
def select_digit(num, position: int):
    return str(num)[position]

def concat_str(__list__):
    __str = ''
    for i in __list__:
        __str += i
    return __str
        
if args.validate and args.even :
    for i in two_DP_list:
        print(i, end='\t')
        ones_row = i.count('1')
        if ones_row%2 == 0:
            print(f'1s: {ones_row}')
        if ones_row%2 == 1:
            print(f'1s: {ones_row}, error occurs ')
            err_row.append(two_DP_list.index(i))
    print()
    col_collection = []
    for item in range(len(two_DP_list[0])):
        result = [select_digit(n, item) for n in two_DP_list]
        ones_col = result.count('1')
        print(concat_str(result), end='\t')
        if ones_col%2 == 0:
            print(f'1s: {ones_col}')
        if ones_col%2 == 1:
            print(f'1s: {ones_col}, error occurs ')
            err_col.append(item)

    print(f'error in row {err_row}')
    print(f'error in col {err_col}')

if args.validate and args.odd:
    for i in two_DP_list:
        print(i, end='\t')
        ones_row = i.count('1')
        if ones_row%2 == 1:
            print(f'1s: {ones_row}')
        if ones_row%2 == 0:
            print(f'1s: {ones_row}, error occurs ')
            err_row.append(two_DP_list.index(i))
    print()
    col_collection = []
    for item in range(len(two_DP_list[0])):
        result = [select_digit(n, item) for n in two_DP_list]
        ones_col = result.count('1')
        print(concat_str(result), end='\t')
        if ones_col%2 == 1:
            print(f'1s: {ones_col}')
        if ones_col%2 == 0:
            print(f'1s: {ones_col}, error occurs ')
            err_col.append(item)

    print(f'error in row {err_row}')
    print(f'error in col {err_col}')