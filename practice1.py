import datetime
import time
import os
# for i in range(0,101):
#     print(i,sep='\r')
#     time.sleep(5)
# def clock():
#     while True:
#         print(datetime.datetime.now().strftime("%H:%M:%S"), end='\r')
#         time.sleep(5)
# clock()
x='python'

for i in range(1,len(x)+1):
    print(x[:i])
    time.sleep(1)
for i in range(len(x)-1,0,-1):
    print(x[:i])
    time.sleep(1)
