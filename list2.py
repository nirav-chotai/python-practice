'''
Created on Sep 12, 2014

@author: nirav.chotai
'''
my_list = [1,9,3,8,5,7]

for number in my_list:
    print 2*number
    
start_list = [5, 3, 1, 2, 4]
square_list = []

for number in start_list:
    square_list.append(number**2)

square_list.sort()
print square_list

print "Before removing" 
print start_list

start_list.pop(1) 
print "After Pop"
print start_list

start_list.remove(2)
print "After Remove"
print start_list

del(start_list[0])
print "After Delete"
print start_list
