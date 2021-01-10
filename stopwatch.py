import keyboard
import time

def stopwatch(buttonPressed):
    while True:
        if keyboard.is_pressed(buttonPressed):
            ticks=time.time()
            break

    return(ticks)

print("press \'s\' to start the stopwatch and \'q\' to stop it")
start=stopwatch('s')
print("stopwatch is running")
stop=stopwatch('q')
print("stopwatch is stopped")
print(stop-start)