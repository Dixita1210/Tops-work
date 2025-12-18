29) Write a Python function to get the largest number, smallest num 
and sum of all from a list. 

def list_stats(numbers):
    largest = max(numbers)      
    smallest = min(numbers)     
    total = sum(numbers)       
    
    return largest, smallest, total


nums = [10, 5, 30, 2, 50]
print(list_stats(nums))



