A lap counter / lap timer for the old analog Carrera (Evolution) 1:24 tracks.

A photointerruptor is embedded into each slot and connected to a
Adafruit Gemma M0 microcontroller. Time and laps are measured by the
microcrontroller and sent through the USB/Serial connection to a
terminal (laptop).

![Fritzing image of circuit](https://github.com/henschkowski/carrera_lapcounter/blob/master/carrera_rundenzaehler_bb.png)


Parts:
- Adafruit Gemma M0 or similar, with CircuitPython
- Resistors: 2x 1k Ohm , 2x 560 Ohm
- 2 photo interrupters, like Sharp GP1S52V or similar (3mm slit)



Idea, circuit and images also here:

http://www.slotrun.de/lichtschranke.htm