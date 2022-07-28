import time
from rulebased import run_berserker
from keyboard_controller import key_down_up


class State:
    def __init__(self):
        self.name = 'dungeon'
        self.fatigue = 188


if __name__ == "__main__":
    # print(ord('q')-ord('a'))
    time.sleep(2)

    my_state = State()
    while my_state.fatigue > 0:
        run_berserker()
        my_state.fatigue -= 7
