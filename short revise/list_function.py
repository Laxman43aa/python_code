#functions of list in Python
# 1. append()
lst=[1,2,3,4]
print(lst)
lst.append(5)
print(lst) # [1, 2, 3, 4, 5]

# 2. extend()
lst=[1,2,]
print(lst)
lst.extend([3,4])
print(lst) # [1, 2, 3, 4]

# 3. insert()
lst=[1,3,4]
lst.insert(1,2)
print(lst) # [1, 2, 3, 4]

# 4. remove()
lst=[1,2,3,4]
lst.remove(2)
print(lst) # [1, 3, 4]

# 5. pop()
lst=[1,2,3,4]
lst.pop(2)
print(lst) # [1, 2, 4]

# 6. clear()
lst=[1,2,3,4]
lst.clear()
print(lst) # []

# 7. index()
lst=[1,2,3,4]
print(lst.index(3)) # 2 returns the index of the first occurrence of the value

# 8. count()
lst=[1,2,3,4,2,]
print(lst.count(2)) # 2 returns the number of occurrences of the value

# 9. sort()
lst=[3,1,4,2]
lst.sort()
print(lst) # [1, 2, 3, 4] sorts the list

# 10. reverse()
lst=[1,2,3,4]
lst.reverse()
print(lst) # [4, 3, 2, 1] reverses the list

# 11. copy()
lst=[1,2,3,4]
lst1=lst.copy()
print(lst1) # [1, 2, 3, 4] copies the list
print( lst) # [1, 2, 3, 4] copies the list

