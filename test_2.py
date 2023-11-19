from threading import Thread
import  time
def func(start,listnumber,out):
    global total_list
    total_list=[]  
    for i in range(listnumber):
        total_list.append(start)
        start=start+2
    print(total_list[2])
    lastnumber=total_list[2]
    out.append(lastnumber)
out = []
go=Thread(target=func,args=(2,3,out,))
go.start()
print(f"out list last number: {total_list[2]}")
print(f"out list {out[0]}")
