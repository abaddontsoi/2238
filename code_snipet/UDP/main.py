import argparse
from mod.udp import udp

parser = argparse.ArgumentParser()

parser.add_argument('-u', '--udp-hex', help='Enter UDP header in HEX',  type=str)
parser.add_argument('-s', '--get-src-port', help='Get packet source port', action='store_true')
parser.add_argument('-d', '--get-des-port', help='Get packet destination port', action='store_true')
parser.add_argument('-t', '--get-total-len', help='Get packet total length', action='store_true')
parser.add_argument('-c', '--get-checksum', help='Get packet checksum', action='store_true')
parser.add_argument('-a', '--get-all', help='Get packet header all properties', action='store_true')


args = parser.parse_args()

# print(args.udp_hex)
try:
    u = udp(args.udp_hex)
except Exception:
    print('Error')

if args.get_src_port:
    print(u.get_src_port())

if args.get_des_port:   
    print(u.get_des_port())

if args.get_total_len:
    print(u.get_total_len())

if args.get_checksum:
    print(u.get_checksum())

if args.get_all:
    u.print_all_dec()
