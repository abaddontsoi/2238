data = input('input codeword: ')
g = input('Enter G: ')

def slicing(data__, g__):
    len_g = len(g__)
    # return [ data__[i:i + len_g] for i in range(len(data__)) if len(data__[i:i + len_g])==len_g]
    return [ 
        data__[i:i + len_g] 
        for i in range(len(data__)) 
            if len(data__[i:i + len_g])==len_g
    ]

print(slicing(data, g)) 