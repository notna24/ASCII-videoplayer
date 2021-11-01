import sys, os
import time

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

CC = [255, 250, 230, 210, 180, 150, 120, 90, 60, 30, 0]
'''
while True:
    clms, lines = os.get_terminal_size()
    #time.sleep(0.1)
    sys.stdout.write(str(clms) + " " + str(lines) + "\n")
    sys.stdout.flush()
'''
def load_frames(path):
    vc = cv2.VideoCapture(path)
    while True:
        status, frame = vc.read()

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        t_clms, t_rows = os.get_terminal_size()
        frame = cv2.resize(frame, dsize=(t_clms, t_rows))
        clms, rows = frame.shape
        #cv2.imshow("title", frame)
        #cv2.waitKey(1)
  

        #print(frame[0, 0])

        #print(rows, clms)
        #print(t_rows, t_clms)

        char_frame = ""

        for r in range(t_rows):
            char_row = ""
            for c in range(t_clms):
                gs_val = frame[r, c]
                #val = (gs_val // (255 // len(CHARS_str))) % len(CHARS_str)
                val = (gs_val // VAL) % LEN_CH
                char_row += CHARS_str[val]
                '''
                for c in CC:
                    if gs_val >= c :
                        char_row += CHARS.get(c)
                        break
                '''     
            char_frame += (char_row)
        sys.stdout.write(char_frame)
        sys.stdout.flush()
        #os.system("cls")
                #print(frame[r, c])
    

if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        print("please specify a file to play: [python play.py path/example.mp4]")
        exit
    load_frames(path)

