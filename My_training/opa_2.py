# my_list = [9,1,5,9,4,2,7,2,9,5,3] occurences = [] for item in my_list :count = 0 for x in
# my_list : if x == item:count +=1 occurences.append(count) duplicates=set() index = 0 while index<
# len(my_list) : if occurences[index] !=1: duplicates.add(my_list[index]) index +=1 print(duplicates)

# my_list = [9,1,5,9,4,2,7,9,5,3]
# """создать множество из повторяющихся элементов списка """
# occurences = []
# for item in my_list:
#     count = 0
#     for x in my_list:
#         if x==item:
#             count+=1
#             occurences.append(count)
# print(occurences)
# duplicates=set()
# index=0
# while index<len(my_list):
#     if occurences[index] !=1:
#         duplicates.add(my_list[index])
#     index+=1
# print(duplicates)


n=9 def fact(n): if (n==1 or n==0): return 1 else: return n*fact(n-1)
print('The factorial of ', n ,'is:' ,fact(n))




n = 9
def fact(n):
    if (n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)

print('The factorial of ', n ,'is:' ,fact(n))

