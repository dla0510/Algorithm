# -*- coding: utf-8 -*-
"""
Created on Thu May 20 23:57:36 2021

@author: dla05
"""

def main():
    s=input()
    bomb=input()
    l=[]
    
    for i in s:
        l.append(i)
        if l[-1]==bomb[-1] and ''.join(l[-len(bomb):])==bomb:
            del l[-len(bomb):]
            
    ans = ''.join(l)
    
    if ans=='':
        print("FRULA")
    else:
        print(ans)

if __name__=='__main__':
    main()