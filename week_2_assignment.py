#create an empty list
my_list = []

#append new elements 
elements =[10,20,30,40]

for i in elements:
    my_list.append(i)

#insert new element to second position index 1
my_list.insert(1,15)

#extend my_list
my_list.extend([50,60,70])

#remove last element from my_list
my_list.pop(-1)

#sort in ascending order
my_list.sort()

#find and print index of value 30 in my_list
print(my_list.index(30))