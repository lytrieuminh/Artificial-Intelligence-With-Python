#Bubble sort:
#Make function bubble_sort using bubble sort algorithm to sort numbers given by user; order numbers into the ascending order.
#Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
#https://en.wikipedia.org/wiki/Bubble_sort

### put your code here ###
def bubble_sort(a):
	for i in range (len(a)):
		swapped = True
		for j in range (len(a)-i-1):
			if a[j] > a[j+1]:
				a[j], a[j+1] = a[j+1], a[j]
				swapped = False
		if swapped:
			break
	return a


###

a = []
number = int(input("The Enter the Total Number of Elements: "))
for i in range(number):
  value = int(input("Please enter the %d Element: " % i))
  a.append(value)
print("The Sorted List in Ascending Order: ", bubble_sort(a))

