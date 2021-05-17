# tabata timer is 20s work/10s rest, usually repeated 8x (4min) per movement
# and often done through 4 exercises (with no extra rest, that's 16min total)

import time

# kinda the cheating way to do it here:
work_list = [0, 30, 60, 90, 120, ...]
rest_list = [20, 50, 70, 110, ...]

def work_action():
    print('work!')
    return

def rest_action():
    print('rest!')
    return

def tabata_timer(max_time):

    print('Start!')

    for x in range(max_time):
        print(x)
        time.sleep(.1) # 1s normally, 0.1 or faster for testing...
        
        if x in work_list:
            work_action()
        if x in rest_list:
            rest_action()

tabata_timer(100)

# TODO make it beep!
# TODO make a GUI!