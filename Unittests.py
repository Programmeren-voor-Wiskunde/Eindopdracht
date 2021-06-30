# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 16:47:04 2021

@author: Jelger
"""

"""Unit Tests: worden alleen geprint indien returnvalue onjuist is""" 
#is_set, expected: True 
kaart1, kaart2, kaart3=Kaart(0,1,2,1), Kaart(0,2,3,3), Kaart(0,3,1,4)
kaart4, kaart5, kaart6=Kaart(1,0,2,1), Kaart(2,0,3,3), Kaart(3,0,1,4)
kaart7, kaart8, kaart9=Kaart(1,2,0,1), Kaart(2,3,0,3), Kaart(3,1,0,4)
kaart10, kaart11, kaart12=Kaart(1,2,1,0), Kaart(2,3,3,0), Kaart(3,1,4,0)

if kaart1.is_set(kaart2,kaart3)==False:
    print("Unit test 1: "+str(kaart1)+","+str(kaart2)+","+str(kaart3)+" "+ "Expected: True, return Falue:"+str(kaart1.is_set(kaart2,kaart3)))
if kaart4.is_set(kaart5,kaart6)==False:
    print("Unit test 2: "+str(kaart4)+","+str(kaart5)+","+str(kaart6)+" "+ "Expected: True, return Falue:"+str(kaart4.is_set(kaart5,kaart6)))
if kaart7.is_set(kaart8,kaart9)==False:
    print("Unit test 3: "+str(kaart7)+","+str(kaart8)+","+str(kaart9)+" "+ "Expected: True, return Falue:"+str(kaart7.is_set(kaart8,kaart9)))
if kaart10.is_set(kaart11,kaart12)==False:
    print("Unit test 4: "+str(kaart10)+","+str(kaart11)+","+str(kaart12)+" "+ "Expected: True, return Falue:"+str(kaart10.is_set(kaart11,kaart12)))      

#is_set, expected: False 
kaart13, kaart14, kaart15=Kaart(1,1,2,1), Kaart(0,2,2,3), Kaart(0,1,1,3)
kaart16, kaart17, kaart18=Kaart(2,1,3,3), Kaart(2,1,1,2), Kaart(1,2,1,2)
kaart19, kaart20, kaart21=Kaart(3,2,1,1), Kaart(2,3,3,3), Kaart(3,3,1,1)

if kaart13.is_set(kaart14,kaart15)==True:
    print("Unit test: "+str(kaart13)+","+str(kaart14)+","+str(kaart15)+" "+ "Expected: False, return Falue:"+str(kaart13.is_set(kaart14,kaart15)))
if kaart16.is_set(kaart17,kaart18)==True:
    print("Unit test: "+str(kaart16)+","+str(kaart17)+","+str(kaart18)+" "+ "Expected: False, return Falue:"+str(kaart16.is_set(kaart17,kaart18)))
if kaart19.is_set(kaart20,kaart21)==True:
    print("Unit test: "+str(kaart19)+","+str(kaart20)+","+str(kaart21)+" "+ "Expected: False, return Falue:"+str(kaart19.is_set(kaart20,kaart21)))
