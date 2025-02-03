import threading
import time
def daemon_task():
    while True:
        print("daemon thread running ")
        time.sleep(1)
    
thread=threading.Thread(target=daemon_task,daemon=True)
thread.start()

time.sleep(5)
print("Main thread exiting...")