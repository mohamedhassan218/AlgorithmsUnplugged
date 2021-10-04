def sum(number):
    if number == 1 :                         #base case
        return 1
    else :
        return number + sum(number-1)        #recursive case
print (sum(22))



array_of_books = [ 'koko','a' , 'b' , 'mo' , 'df' , 'gh']
def insertion_sort (arr):
    for i in range ( len(arr)) :              #sort book at position i by shifting
        hand = arr[i]                       #take current book 
        j = i-1
        while j >= 1 and arr[j] > hand:            #as long as current position not found 
            arr[ j+1 ] = arr[j]                   #shift book right to position j
            j  = j - 1
        arr[j] = hand                     #insert current book at correct position
    return arr

def quicksort(array):
    if len(array) <2:                  #base case
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]  #recursive case
        greater = [ m for m in array[1:] if m > pivot]
        return quicksort(less) + pivot + quicksort(greater)
array5 = [2,8,20,6,103,4,900]
print (quicksort(array5))

# merges two sorted arrays a & b
def merge(a,b):
	c=[]
	a_idx,b_idx=0,0
	while a_idx<len(a) and b_idx<len(b):
		if a[a_idx]<b[b_idx]:
			c.append(a[a_idx])
			a_idx+=1
		else:
			c.append(b[b_idx])
			b_idx+=1
	if a_idx==len(a): c.extend(b[b_idx:])
	else: 			  c.extend(a[a_idx:])
	return c 

# performs merge sort on the input array
def merge_sort(a):
	# a list of zero or one elements is sorted, by definition
	if len(a)<=1: return a 
	# split the list in half and call merge sort recursively on each half
	left,right = merge_sort(a[:len(a)/2]),merge_sort(a[len(a)/2:])
	# merge the now-sorted sublists
	return merge(left,right)

def create_array(size=10,max=50):
	from random import randint
	return [randint(0,max) for _ in range(size)]

a=create_array()
print (a) 
a=merge_sort(a)
print (a)
                                              #Merge sort from github 

 

