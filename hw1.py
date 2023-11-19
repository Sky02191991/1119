from threading import Thread
import  time


def th1_run():
    a = []
    for i in range(8):
        a.append(i+1)
        time.sleep(0.5)
    print(a)

th1 = Thread(target=th1_run)
th1.start()

b = []
for j in range(3):
    b.append(j+1)
    time.sleep(0.5)


print(b)
th1.join()
print("finish all")


