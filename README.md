# People counter

People counter is a system helping to enforce occupancy limits in public spaces by counting people coming in and out.
It comprises:
* a central server for tracking devices,
* counter devices with ultrasonic and IR sensors,
* displays with a warning sign for visitors,
* control panels for security.

See demo: https://www.youtube.com/watch?v=Mto_cI-SvnQ

## Hardware

### Ultrasound and beam sensors

A pair of HC-SR04 ultrasound sensors detects when someone enter or exit room.
It sends events to main server thus can operate as standalone device based on Raspberry PI.

Beside power and ground pins, the sensors require 4 GPIO pins (each sensor has TRIGGER and ECHO pins).

<p align="center">
    <a href="readme/ultrasound.jpg"><img src="readme/ultrasound.jpg" width="400" /></a>
</p>

<p align="center">
    <a href="readme/sensors-schematic.svg"><img src="readme/sensors-schematic.svg" width="400" /></a>
</p>

A single beam interruption sensor detects an event of entering or exiting the room, but doesn't distinguish between the two types.
It relies on the pair of ultrasound sensors to decide wheter an exit or an enter event occured.

The beam sensor requires a power pin, a ground pin and a GPIO pin.

### Display

Display shows the number of people who entered the space. When treshold is reached, warning light turns red and the display is blinking.

<p align="center">
    <a href="readme/display-green.jpg"><img src="readme/display-green.jpg" width="300" /></a>
    <a href="readme/display-red.jpg"><img src="readme/display-red.jpg" width="300" /></a>
</p>

<p align="center">
    <a href="readme/display-schematic.svg"><img src="readme/display-schematic.svg" width="600" /></a>
</p>

### Control panel

Control panel lets staff quickly adjust recorded occupancy by:
* adding to counter,
* resetting counter value,
* subtracting to counter.

<p align="center">
    <a href="readme/control-panel.jpg"><img src="readme/control-panel.jpg" width="300" /></a>
</p>

<p align="center">
    <a href="readme/control-panel-schematic.svg"><img src="readme/control-panel-schematic.svg" width="300" /></a>
</p>

## Development

Pins in use:
* GPIO 18: display LED
* GPIO 20, 21, 26, 13, 6, 16, 19: rightmost counter display
* GPIO 1, 12, 5, 0, 11, 8, 7: leftmost counter display
* GPIO 15, 23, 25: control buttons
* GPIO 17: beam ir sensor
