#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
    a =[1,2,3,4]
    b  = [2,3,4,5,7]
    i=0
    k=0
    mc  = a.length+b.length / 2 
    for ia in range(a):
        for ib in range(b):
            if(i+k)>mc:
                if(a[i]>b[k]):
                    print(a[i])
                else:
                    print(b[k])
                break
            if(a[i]>b[k])&k<b.length:
                k+=1 
            else:
                if i<a.length :
                    i+=1


