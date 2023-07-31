# file_capital=open("capital.txt","r")
# print(file_capital.readable()) #True
# file_capital.close()
##############################################
# file_capital=open("capital.txt","w")
# print(file_capital.readable()) # false
# file_capital.close()
#############################################
# file_capital=open("capital.txt","r")
# print(file_capital.readline())#read one line
# # print(file_capital.readlines())#read all of lines but in list we can creat a object
# capital=file_capital.readlines()
# for x in capital:
#     print(x)
#
# file_capital.close()
############################################
# file_capital=open("capital.txt","a")
# file_capital.write("\n they are capital of the world")
#
# file_capital.close()
# ###########################################
# file_capital=open("capital.txt","r")
# print(file_capital.readline())#read one line
# # print(file_capital.readlines())#read all of lines but in list we can creat a object
# capital=file_capital.readlines()
# for x in capital:
#     print(x)
#
# file_capital.close()
##########################################
# empty=open("empty.txt","w")
# empty.write("\n this is empty file")
#
# empty.close()
#########################################
empty=open("empty.txt","r+")
empty.write("\n this not empty")
empties=empty.readlines()

for x in empties:
    print(x)

empty.close()