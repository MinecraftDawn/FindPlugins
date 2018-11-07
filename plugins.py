# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 13:38:29 2018

@author: Eric
"""

f = open("snow.txt","r+")
fs = f.readline()

sa = str(fs).split(", ")

sss = []
for i in sa:
    if ":" in i:
        sss.append(i[1:i.find(":")])
        
removed = list(set(sss))
for i in removed:
    print(i)
removed.sort()

fo = open("SnowPlugin.txt","a")

for i in removed:
    fo.write(i + "\n")
    
fo.close()
f.close()