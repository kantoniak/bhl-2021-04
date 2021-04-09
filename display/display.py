import time
import board
import neopixel

color_green = (0, 255, 0)
color_red = (255, 0, 0)
pixels = neopixel.NeoPixel(board.D18, 1)

while (true):
    pixels.fill(color_green)
    time.sleep(1000)
    pixel.fill(color_red)
    time.sleep(1000)