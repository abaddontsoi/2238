import argparse
from mod.cal_frame_lost import cal_frame_lost, recursive_cal_frame_lost

parser = argparse.ArgumentParser()

parser.add_argument('-f','--frames', help='Enter total frames for calculation', nargs=1, type=int)
parser.add_argument('-i','--lost-interval', help='Enter lost interval', nargs=1, type=int)
parser.add_argument('-a','--lost-amount', help='Enter lost amount', nargs=1, type=int)

args = parser.parse_args()

lost_frame = cal_frame_lost( args.frames[0], args.lost_interval[0], args.lost_amount[0])

print(f"No. of frame lost = {lost_frame}")
print(f'Total delay = original delay + (delay per frame + timeout)*{lost_frame}')