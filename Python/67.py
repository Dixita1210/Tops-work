 #How can you pick a random item from a range? 
#using randint
import random
r=range(0,11)
random_item=random.randint(0,len(r) -1)
print(random_item)