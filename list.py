'''
Created on Sep 12, 2014

@author: nirav.chotai
'''
zoo_animals = ["pangolin", "cassowary", "sloth", "cat"];
# One animal is missing!

if len(zoo_animals) > 3:
    print "The first animal at the zoo is the " + zoo_animals[0]
    print "The second animal at the zoo is the " + zoo_animals[1]
    print "The third animal at the zoo is the " + zoo_animals[2]
    print "The fourth animal at the zoo is the " + zoo_animals[3]
    
numbers = [5, 6, 7, 8]

print "Adding the numbers at indices 0 and 2..."
print numbers[0] + numbers[2]
print "Adding the numbers at indices 1 and 3..."
print numbers[1] + numbers[3]

zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
# Last night our zoo's sloth brutally attacked 
#the poor tiger and ate it whole.

# The ferocious sloth has been replaced by a friendly hyena.
zoo_animals[2] = "hyena"
print zoo_animals[2]
# What shall fill the void left by our dear departed tiger?
# Your code here!
zoo_animals[3] = "lion"
print zoo_animals[3]

suitcase = [] 
suitcase.append("sunglasses")

# Your code here!
suitcase.append("belt")
suitcase.append("wallet")
suitcase.append("watch")
list_length = len(suitcase) # Set this to the length of suitcase

print "There are %d items in the suitcase." % (list_length)
print suitcase

suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

first  = suitcase[0:2]  # The first and second items (index zero and one)
middle = suitcase[2:4]  # Third and fourth items (index two and three)
last   = suitcase[4:6]  # The last two items (index four and five)

animals = "catdogfrog"
cat  = animals[:3]   # The first three characters of animals
dog  = animals[3:6]              # The fourth through sixth characters
frog = animals[6:10]              # From the seventh character to the end

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")    # Use index() to find "duck"

# Your code here!
animals.insert(duck_index, "cobra")


print animals # Observe what prints after the insert operation

