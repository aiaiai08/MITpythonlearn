# x = float(input(" "))
# p = 0
# while (3**p*x)%1 != 0:
#     p +=1
# z = int((3**p*x))
# base2 = ""

# while z > 0:
#     a = str(z%3)
#     print(a)
#     base2 += str(a)
#     z = z//3
# base2R = (base2[::-1])
# base2R = int(base2R)
# print(str(base2R))
# base2R = base2R*10**(-p)
# print(str(base2R))


# import numpy as np

# array = np.array([['a','b'],['c','d']])

# array1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# array2 = np.array([[1,2,3]
#                    ,[4,5,6]
#                    ,[7,8,9]])

# print(array1*array2)


# def merge(L):
#     if len(L) == 1:
#         return L
#     else:
#         L1 = L[0:len(L)/2+1]
#         L2 = :[len(L)/2+1:len(L)+1]
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
        i = 0
        sum = 0
        L = []
        for i, j in zip(self.l1,self.l2):
            sum+=((10**i)*(i+j))
            i+=1
        for num in range(len(sum) - 1, -1, -1):
            L.append(sum[num])
        return L
        
Ex = Solution([2,4,3],[5,6,4])
print(Ex)