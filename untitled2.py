# def find_grades(grades,students):
#     L = []
#     for i in students:
#         L.append(grades[i])
#     return L

# d = {'Ana':'B','Matt':'C','John':'B','Katy':'A'}
# print(find_grades(d,['Matt','John']))

# def find_in_L(Ld,k):
#     i = False
#     for d in Ld:
#         if k in d:
#             i = True
#             break
#     return i
        
# d1 = {1:2, 3:4, 5:6}
# d2 = {2:4, 4:6}
# d3 = {1:1 , 3:9, 4:16, 5:25}
# print(find_in_L([d1,d2,d3],2))
# print(find_in_L([d1,d2,d3],25))

# def count_matches(d):
#     count = 0
#     for k,v in list(d.items()):
#         if k == v:
#             count+=1
#     return count

# d = {1:2, 3:4, 5:6}
# print(count_matches(d))
# d1 = {1:2, 'a':'a', 5:5}
# print(count_matches(d1))

# def in_list_of_lists(L, e):
#     if len(L) == 0:
#         return False
#     elif e in L[0]:
#         return True
#     else:
#         return in_list_of_lists(L[1:],e)
    
# test = [[1,2],[3,4],[5,6,7]]
# print(in_list_of_lists(test, 0))
# print(in_list_of_lists(test, 3))

class Animal(object):
    tag = 1
    def __init__(self,age,name):
        self.age = age
        self.name = name
    def __str__(self):
        return 'Animal'+str(self.name)+str(self.age)
def make_animals(L1 ,L2):
    L0 = []
    for i in range(0,len(L1)):
        L0.append(Animal(L1[i],L2[i]))
    return L0
        

L1 = [2,5,1]
L2 = ['blobfish','crazyant','parafox']
animals = make_animals(L1,L2)

print(animals)
for i in animals:
    print(i)
dog = Animal(1,'dg')
print(dog.tag)