import threading ,time

global j
def sleep5():
    global j
    for j in range(10):
        time.sleep(0.5)  
        print(f"back ground {j} in back count")
              

backcount=threading.Thread(target=sleep5)
backcount.start()

for i in range(10):
    time.sleep(1)
    print(f"now i is  {i}")
    print(j)
    if j == 2 or 1 :
        break
    
backcount.join()
print("end all")