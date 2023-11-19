import threading ,time
a =[]
b = []
#a_in= int(input("請輸入A陣列的長度:"))
b_in= int(input("請輸入B陣列的長度:"))
#a_in=a_in+1
def thread1(a_in):
    print(a_in)
    a_in=a_in+1
    for i in range(a_in) :
        time.sleep(0.5)
        if i == 0:
            pass
        else:
            a.append(i)
            print(f"a={a}")
astart = threading.Thread(target = thread1,args=(3,))
astart.start()
b_in=b_in+1
for i  in range(b_in)  :
    time.sleep(0.5)
    if i == 0:
        pass
    else:
        b.append(i)
        print(f"b={b}")
print("================")
#int(a)
#print(b)

astart.join()
c=a+b
print(f"end all show == {c}")


