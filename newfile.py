# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
# nums=[2, 2, 3, 3, 3]
# newList=[]
# for i in nums:
#     if i not in newList:
#         newList.append(i)
# print(newList)
list1=[1,2,3,4,5]
list2=[7,8,9,10,12,13,14]
newlist=[]
i=0
j=0
len1=len(list1)
len2=len(list2)
while i<len1 and j<len2:
    if list1[i]<list2[j]:
        newlist.append(list1[i])
        i+=1
    else:
        newlist.append(list2[j])
        j+=1
while i<len1:
    newlist.append(list1[i])
    i+=1
while j<len2:
    newlist.append(list2[j])
    j+=1
print(newlist)