import argparse
from mod.IPH import IPH

parser = argparse.ArgumentParser()

parser.add_argument('-i','--ip-hex', help='', nargs='?', type=str)
parser.add_argument('-v','--version', help='Version Number', action='store_true')
parser.add_argument('-H','--hlen', help='Header Length', action='store_true')
parser.add_argument('-s','--service-type', help='Service type', action='store_true')
parser.add_argument('-t','--total-len', help='Total Length', action='store_true')
parser.add_argument('-I','--identification', help='Identification', action='store_true')
parser.add_argument('-f','--flags', help='Flags', action='store_true')
parser.add_argument('-F','--fragment-offset', help='Fragment Offset', action='store_true')
parser.add_argument('-T','--ttl', help='Time-to-live', action='store_true')
parser.add_argument('-p','--protocol', help='Protocol', action='store_true')
parser.add_argument('-c','--checksum', help='Header Checksum', action='store_true')
parser.add_argument('-S','--src-ip', help='Source IP address', action='store_true')
parser.add_argument('-D','--des-ip', help='Destination IP address', action='store_true')
parser.add_argument('-a','--all', help='Show all detail', action='store_true')

args = parser.parse_args()

try:
    u = IPH(args.ip_hex)
except Exception:
    print('error')

if args.version:
    u.show_version()
if args.hlen:
    u.show_hlen()
if args.service_type:
    u.show_ser_type()
if args.total_len:
    u.show_t_len()
if args.identification:
    u.show_iden()
if args.flags:
    u.show_flags()
if args.fragment_offset:
    u.show_frag_offset()
if args.ttl:
    u.show_ttl()
if args.protocol:
    u.show_protocol()
if args.checksum:
    u.show_h_checksum()
if args.src_ip:
    u.show_src_ip()
if args.des_ip:
    u.show_des_ip()
if args.all:
    u.show_all()