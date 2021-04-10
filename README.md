# PROJNAME

PROJNAME is a system helping to enforce occupancy limits in public spaces by counting people coming in and out.
It comprises:
* a central server for tracking devices,
* counter devices with ultrasonic and IR sensors,
* displays with a warning sign for visitors,
* control panels for security.

## Display

Display show the number of people currently in the space. When treshold is reached, warning light turns red and the display is blinking.

<p align="center">
    <img src="readme/display-green.jpg" width="300" />
    <img src="readme/display-red.jpg" width="300" />
</p>

## Control panel

Control panel lets staff to quickly adjust recorded occupancy by:
* adding to counter,
* resetting counter value,
* subtracting to counter.

<p align="center">
    <img src="readme/control-panel.jpg" width="300" />
</p>

## Ultrasound sensors

A pair of HC-SR04 ultrasound sensors detects when someone enter or exit room.
It sends events to main server thus can operate as standalone device based on Raspberry PI.

Beside power and ground pins, the sensors require 4 GPIO pins (each sensor has TRIGER and ECHO pins).

<p align="center">
    <img src="readme/ultrasound.jpg" width="400" />
</p>


## Development

Pins in use:
* GPIO 18: display LED
* GPIO 20, 21, 26, 13, 6, 16, 19: rightmost counter display
* GPIO 1, 12, 5, 0, 11, 8, 7: leftmost counter display
* GPIO 15, 23, 25: control buttons
* GPIO 17: beam ir sensor
