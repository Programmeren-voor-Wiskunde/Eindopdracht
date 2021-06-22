# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 15:00:10 2021

@author: Jelger
"""
import copy
def minimale_afstand(s):
    t=copy.copy(s)
    som=0   
    h=sum(s)/len(s)
    for i in s:
       som+=abs(h-i)
    return som
        
print(minimale_afstand([80, 36, 41, 28]))