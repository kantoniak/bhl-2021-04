import time
from neopixel import *

color_green = Color(0, 255, 0)
color_red = Color(255, 0, 0)

LED_PIN        = 18
LED_BRIGHTNESS = 128 # 0 to 255
strip = Adafruit_NeoPixel(1, LED_PIN, 800000, 5, False, LED_BRIGHTNESS)
strip.begin()

while (true):
    strip.setPixelColor(i, color_green)
    strip.show()
    time.sleep(1000)
    strip.setPixelColor(i, color_red)
    strip.show()
    time.sleep(1000)
