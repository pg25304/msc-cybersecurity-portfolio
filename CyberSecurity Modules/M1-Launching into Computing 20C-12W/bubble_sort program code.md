```python
#Measure how long the sort takes
import time 
#plot performance
import matplotlib.pyplot as plt
#Generate random number
import random
#buble-sort function
def bubble_sort(list_to_sort):
    #get length/size of the list
    n = len(list_to_sort)
    #outer loop with range same as number of items
    for i in range(n):
        #inner loop, compare adjacent items/elements and swap if they are not in order
        for j in range(0, n-i-1):
            #Condition, compare two adjacent number in the list
            if list_to_sort[j] > list_to_sort[j+1]:
                list_to_sort[j],list_to_sort[j+1] =  list_to_sort[j+1], list_to_sort[j]
   # return list_to_sort
# Performance test with different sizes
sizes = [100, 200, 300, 400, 500]
times = []

for size in sizes:
    #create a random list of 'size' element, 
    #random.randit(0, 1000); create random integer 0-1000
    #for_in range(size); Loop exactly size times -itsn't loop just repeat action; 
    #"_" charactor means "I am gonna loop the variable"
    test_data = [random.randint(0, 1000) for _ in range(size)]
    #measure time taken, start time
    start = time.time()
    bubble_sort(test_data)
    #end of process
    end = time.time()
    #save the time taken in times list
    times.append(end - start)

# Plotting
plt.plot(sizes, times, marker='o')
plt.title("Bubble Sort Performance - (module 1 UoEO-Payman Ghorbani)")
plt.xlabel("Input Size")
plt.ylabel("Time (seconds)")
plt.grid(True)
plt.show()

                
                
        
```


    
![png](output_0_0.png)
    



```python

```


```python

```
