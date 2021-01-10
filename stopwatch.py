import keyboard
import time

def stopwatch(buttonPressed):
    print("press \'s\' to start the stopwatch and \'q\' to stop it")
    while True:
        if keyboard.is_pressed(buttonPressed):
            ticks=time.time()
            break

    return(ticks)

start=stopwatch('s')
print("stopwatch is running")
stop=stopwatch('q')
print("stopwatch is stopped")
print(stop-start)