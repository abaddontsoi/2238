import argparse
from mod.gbn import *

parser = argparse.ArgumentParser()

# total_size, frame_size, dis, p_speed, chan_data_rate, wind_size, ack_size=0
parser.add_argument('-t', '--total-size', help='Total data size in BIT', nargs=1, type=int)
parser.add_argument('-f', '--frame-size', help='Frame size in BIT', nargs=1, type=int)
parser.add_argument('-d', '--distance', help='Distance in Meter', nargs=1, type=int)
parser.add_argument('-p', '--propagation-speed', help='Propagation time in ms^-1', nargs=1, type=int)
parser.add_argument('-c', '--channel-data-rate', help='Channel data rate in bps', nargs=1, type=int)
parser.add_argument('-w', '--windows-size',help='Windows size', nargs=1, type=int)
parser.add_argument('-a', '--ack-size',help='ACK size in BIT', nargs=1, type=int)

args = parser.parse_args()

cal_gbn_delay(args.total_size[0], args.frame_size[0], args.distance[0], args.propagation_speed[0], 
    args.channel_data_rate[0], args.windows_size[0], args.ack_size[0])