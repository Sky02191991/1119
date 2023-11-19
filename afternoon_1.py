from threading import Thread
import  time
#call by vaclue
def add_1 (b):
    b+=1
    a=3
    add_1(a)
#start1=Thread(target=add_1,args=(3,))
#start1.start()
a=3
add_1(a)