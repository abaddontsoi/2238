import argparse
from mod.RSA import *

parser = argparse.ArgumentParser()

parser.add_argument('-p','--the-p', help='', nargs='?', type=int)
parser.add_argument('-q','--the-q', help='', nargs='?', type=int)
parser.add_argument('-e','--the-e', help='', nargs='?', type=int)
parser.add_argument('-d','--the-d', help='', nargs='?', type=int)

args = parser.parse_args()

try:
    u = rsa(args.the_p, args.the_q, args.the_e, args.the_d)
    u.display()
except Exception as e:
    print(e)