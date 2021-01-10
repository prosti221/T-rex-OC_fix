import psutil
import os
import time
import keyboard

low_OC = 'ctrl+alt+a'
high_OC = 'ctrl+alt+b'

process_name = "t-rex"
output_file = "C:/Users/Faisal/AppData/Local/Programs/NiceHash Miner/miner_plugins/03f80500-94ec-11ea-a64d-17be303ea466/bins/15.7/output.txt"
pid = ""

def get_process():
    for proc in psutil.process_iter():
        if process_name in proc.name():
            pid = proc.pid
            p = psutil.Process(pid)
            return p
    return 0

p = get_process()
cutoff = 34
while p != 0:
    f = open(output_file, "r")
    data = f.read().splitlines()

    if cutoff != 34:
        for line in data[cutoff:]:
            print(line)
    else:
        print("\n######################### T-REX OC MANAGER #########################")

    for line in data[cutoff: ]:
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

    cutoff = len(data)
    time.sleep(25)

print("Unknown miner, setting low OC")
keyboard.press_and_release(low_OC)
time.sleep(5)
keyboard.press_and_release(low_OC)