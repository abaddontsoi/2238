from math import ceil, floor


def cal_gbn_delay(total_size, frame_size, dis, p_speed, chan_data_rate, wind_size, ack_size=0):
    complet_frame_count = floor(total_size/frame_size)
    incomplete_frame_size = total_size%frame_size or None
    tp = (dis/p_speed) * 1000
    pack_tx = frame_size/chan_data_rate * 1000
    ack_tx = ack_size/chan_data_rate * 1000


    print(f'No. of complete frames to be sent = ⎿{total_size}bits/ {frame_size}bits⏌ = {complet_frame_count}')
    print(f'Size of last frame = {incomplete_frame_size}')

    print('\nFor 1 round trip')
    print(f'Propagation delay of a packet =  {dis}/{p_speed} = {tp} ms')
    print(f'Transmission Delay of a packet = {frame_size} bit / {chan_data_rate}bps = {pack_tx} ms')
    print(f'Transmission Delay of an ACK (Tx) = {ack_size}/{chan_data_rate}bps = {ack_tx} ms')
    print(f'Propagation delay of an ACK =  {dis}/{p_speed} = {tp} ms')

    round_trip_delay = tp + tp + pack_tx + ack_tx
    print(f'Delay for one round trip = {tp}ms + {tp}ms + {pack_tx}ms + {ack_tx}ms = {round_trip_delay} ms')

    rep = complet_frame_count / wind_size
    remain_wind_size = complet_frame_count % wind_size

    all_complete_round_trip_delay = rep*round_trip_delay

    if remain_wind_size == 0:
        print(f'\nNo. of repetition = {complet_frame_count} / {wind_size} = {rep}')
        print(f'Delay for the {rep} rounds = {rep} x {round_trip_delay} = {all_complete_round_trip_delay}ms')
    else:
        print(f'\nNo. of repetition = {complet_frame_count} / {wind_size} = {rep}')
        print(f'{ceil(rep)} rounds are needed')
        print(f'Delay for the first {floor(rep)} rounds = {floor(rep)} x {round_trip_delay} = {floor(rep)*round_trip_delay} ms')

        if incomplete_frame_size:
            remain_frames = ceil(total_size/frame_size) - floor(rep) * wind_size
            last_frame_tx = incomplete_frame_size/chan_data_rate * 1000
            last_trip_time = tp + tp + (remain_frames - 1) * pack_tx + last_frame_tx
            print(f'\nIn the last round, it has {remain_frames} frames')
            print(f'Delay for the last round = {tp} + {tp} + {remain_frames-1}x{pack_tx}ms + {last_frame_tx}ms = {last_trip_time} ms')

            print(f'\nTotal Delay = {floor(rep)*round_trip_delay} + {last_trip_time} = {floor(rep)*round_trip_delay+last_trip_time} ms')
        else:
            remain_frames = ceil(total_size/frame_size) - floor(rep) * wind_size
            last_trip_time = tp + tp + remain_frames * pack_tx 
            print(f'\nIn the last round, it has {remain_frames} frames')
            print(f'Delay for the last round = {tp} + {tp} + {remain_frames}x{pack_tx}ms = {last_trip_time} ms')

            print(f'\nTotal Delay = {floor(rep)*round_trip_delay} + {last_trip_time} = {floor(rep)*round_trip_delay+last_trip_time} ms')