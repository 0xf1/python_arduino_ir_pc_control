from time import sleep

import serial

from kbd import PressKey, ReleaseKey

VK_MENU = 0x12
alt_pressed = False
control_pressed = False

ser = serial.Serial(port='COM3', baudrate=115200, timeout=5)
print("connected to: " + ser.portstr)


def win_tab(*args):
    """Press Windows+Tab"""
    vk_win = 0X5B
    vk_tab = 0x09
    PressKey(vk_win)
    PressKey(vk_tab)
    ReleaseKey(vk_tab)
    sleep(.2)
    ReleaseKey(vk_win)


def alt_press(*args):
    global alt_pressed
    alt_pressed = True


def control_press(*args):
    global control_pressed
    control_pressed = True


def power_off(*args):
    import os
    os.system('shutdown -s -t 0')


def push(key_code):
    global alt_pressed
    global control_pressed

    if alt_pressed:
        PressKey(VK_MENU)  # Alt

    if control_pressed:
        PressKey(0xA2)  # left control

    PressKey(key_code)
    sleep(.2)
    ReleaseKey(key_code)

    if alt_pressed:
        sleep(.2)
        ReleaseKey(VK_MENU)  # Alt~
        alt_pressed = False

    if control_pressed:
        sleep(.2)
        ReleaseKey(0xA2)  # left control
        control_pressed = False


# SAMSUNG keys
keys = {"2256078599": ["smart tv - windows+tab", win_tab, ""],
        "2673870599": ["up", push, 0x26],
        "2657158919": ["down", push, 0x28],
        "4244768519": ["power off - shutdown", power_off, ""],

        "2590312199": ["left", push, 0x25],
        "2640447239": ["right", push, 0x27],
        "2540177159": ["enter", push, 0x0D],
        "2807564039": ["return - space", push, 0x20],
        "3526166279": ["exit - esc", push, 0x1B],

        "2473330439": ["A - alt", alt_press, ""],
        "3927246599": ["C - left control", control_press, ""],
        "3910534919": ["D - F key", push, 0x46],  # useful for youtube to switch fullscreen mode
        "3074950919": [">> btn - tab", push, 0x09],

        "3977381639": ["channel up - page up", push, 0x21],
        "4010804999": ["channel down - page down", push, 0x22],

        "4094363399": ["volume up", push, 0xAE],
        "4161210119": ["volume down", push, 0xAF],
        "4027516679": ["mute", push, 0xAD],

        "4211345159": ["1 - F1", push, 0x70],
        "4194633479": ["2 - F2", push, 0x71],
        "4177921799": ["3 - F3", push, 0x72],
        "4144498439": ["4 - F4", push, 0x73],
        "4127786759": ["5 - F5", push, 0x74],
        "4111075079": ["6 - F6", push, 0x75],
        "4077651719": ["7 - F7", push, 0x76],
        "4060940039": ["8 - F8", push, 0x77],
        "4044228359": ["9 - F9", push, 0x78],
        "3994093319": ["10 - F10", push, 0x79],
        "3960669959": ["PRE-CH - NUMLOCK", push, 0x90],
        "3843688199": ["MENU - left win key", push, 0x5B],
        "2957969159": ["GUIDE - apps", push, 0x5D],

        }

while True:
    data = ser.readline()
    data = data.strip().decode("utf-8")

    if data == "":
        sleep(.1)
        continue

    print(data)
    k = keys.get(data)
    if k is not None:
        print(k[0])
        k[1](k[2])

    sleep(.1)

ser.close()
