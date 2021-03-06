# Gemma IO demo
# Welcome to CircuitPython 2.2.4 :)

from digitalio import DigitalInOut, Direction, Pull
import touchio
import board
import time
import sys

######################### MAIN LOOP ##############################

touch = touchio.TouchIn(board.A1)
contact = [DigitalInOut(board.D0), DigitalInOut(board.D1)]
contact[0].direction = Direction.INPUT
contact[1].direction = Direction.INPUT
contact[0].pull = Pull.UP
contact[1].pull = Pull.UP

laps = [0, 0]
best_lap_time = [1000,1000]
last_contact_time = [0.0, 0.0]
contact_pressed = [False, False]

first = [True, True]

touch_count = 10000

while True:
    time.sleep(0.01)

    if touch.value:
        touch_count += 1
        
        if touch_count == 200:
            print("-------------------- RESET --------------------")
            laps = [0, 0]
            last_contact_time = [0.0, 0.0]
            contact_pressed = [False, False]
            first = [True, True]
            last_touch_time = 0.0
            best_lap_time = [1000.0, 1000.0]

    else:
        touch_count = 0
    
    for i in (0, 1):
        if not contact[i].value and not contact_pressed[i]:
            last_contact_time[i] = time.monotonic()
            contact_pressed[i] = True
            track_num = 1 if i == 1 else 2

            if first[i]:
                first[i] = False
                print("Start on track %d !" % (track_num,))
                continue
            
            lap_time = time.monotonic() - last_contact_time[i]
            last_contact_time[i] = time.monotonic()
            contact_pressed[i] = True
            laps[i] += 1
            track_num = 1 if i == 1 else 2

            if lap_time < 2:
                lap_time = "N/A"
            elif lap_time < best_lap_time[i]:
                best_lap_time[i] = lap_time 

            print("Track %s: laps = %d, lap_time = %s, best_lap_time = %f" % (track_num, laps[i], lap_time, best_lap_time[i]))
        if contact[i].value and contact_pressed[i]:
            contact_pressed[i] = False



