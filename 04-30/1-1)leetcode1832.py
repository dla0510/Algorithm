# -*- coding: utf-8 -*-
"""
Created on Fri May  7 11:27:09 2021

@author: dla05
"""
def checkIfPangram(sentence):
    result = True
    arr = []
    for i in range(0,26):
        arr.append(False)
    
    for i in range(len(sentence)):
        arr[ord(sentence[i])-97]=True
        
    for i in arr:
        if i==False:
            result=False
    
    return result

sentence="thequickbrownfoxjumpsoverthelazydog"
