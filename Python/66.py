 # How can you pick a random item from a list or tuple? 
import random 

lst= [1,2,3,4,5,6,7,89,10]
random_item=random.choice(lst) #using choice - return random elemnent
random_item=random.randint(0,len(lst) -1) #using randint for number or index but have to give a range 
print(random_item)