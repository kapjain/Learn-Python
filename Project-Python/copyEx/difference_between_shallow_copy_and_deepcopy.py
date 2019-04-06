"""
This create problems for only mutable object like list dictionary, set

Shallow copy take care of object at object level but Deep copy take care of reference of references
shallow copy is faster because it does copy the whole structure of each references

"""
l1 = [1,2,3,4,5]
l2 = l1 # reference variable
l1.append(6)
print(l1) #[1, 2, 3, 4, 5, 6]
print(l2) #[1, 2, 3, 4, 5, 6]


l = [1,2,[3,4]]

import copy
l1 = copy.copy(l) # shallow copy
l2 = copy.deepcopy(l) # deepcopy

l[2][1] = 'Kapil'
print(l) # [1, 2, [3, 'Kapil']]
print(l1) #[1, 2, [3, 'Kapil']]
print(l2) #[1, 2, [3, 4]]