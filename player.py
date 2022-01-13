import sys, os
import time
import itertools

import cv2

CHARS_str = ".:-=/(?%@"
#CHARS_str = "#%@AED=-:."
LEN_CH = len(CHARS_str)
VAL = (255 // len(CHARS_str))

CHARS = {255:"#",
         250:"%",
         230:"@",
         210:"A",
         180:"E",
         150:"D",
         120:"+",
         90:"=",
         60:"-",
         30:":",
         0:"."}


def load_frames(path):
    vc = cv2.VideoCapture(path)
    while True:
        status, frame = vc.read()
        if not status: exit()

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        t_clms, t_rows = os.get_terminal_size()
        frame = cv2.resize(frame, dsize=(t_clms, t_rows)).tolist()

        frame = itertools.chain(*frame)
        char_frame = ''.join(list(map(lambda x: CHARS.get(min(key for key in CHARS.keys() if key >= x)), frame)))

        sys.stdout.write(char_frame)
        sys.stdout.flush()



if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        print("please specify a file to play: [python play.py path/example.mp4]")
        exit
    load_frames(path)

