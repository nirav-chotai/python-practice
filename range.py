'''
Created on Sep 12, 2014

@author: nirav.chotai
'''
#range(stop)
#range(start, stop)
#range(start, stop, step)

def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print my_function(range(0,3)) # Add your range between the parentheses!

n = [3, 5, 7]

def total(numbers):
    result = 0
    for i in range(len(numbers)):
        result = result + numbers[i]
    return result
    
print total(n)

n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
    result = ""
    for i in words:
        result = result+i
    return result

print join_strings(n)

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
    results =[]
    for numbers in lists:
        for i in numbers:
            results.append(i)
    return results

print flatten(n)