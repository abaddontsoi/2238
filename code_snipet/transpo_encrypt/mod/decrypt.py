def removeDummy(data: str, dummy):
    dumed = data
    clean  = dumed.replace(dummy,'')
    return clean

def string2table(data, col):
    final = []
    while len(data) != 0:
        final.append(data[0:col])
        data = data[col:]
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

def decrypt(cipher, key: str, dummy):

    # print dummy text
    print(f"The dummy character is: {dummy}")
    
    col_count = len(key)

    table = string2table(cipher, col_count)
    row_count = len(table)
    col_list = transpo(table, col_count)
    key_list = [int(i) for i in key]

    # displaying cipher text in table
    print("Cipher text in a table:")
    for i in key_list:
        print(f"{i}", end='\t')
    print()
    for i in table:
        for j in i:
            print(f"{j}", end='\t')
        print()


    decrypted = {}
    for i in range(col_count):
        decrypted.update({
            int(key_list[i]): col_list[i]
        })
    
    organized = []
    theString = ''
    for i in range(len(decrypted)):
        organized.append(decrypted[i+1])
    
    organized = transpo(organized, row_count)
    for i in organized:
        theString += i

    # print plain text in a table
    print("Plain text in a table:")
    for i in range(col_count):
        print(f"{i+1}", end='\t')
    print()
    for i in organized:
        for j in i:
            print(f"{j}", end='\t')
        print()

    theString = removeDummy(theString, dummy)

    return theString