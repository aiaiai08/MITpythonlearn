# # -*- coding: utf-8 -*-
# """
# Created on Fri Mar 27 17:12:20 2026

# @author: aisupakrit
# """
# from dateutil import parser
# class Workout(object):
#     calph = 200
#     def __init__(self,start,end,calories=None):
#        self.start = parser.parse(start)
#        self.end = parser.parse(end)
#        if calories == None:
#            self.calories = Workout.calph*(self.end-self.start).total_seconds()/3600
#        else:
#            self.calories = calories
#     def get_cal(self):
#         self.calories
#         return self.calories  
           
# w_one = Workout('1/1/2021 3:30PM','1/1/2021 4:00PM')
# w_two = Workout('1/1/2021 3:35PM','1/1/2021 4:00PM',300)

# print(w_one.get_cal())
# print(w_two.get_cal())

# def all_true(n,Lf):
#     for f in Lf:
#         if Lf(f) == False:
#             return False
#             break
#         else return True

# def remove_and_sort(Lin,k):
#     del(Lin[0:k])
#     Lin.sort()
    
# L = [1,6,3]
# k = 1
# remove_and_sort(L,k)
# print(L)

# def count_sqrts(num_list):
#     L = []
#     count = 0
#     for i in num_list:
#         L.append(i**2)
#     for a in L:
#         if a in num_list:
#             count +=1
#     return count


# print(count_sqrts([3,4,2,1,9,25]))

# def sum_str_lengths(L):
#     count = 0
#     if len(L) == 0:
#         return 0
#     else:
#         if type(L[0]) == str:
#             return len(L[0]) + sum_str_lengths(L[1:])
#         elif type(L[0]) == list:
#             return sum_str_lengths(L[0]) + sum_str_lengths(L[1:])
#         else:
#             raise ValueError
        



# def sum_str_lengths(L):
#     total = 0
#     for i in L:
#         if type(i) == str:
#             total += len(i)
#         elif type(i) == list:
#             for e in i:
#                 if type(e) == str:
#                     total += len(e)
#                 else:
#                     raise ValueError
#         else:
#             raise ValueError
#     return total

# print(sum_str_lengths([12, ["e", "fg"]]))      # raises ValueError
# print(sum_str_lengths(["abcd", [3, "fg"]]))    # raises ValueError
# print(sum_str_lengths(["abcd", ["e", "fg"]]))  # prints 7

# def bubble_sort(L):
#     swapt = True
#     while swapt:
#         swapt = False
#         for i in range (1,len(L)):
#             if L[i] < L[i-1]:
#                 L[i],L[i-1] = L[i-1],L[i]
#                 swapt = True
#     return(L)
    
# print(bubble_sort([1,6,2,0,5,3,6,1]))

# def keys_with_value(aDict, target):
#     L = []
#     for e in aDict:
#         if aDict[e] == target:
#             L.append(e)
#     return L

# aDict = {1:2, 2:4, 5:2}
# target = 2   
# print(keys_with_value(aDict, target)) # prints the list [1,5]
            
# def all_positive(d):
#     L = []
#     for e in d:
#         sum = 0
#         for i in d[e]:
#             sum +=i
#             print(sum)
#         if sum > 0:
#             L.append(e)
#     L.sort()
#     return L

# d = {5:[2,-4], 2:[1,2,3], 1:[2]}
# print(all_positive(d))   # prints the list [1, 2]         

# def recur_power(base, exp):
#     if exp == 0:
#         return 1
#     else:  
#         return base*recur_power(base, exp-1)
        
# print(recur_power(2,5))  # prints 32
                
def flatten(L):
    Lnew = []
    if type(L[0]) != list:
        Lnew.append (L[0])
    else:
        Lnew.append(flatten(L[0]))
    return Lnew

L = [[1,4,[6],2],[[[3]],2],4,5]
print(flatten(L)) # prints the list [1,4,6,2,3,2,4,5]