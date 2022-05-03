from math import floor


def cal_frame_lost(total_frame, lost_interval, lost_amount):
    frame = total_frame
    lost = 0
    current_lost = 0
    remaining_frame = 0

    while True:
        if frame >= lost_interval:
            current_lost = floor(frame/lost_interval) * lost_amount
            print(f"In {frame} frames, there are ⎿ {frame} / {lost_interval} ⏌ x {lost_amount} = {current_lost} lost", end="")
            remaining_frame = frame - floor(frame/lost_interval) * lost_interval
            frame = current_lost + remaining_frame
            print(f", and {remaining_frame} frames remaining")
            lost += current_lost

        if current_lost + remaining_frame < lost_interval:
            print(f"In {current_lost} + {remaining_frame} = {current_lost + remaining_frame} frames < {lost_interval} frames, no lost happens")
            break

    return lost

def recursive_cal_frame_lost(total_frame, lost_interval, lost_amount):
    if total_frame <= lost_interval:
        return
    else :
        pass