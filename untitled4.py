# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 15:08:16 2026

@author: aisupakrit
"""
# 2 object can't have same properties and location

# Cube = [list1 , list2 , ... ,list8]

# position 1 = Front Up Right
# 2 = ful
# 3 = fdl
# 4 = fdr
# 5 = bur
# 6 = bul
# 7 = bdl
# 8 = bdr
# c = [x,y,z]
# 
r = '🟥'
b = '🟦'
g = '🟩'
o = '🟧'
w = '⬜'
y = '🟨'
class Cube(object):
    def __init__(self,c1,c2,c3,c4,c5,c6,c7,c8):
        # c1 = list(c1)
        # c2 = list(c2)
        # c3 = list(c3)
        # c4 = list(c4)
        # c5 = list(c5)
        # c6 = list(c6)
        # c7 = list(c7)
        # c8 = list(c8)
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4
        self.c5 = c5
        self.c6 = c6
        self.c7 = c7
        self.c8 = c8
           
    def R(self):
        
        self.c1,self.c4,self.c5,self.c8 = self.c4,self.c8,self.c1,self.c5
        (self.c1)[1],(self.c1)[2] = (self.c1)[2],(self.c1)[1]
        (self.c4)[1],(self.c4)[2] = (self.c4)[2],(self.c4)[1]
        (self.c5)[1],(self.c5)[2] = (self.c5)[2],(self.c5)[1]
        (self.c8)[1],(self.c8)[2] = (self.c8)[2],(self.c8)[1]
        
        return self
    def Rprime(self):
        ((self.R()).R()).R()
    def z(self):
        self.c1,self.c2,self.c3,self.c4,self.c5,self.c6,self.c7,self.c8 = self.c5,self.c1,self.c4,self.c8,self.c6,self.c2,self.c3,self.c7
        (self.c1)[1],(self.c1)[0] = (self.c1)[0],(self.c1)[1]
        (self.c2)[1],(self.c2)[0] = (self.c2)[0],(self.c2)[1]
        (self.c3)[1],(self.c3)[0] = (self.c3)[0],(self.c3)[1]
        (self.c4)[1],(self.c4)[0] = (self.c4)[0],(self.c4)[1]
        (self.c5)[1],(self.c5)[0] = (self.c5)[0],(self.c5)[1]
        (self.c6)[1],(self.c6)[0] = (self.c6)[0],(self.c6)[1]
        (self.c7)[1],(self.c7)[0] = (self.c7)[0],(self.c7)[1]
        (self.c8)[1],(self.c8)[0] = (self.c8)[0],(self.c8)[1]    
        return self
    def zprime(self):
        self.z()
        self.z()
        self.z()
        return self
    def L(self):
        self.z()
        self.z()
        self.R()
        self.z()
        self.z()
        return self
    def F(self):
        self.z()
        self.L()
        self.zprime()
        return self
    def U(self):
        self.z()
        ((self.R()).R()).R()
        self.L()
        self.F()
        self.R()
        ((self.L()).L()).L()
        self.zprime()
    def __str__(self):
        return str(self.c1)+str(self.c2)+str(self.c3)+str(self.c4)+str(self.c5)+str(self.c6)+str(self.c7)+str(self.c8)
    
    def moveset(self,L):
        for i in L:
            if i == 'R':
                self.R()
            elif i == 'L':
                self.L()
            elif i == 'U':
                self.U()
            elif i == 'Rprime':
                self.Rprime()
            else:
                pass
        return self
    def visual(self):
        print(6*' '+str((self.c6)[2])+str((self.c5)[2]))
        print(6*' '+str((self.c2)[2])+str((self.c1)[2]))
        print(str((self.c6)[0])+str((self.c2)[0])+' '+str((self.c2)[1])+str((self.c1)[1])+' '+str((self.c1)[0])+str((self.c5)[0])+' '+str((self.c5)[1])+str((self.c6)[1]))
        print(str((self.c7)[0])+str((self.c3)[0])+' '+str((self.c3)[1])+str((self.c4)[1])+' '+str((self.c4)[0])+str((self.c8)[0])+' '+str((self.c8)[1])+str((self.c7)[1]))
        print(6*' '+str((self.c3)[2])+str((self.c4)[2]))
        print(6*' '+str((self.c7)[2])+str((self.c8)[2]))
C = Cube([r,g,w],[o,g,w],[o,g,y],[r,g,y],[r,b,w],[o,b,w],[o,b,y],[r,b,y])
moves = 'RURRRURUURRR'

C.moveset((list(moves)))

moves2 = 'RUURRRUUURUUURRR'
C.moveset((list(moves2)))

print(C)


C.visual()