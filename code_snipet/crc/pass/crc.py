import argparse

# extract needed part of the dataword
def slice(data, poly):
    return []

# do the xor calculation
def Xor(data__, divisor__):
    result = ''
    for i in range(1, len(data__)):
        if data__[i]==divisor__[i]:
            result += '0'
        else:
            result += '1'
    return result

def divise(word, g__):
    space_counter = 0

    len_g = len(g__)
    zero_div = len_g*'0'
    print(f'\nZero devisor = {zero_div}')

    steps = len(word) - len_g + 1

    xor_word = word[0:len_g]
    # print(steps)
    for i in range(steps):
        # xor_word xor with g__, store in xor_word, removing first digit, add next digit from word
        if i == steps-1:
            if xor_word[0] == '0':
                xor_word = Xor(xor_word, zero_div)
                print(xor_word, end=f'\t {i}\n')
            else:
                xor_word = Xor(xor_word, g__)
                print(xor_word, end=f'\t {i}\n')
            return xor_word
        
        if i < steps-1:
            if xor_word[0] == '0':
                xor_word = Xor(xor_word, zero_div)
                xor_word += word[i + len_g]                
                print(xor_word, end=f'\t {i}\n')
            else:
                xor_word = Xor(xor_word, g__)
                xor_word += word[i + len_g]
                print(xor_word, end=f'\t {i}\n')
    
    return xor_word

def check(data):

    for i in data:
        if i != '0':
            return False
    
    return True

parser = argparse.ArgumentParser()

parser.add_argument('-d','--data', help='Enter dataword as parameter', nargs=1)
parser.add_argument('-g','--poly-g', help='Enter G as parameter', nargs=1)
parser.add_argument('-c','--check', help='Check codeword', action='store_true')

args = parser.parse_args()

if not args.check:
    if args.data is None:
        data = input('Enter dataword: ')
    else:
        data = args.data[0]

    if args.poly_g is None:
        polyNom = input('Enter polynomial G:')
    else:
        polyNom = args.poly_g[0]

    partcial = []

    # for i in range(len(dataword)):
    #     partcial.append(dataword[i:i+3])

    dataword = data + (len(polyNom) - 1)*'0'
    print(f'\nZero added dataword: {dataword}')

    print(f'\nPolynomial is: {polyNom}')

    crc = divise(dataword, polyNom)
    codeword = data + crc
    print(f'crc is: {crc}')
    print(f'codeword is: {codeword}')

if args.check:
    if args.data is None:
        data = input('Enter codeword: ')
    else:
        data = args.data[0]

    if args.poly_g is None:
        polyNom = input('Enter polynomial G:')
    else:
        polyNom = args.poly_g[0]

    partcial = []

    # for i in range(len(dataword)):
    #     partcial.append(dataword[i:i+3])

    dataword = data
    print(f'\ndataword: {dataword}')

    print(f'\nPolynomial is: {polyNom}')

    crc = divise(dataword, polyNom)

    if check(crc):
        print(f'crc is: {crc}')
        print(f"No errors")
    else:
        print(f"error occurs")