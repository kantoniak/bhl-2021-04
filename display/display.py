import time
from rpi_ws281x import *

color_green = Color(0, 255, 0)
color_red = Color(255, 0, 0)

LED_PIN        = 26
LED_BRIGHTNESS = 128 # 0 to 255
strip = Adafruit_NeoPixel(1, LED_PIN, 800000, 10, False, LED_BRIGHTNESS, 0)
strip.begin()

while (true):
    strip.setPixelColor(i, color_green)
    time.sleep(1000)
    strip.setPixelColor(i, color_red)
    time.sleep(1000)
