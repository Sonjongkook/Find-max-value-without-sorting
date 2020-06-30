def findfiveLargestNumbers(array):
	fiveLargest = [None] *5
	for num in array:
		updateLargest(fiveLargest, num)
	return fiveLargest
   
# Helper method to compare largestlist and number in list
def updateLargest(fiveLargest, num): 
	if fiveLargest[4] is None or num > fiveLargest[4]: #update the largest list if the elment is none or the number in list is larger
		shiftUpdate(fiveLargest, num, 4)
	elif fiveLargest[3] is None or num > fiveLargest[3]:
		shiftUpdate(fiveLargest, num, 3)
	elif fiveLargest[2] is None or num > fiveLargest[2]:
		shiftUpdate(fiveLargest, num, 2)
	elif fiveLargest[1] is None or num > fiveLargest[1]:
		shiftUpdate(fiveLargest, num, 1)
	elif fiveLargest[0] is None or num > fiveLargest[0]:
		shiftUpdate(fiveLargest, num, 0)

def shiftUpdate(array, num, idx): #if we input num in largestlist the order should be changed
	for i in range(idx+1): #iterate from start to end because we need to shift downward first and change the number in target index
		if i ==idx:
			array[i] = num #put the number in largestlist
		else:
			array[i] = array[i+1] #shfting to the downward


test_case1= [3,5,6,7,5,7,0,13,55,3,22,12,78,90,223,11,5,4,34]
print(findfiveLargestNumbers(test_case1))
test_case2 = [-1,-2,-3,-7,-17,-27,-18,-541,-8,-7,7]
print(findfiveLargestNumbers(test_case2))
test_case3 = [7,7,7,7,7,7,8,7,7,7,7]
print(findfiveLargestNumbers(test_case3))

