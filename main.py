print("Hello, ESP32-S3!")
from machine import Pin, SPI
import time
import neopixel

rclk = Pin(7, Pin.OUT)

np = neopixel.NeoPixel(Pin(21, Pin.OUT), 1)

spi = SPI(2, baudrate=10000000, sck=Pin(8), mosi=Pin(9))
# .  A
# F   B
#   G
# E   C
#   D
#      .
# BAFG.CDE

segments = {
    0: int("00000000", 2),
    1: int("11110101", 2),  # A
    2: int("11010011", 2),  # 2
    3: int("11010110", 2),  # 3
    4: int("10110100", 2),  # 4
    5: int("01110110", 2),  # 5
    6: int("01110111", 2),  # 6
    7: int("11000100", 2),  # 7
    8: int("11110111", 2),  # 8
    9: int("11110110", 2),  # 9
    10: int("11101111", 2),  # 0.
    11: int("11111101", 2),  # A.
}
segments2 = {
    " ": 0b00000000,
    "0": 0b11100111,
    "1": 0b10000100,
    "2": 0b11010011,
    "3": 0b11010110,
    "4": 0b10110100,
    "5": 0b01110110,
    "6": 0b01110111,
    "7": 0b11000100,
    "8": 0b11110111,
    "9": 0b11110110,
    "0.": 0b11101111,
    "1.": 0b10001100,
    "2.": 0b11011011,
    "3.": 0b11011110,
    "4.": 0b10111100,
    "5.": 0b01111110,
    "6.": 0b01111111,
    "7.": 0b11001100,
    "8.": 0b11111111,
    "9.": 0b11111110,
    "A": 0b11110101,
    "B": 0b00110111,
    "C": 0b01100011,
    "D": 0b10010111,
    "E": 0b01110011,
    "F": 0b01110001,
    "H": 0b10110101,
    "I": 0b00100001,
    "J": 0b10000110,
    "L": 0b00100011,
    "N": 0b00010101,
    "T": 0b00110011,
}

np[0] = (50, 0, 0)
np.write()
time.sleep(0.3)

np[0] = (50, 25, 0)
np.write()
time.sleep(0.3)

np[0] = (50, 50, 0)
np.write()
time.sleep(0.3)

np[0] = (25, 50, 0)
np.write()
time.sleep(0.3)

np[0] = (0, 50, 0)
np.write()
time.sleep(0.3)

np[0] = (0, 50, 25)
np.write()
time.sleep(0.3)

np[0] = (0, 50, 50)
np.write()
time.sleep(0.3)

np[0] = (0, 25, 50)
np.write()
time.sleep(0.3)

np[0] = (0, 0, 50)
np.write()
time.sleep(0.3)

np[0] = (25, 0, 50)
np.write()
time.sleep(0.3)

np[0] = (50, 0, 50)
np.write()
time.sleep(0.3)

np[0] = (50, 0, 25)
np.write()
time.sleep(0.3)

np[0] = (50, 25, 25)
np.write()
time.sleep(0.3)

np[0] = (25, 50, 25)
np.write()
time.sleep(0.3)

np[0] = (50, 50, 50)
np.write()
time.sleep(0.3)

np[0] = (0, 0, 0)
np.write()


def seg_draw(*args):
    digits = list(args)[:5] + [" "] * (5 - len(args))
    data = bytes([segments2.get(d, 0x00) for d in digits][::-1])
    spi.write(data)

    # latch
    rclk.value(1)
    rclk.value(0)


def draw2(*args):
    digits = list(args)[:5] + [" "] * (5 - len(args))
    data = bytes([segments.get(d, 0x00) for d in digits][::-1])
    spi.write(data)

    # latch
    rclk.value(1)
    rclk.value(0)


# def seg()


for key in sorted(segments.keys()):
    draw2(key, key, key, key, key)
    time.sleep(0.2)

for key in sorted(segments2.keys()):
    seg_draw(key, key, key, key, key)
    time.sleep(0.1)

# time.sleep(0.8)

seg_draw("I", "N", "I", "T")

time.sleep(2)
while True:
    seg_draw("C", " ", " ", " ", "B")
    time.sleep(0.8)
    seg_draw(" ", " ", " ", "B", "L")
    time.sleep(0.8)
    seg_draw(" ", " ", "B", "L", "A")
    time.sleep(0.8)
    seg_draw(" ", "B", "L", "A", "C")
    time.sleep(0.8)
    seg_draw("B", "L", "A", "C", " ")
    time.sleep(0.8)
    seg_draw("L", "A", "C", " ", "J")
    time.sleep(0.8)
    seg_draw("A", "C", " ", "J", "A")
    time.sleep(0.8)
    seg_draw("C", " ", "J", "A", "C")
    time.sleep(0.8)
    seg_draw(" ", "J", "A", "C", " ")
    time.sleep(0.8)
    seg_draw("J", "A", "C", " ", " ")
    time.sleep(0.8)
    seg_draw("A", "C", " ", " ", " ")
    time.sleep(0.8)









