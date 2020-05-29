from time import time
from pygame import mixer
from datetime import datetime

def musicianloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break

def registerTime(msg):
    with open("register.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == "__main__":
    init_water= time()
    init_eyes= time()
    init_exer= time()

    watersecs=1800
    exsecs=2700
    eyessecs=900

    water_quantity=3500
    

    while True:
        if time()-init_water>watersecs:
            print("Water drinking time. Enter drank to stop")
            musicianloop("water.mp3","drank")
            registerTime("drank water at: ")
            water_quantity-=250
            print("Water quantity left: ",water_quantity)
        if time()-init_eyes>eyessecs:
            print("Eye exercise time. Enter done to stop")
            musicianloop("water.mp3","done")
            registerTime("Eye exercise done at: ")
        if time()-init_exer>exsecs:
            print("Eye exercise time. Enter exercised to stop")
            musicianloop("water.mp3","exercised")
            registerTime("Eye exercise done at: ")



