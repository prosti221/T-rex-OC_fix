import psutil
import os
import time
import keyboard

low_OC = 'ctrl+alt+a'
high_OC = 'ctrl+alt+b'

process_name = "t-rex"
output_file = "output.txt"

def get_process():
    for proc in psutil.process_iter():
        if process_name in proc.name():
            return psutil.Process(proc.pid)
    return 0

p = get_process()
line_offset = 34
while p != 0:
    f = open(output_file, "r")
    data = f.read().splitlines()

    if line_offset != 34:
        for line in data[line_offset:]:
            print(line)
    else:
        print("\n######################### T-REX OC FIX #########################")

    for line in data[line_offset: ]:
          if "generating DAG" in line or "R:100%" in line:
                print("\nLow OC turned on")
                keyboard.press_and_release(low_OC)
                time.sleep(2)
                print("Restarting miner and generating new DAG")
                try:
                    p.kill()
                except:
                    print("Process no longer exists, turning on low OC")
                    keyboard.press_and_release(low_OC)
                time.sleep(70)
                print("High OC turned on")
                keyboard.press_and_release(high_OC)
                print("\nMiner is currently running...")
                p = get_process()

    line_offset = len(data)
    time.sleep(25)

print("Unknown miner, setting low OC")
keyboard.press_and_release(low_OC)
