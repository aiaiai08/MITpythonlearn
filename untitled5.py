# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 13:52:01 2026

@author: aisupakrit
"""
# input = N,W(sorted)
# arrange W from most to least to N-1 route
# each point is in order
# rotue can be ignored when a triangle is formed

# remain routes will start from last point N and N-2 and go on by one
# flip the order then go to 1 and 1+3 go on...

def route(N,W):
    L = []
    count = 0
    for i in range (1,N,1):
        print(i)
        if i%2 != 0:
            for c in range (1,N):
                if c+i <= N:
                    point = []
                    point.append(c)
                    point.append(c+i)
                    if point and point[-1::-1] not in L:
                        L.append(point)
                        count +=1
                else:
                    point = []
                    point.append(c)
                    point.append(c+i-N)
                    if point and point[-1::-1] not in L:
                        L.append(point)
                        count +=1
        elif i%2 == 0:
            for c in range (N,0,-1):
                if c-i > 0:
                    point = []
                    point.append(c)
                    point.append(c-i)
                    if point and point[-1::-1] not in L:
                        L.append(point)
                        count +=1
                else:
                    point = []
                    point.append(c)
                    point.append(c-i+N)
                    if point and point[-1::-1] not in L:
                        L.append(point)
                        count +=1
    print(count)
    return L


print(route(4,[1,1,1]))
