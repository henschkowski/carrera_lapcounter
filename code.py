# Gemma IO demo
# Welcome to CircuitPython 2.2.4 :)

from digitalio import DigitalInOut, Direction, Pull
import touchio
import board
import time

######################### MAIN LOOP ##############################

touch = touchio.TouchIn(board.A1)
contact = [DigitalInOut(board.D0), DigitalInOut(board.D1)]
contact[0].direction = Direction.INPUT
contact[1].direction = Direction.INPUT
contact[0].pull = Pull.UP
contact[1].pull = Pull.UP

laps = [0, 0]
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
    else:
        touch_count = 0
    
    for i in (0, 1):
        if not contact[i].value and not contact_pressed[i]:
            if first[i]:
                last_contact_time[i] = time.monotonic()
                contact_pressed[i] = True
                track_num = 1 if i == 1 else 2
                first[i] = False
                print("Start on track %d !" % (track_num,))
            else:
                lap_time = time.monotonic() - last_contact_time[i]
                last_contact_time[i] = time.monotonic()
                contact_pressed[i] = True
                laps[i] += 1
                track_num = 1 if i == 1 else 2
                print("Track %s: laps = %d, lap_time = %f" % (track_num, laps[i], lap_time))
        if contact[i].value and contact_pressed[i]:
            contact_pressed[i] = False



