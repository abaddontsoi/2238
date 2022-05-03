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
flag = {
    '000':'Can be fragmented, last and only fragment',
    '001':'Can be fragmented, more fragment coming',
    '010':'Must not fragment',
    '011':'Error',
    '100':'Error',
    '101':'Error',
    '110':'Error',
    '111':'Error',
}

class IPH:
    def __init__(self, raw):
        self.hex = raw
        self.bin = self.hex2bin(self.hex)
        self.ver = self.bin[:4]
        self.hlen = self.bin[4:8]
        self.ser_type = self.bin[8:16]
        self.t_len = self.bin[16:32]
        self.iden = self.bin[32:48]
        self.flags = self.bin[48:51]
        self.frag_offset = self.bin[51:64]
        self.ttl = self.bin[64:72]
        self.protocol = self.bin[72:80]
        self.h_checksum = self.bin[80:96]
        self.src_ip = self.bin[96:128]
        self.des_ip = self.bin[128:160]

    def hex2bin(self,data):
        bin = ''
        for i in data:
            bin += h2b[i]
        return bin

    def bin2dec(self, data):
        dec = 0
        exp = len(data) - 1
        for i in data:
            if i == '1':
                dec += 2**exp
            exp -= 1 
        return dec

    def show_version(self):
        ver = self.bin2dec(self.ver)
        print(f'\nIP version: {self.ver} -> {ver}')

    def show_hlen(self):
        hlen = self.bin2dec(self.hlen) * 4
        print(f'\nHeader length: {self.hlen} -> {hlen} bytes')

    def show_ser_type(self):
        ser_type = self.bin2dec(self.ser_type)
        print(f'\nService type: {self.ser_type} -> {ser_type}')

    def show_t_len(self):
        tlen = self.bin2dec(self.t_len)
        print(f'\nTotal length: {tlen} bytes, Data size: {tlen-self.bin2dec(self.hlen) * 4}')

    def show_iden(self):
        iden = self.bin2dec(self.iden)
        print(f'\nIdentification: {self.iden} -> {iden}')

    def show_flags(self):
        print(f'\nFlags: {self.flags} -> {flag[self.flags]}')

    def show_frag_offset(self):
        offset_dec = self.bin2dec(self.frag_offset)
        print(f'\nFragment offset: {self.frag_offset} -> {offset_dec*8}th byte')
        
    def show_ttl(self):
        ttl = self.bin2dec(self.ttl)
        print(f'\nTime to live: {self.ttl} -> {ttl} router(s)')

    def show_protocol(self):
        protocol = self.bin2dec(self.protocol)
        print(f'\nProtocol: {self.protocol} -> {protocol}')
    
    def show_h_checksum(self):
        print(f'\nHeader checksum: {self.h_checksum}')
    
    def bin2dot_dec(self, data):
        first = self.bin2dec(data[0:8])
        second = self.bin2dec(data[8:16])
        third = self.bin2dec(data[16:24])
        fourth = self.bin2dec(data[24:32])
        return str(first) + '.' + str(second) + '.' + str(third) + '.' + str(fourth)

    def show_src_ip(self):
        src_ip = self.bin2dot_dec(self.src_ip)
        print(f'\nSource IP: {self.src_ip} -> {src_ip}')
    
    def show_des_ip(self):
        des_ip = self.bin2dot_dec(self.des_ip)
        print(f'\nDestination IP: {self.des_ip} -> {des_ip}')

    def show_all(self):
        self.show_version()
        self.show_hlen()
        self.show_ser_type()
        self.show_t_len()
        self.show_iden()
        self.show_flags()
        self.show_frag_offset()
        self.show_ttl()
        self.show_protocol()
        self.show_h_checksum()    
        self.show_src_ip()
        self.show_des_ip()
