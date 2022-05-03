import argparse
from mod.decrypt import *
from mod.encrypt import *

parser = argparse.ArgumentParser()

parser.add_argument('-e','--encrypt', help='Enter plain text for encryption', nargs='?', type=str)
parser.add_argument('-d','--decrypt', help='Enter cipher text for decryption', nargs='?', type=str)
parser.add_argument('-x','--dummy', help='Enter lost amount', nargs=1, type=str)
parser.add_argument('-k','--key', help='Enter key', nargs=1, type=str)

args = parser.parse_args()

if args.encrypt:
    cText = encrypt(args.encrypt, args.key[0], args.dummy[0])
    print('Chipher text in string:')
    print(f"\'{cText}\'")

if args.decrypt:
    pText = decrypt(args.decrypt, args.key[0], args.dummy[0])
    print('Plain text in string:')
    print(f"\'{pText}\'")
