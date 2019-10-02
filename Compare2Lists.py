list1 = [2,4,6,7,8,1]
list2 = [1,2,3,4]

# set1 = set(list1)
# print(set1)
# set2 = set(list2)
# print(set2)
# set1 = set1 - set2
# list1 = list(set1)
# list1.sort()
# print(list1)
for item in list2:
    print(item)
    if item in list1:
        list1.remove(item)
print(list1)



