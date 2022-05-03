# data    = input('Enter codeword: ')
# divisor = input('Enter divisor: ')
default_divisor = '0000'

# def div(data__, divisor__):
#     result = ''
#     for i in range(1, len(data__)):
#         if data__[i]==divisor__[i]:
#             result += '0'
#         else:
#             result += '1'
#     return result

# dived = ''
# if data[0]=='1':
#     dived = div(data, divisor)
# if data[0]=='0':
#     dived = div(data, default_divisor)

# print(dived)


# def divise(word, g__, divisor__):
#     len_g = len(g__)
#     zero_div = len_g*'0'
#     print(f'\nDefault devisor = {zero_div}')
#     xor_word = word[0:len_g]
#     for item in range( len(word)-len_g+1 ):
#         xor_word += word[item + len_g]
#         print(xor_word)
#     return 



# str1 = '1234'
# # str2 = str1 - str1[0]
# str1 = str1[1:]

# print(str1)

def Xor(data__, divisor__):
    result = ''
    for i in range(1, len(data__)):
        if data__[i]==divisor__[i]:
            result += '0'
        else:
            result += '1'
    return result

def divise(word, g__):
    len_g = len(g__)
    zero_div = len_g*'0'
    print(f'\nZero devisor = {zero_div}')

    steps = len(word) - len_g + 1

    xor_word = word[0:len_g]
    print(steps)
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

# xor_word = Xor('1100', '1101')
# print(xor_word)

print(divise('100100000', '1101'))