def addDummy(data, col, dummy):

    dum_count = col - len(data)%col
    dumed = data
    if len(data)%col != 0:
        dumed += dum_count * dummy

    return dumed

def string2table(data, col, dummy):
    final = []
    temp = addDummy(data, col, dummy)
    while len(temp) != 0:
        final.append(temp[0:col])
        temp = temp[col:]
    return final

def transpo(table: list, col: int):
    col_list = []
    temp = ''
    for i in range(col):
        for j in range(len(table)):
            temp += table[j][i]
        col_list.append(temp)
        temp = ''
    return col_list

def encrypt(plain, key: str, dummy):

    # print dummy text
    print(f"The dummy character is: {dummy}")

    encrypted = []
    col_count = len(key)

    # displaying plaintext in table
    table = string2table(plain, col_count, dummy)
    print("Plain text in a table:")
    for i in range(col_count):
        print(f"{i+1}", end='\t')
    print()
    for i in table:
        for j in i:
            print(f"{j}", end='\t')
        print()

    row_count = len(table)
    col_list = transpo(table, col_count)
    key_list = [int(i) for i in key]
    
    for i in key_list:
        encrypted.append(col_list[i-1])

    encrypted = transpo(encrypted, row_count)

    print("Cipher text in a table:")
    for i in key_list:
        print(f"{i}", end='\t')
    print()
    for i in encrypted:
        for j in i:
            print(f"{j}", end='\t')
        print()


    theString = ''
    for i in encrypted:
        theString += i
    
    return theString