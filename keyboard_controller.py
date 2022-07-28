import win32api
import win32con
import time
import ctypes

left_arrow = 0x61
up_arrow = 0x65
right_arrow = 0x63
down_arrow = 0x62


def character2hex(character):
    return 0x41 + ord(character)-ord('a')


def key_down_up(num, hold_time=0.2):
    map_virtual_key = ctypes.windll.user32.MapVirtualKeyA
    time.sleep(0.4)
    win32api.keybd_event(num, map_virtual_key(num, 0), 0, 0)
    time.sleep(hold_time)
    win32api.keybd_event(num, map_virtual_key(num, 0), win32con.KEYEVENTF_KEYUP, 0)


def move(direction, m_time):
    if direction == 'l':
        key_down_up(character2hex('j'), m_time)
    elif direction == 'r':
        key_down_up(character2hex('l'), m_time)
    elif direction == 'u':
        key_down_up(character2hex('i'), m_time)
    else:
        key_down_up(character2hex('k'), m_time)


def skill(chara):
    key_down_up(character2hex(chara))
