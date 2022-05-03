h2b = {
    '0':'0000',
    '1':'0001',
    '2':'0010',
    '3':'0011',
    '4':'0100',
    '5':'0101',
    '6':'0110',
    '7':'0111',
    '8':'1000',
    '9':'1001',
    'A':'1010',
    'B':'1011',
    'C':'1100',
    'D':'1101',
    'E':'1110',
    'F':'1111',
}

class udp:
    def __init__(self, raw: str):
        self.hex = raw
        self.bin = self.hex2bin(self.hex)
        self.src_port = self.bin[:16]
        self.des_port = self.bin[16:32]
        self.total_len = self.bin[32:48]
        self.checksum = self.bin[48:]

    def __repr__(self):
        return f'{self.src_port}\n{self.des_port}\n{self.total_len}\n{self.checksum}'

    def hex2bin(self,data):
        bin = ''
        for i in data:
            bin += h2b[i]
        return bin

    def bin2dec(self, data: str):
        dec = 0
        # exp = 15
        exp = len(data) - 1
        for i in data:
            if i == '1':
                dec += 2**exp
            exp -= 1
        return dec

    def get_src_port(self):
        return self.bin2dec(self.src_port)


    def get_des_port(self):
        return self.bin2dec(self.des_port)


    def get_total_len(self):
        return self.bin2dec(self.total_len)
    

    def get_checksum(self):
        return self.bin2dec(self.checksum)

    def print_all_dec(self):
        print(f"Source port: {self.bin2dec(self.src_port)}")
        print(f"Destination port: {self.bin2dec(self.des_port)}")
        print(f"Header + data: {self.bin2dec(self.total_len)} bytes")
        print(f"Checksum: {self.bin2dec(self.checksum)}")

