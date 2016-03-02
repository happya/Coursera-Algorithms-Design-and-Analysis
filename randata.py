###Filename: randata.py
import random


def getrandata(num):
    a=[]
    i=0
    while i<num:
        a.append(random.randint(0,1000))
        i+=1
    return a