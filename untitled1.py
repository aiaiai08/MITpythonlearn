# # # def same_chars(s1,s2):
# # #     s1 = str(s1)
# # #     s2 = str(s2)
# # #     count1 = 0
# # #     count2 = 0
# # #     for i in range(len(s1)):
# # #         for a in range(len(s2)):
# # #             if s2[a] == s1[i]:
# # #                 count1 +=1
# # #                 break
# # #     for i in range(len(s2)):
# # #         for a in range(len(s1)):
# # #             if s1[a] == s2[i]:
# # #                 count2 +=1
# # #                 break
# # #     return count1 == len(s1) and count2 == len(s2)

# # # print(same_chars("abc", "cab"))     # prints True
# # # print(same_chars("abccc", "caaab")) # prints True
# # # print(same_chars("abcd", "cabaa"))  # prints False
# # # print(same_chars("abcabc", "cabz")) # prints False
# # # print(same_chars("abcccabbb", "caaabccccccc")) # prints True

        
# # # def dot_product(tA,tB):
# # # tA = tuple(tA)
# # #     tB = tuple(tB)
# # #     a = len(tA)
# # #     x = 0
# # #     for i in range(len(tA)):
# # #         for b in range(len(tB)):
# # #             if i == b:
# # #                 x += tA[i]*tB[b]
# # #     return (a,x)
# # # tA = (1, 2, 3)
# # # tB = (4, 5, 6)   
# # # print(dot_product(tA, tB)) # prints (3,32)

# # # def remove_elem(L ,e):
# # #     newlist = []# #     
# # #     for i in L:
# # #         if i == e:
# # #             pass
# # #         else:
# # #             newlist.append(i)
# # #     return newlist
# # # x = [1,2,1,32,2,1,2]
# # # print(remove_elem(x,1))

def sort_words(sen):
    a = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    sen1 = sen
    L = sen1.split(' ')
    print(L)
    print(L[3])
    sen2 = []
    d1 = []
    for i in L:
        if i not in d1:
            d1.append[i]
    for i in a:
        for b in L:
            if i == b[0]:
                sen2.append(b)
    sen3 = ' '.join(sen2)
    return sen3
    
print(sort_words('Hello world I Am Aa'))


# # Aba Aab
# if (L[0])[0] == (L[1])[0]: #first position 0
    
# for c in range(maxletter):
#     for d in L:
#         if (L[d])[c] not in Y:
#             Y.append((L[d])[c])
#         else:
#               found = True
#               break
#     if found:
#         break
        
#     #1 check all member
#     #2 detect equal 
#     #3 check position 2 of equal
#     #4 detect equal if not make new order
        
# #check equal member
# # X = [1,1,2]
# # Y = []
# # for i in X:
# #     if i not in Y:
# #         Y.append(i)
# # print(Y)

    
    
    
        
