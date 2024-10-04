# Importing the threading module
import threading 
deposit = 100

def add_profit(): 
    global deposit
    for i in range(1000000):
        deposit = deposit + 10

def pay_bill(): 
    global deposit
    for i in range(1000000):
        deposit = deposit - 10

thread1 = threading.Thread(target = add_profit, args = ())
thread2 = threading.Thread(target = pay_bill, args = ())

thread1.start() 
thread2.start()

thread1.join()
thread2.join()

print(deposit)