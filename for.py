'''
Created on Sep 12, 2014

@author: nirav.chotai
'''
names = ["Adam","Alex","Mariah","Martine","Columbus"]
for name in names:
    print name

webster = {
    "Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

for key in webster:
    print webster[key]

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for n in a:
    if (n%2==0):
        print n

# Write your function below!
def fizz_count(x):
    count = 0
    for n in x:
        if (n=="fizz"):
            count = count+1
    return count
    
lists = ["fizz","cat","fizz"]
number = fizz_count(lists)
print number