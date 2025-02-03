import threading
import time

print("Main Thread Started")

def first_task():
    print("Sub task1 started ")
    time.sleep(2)
    print("Sub task1 completed")
    
def second_task():
    print("Sub task2 started ")
    time.sleep(3)
    print("Sub task2 completed")
    
def display():
    for i in range(1,5):
        if i%2==0:
            print ("even")
            time.sleep(2)
            
    
thread1=threading.Thread(target=first_task)
thread2=threading.Thread(target=second_task)
thread3=threading.Thread(target=display)

thread1.start()
thread2.start()
thread3.start()
print("Main thread completion is completed")