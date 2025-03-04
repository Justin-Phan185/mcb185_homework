def nums(num_lst):
	count = 0
	for num in num_lst:
		count += 1
	return count
#print(nums([1,2,3,4,5,7]))

def minimum(num_lst):
	mini = num_lst[0]
	for num in num_lst: #how important is the [1:] here??
		if num < mini:
			mini = num
	return mini
#print(minimum([2,2,1,4,5,7]))

def maximum(num_lst):
	maxi = num_lst[0]
	for num in num_lst:
		if num > maxi:
			maxi = num
	return maxi
#print(maximum([2,2,1,4,5,7]))

def mini_maxi(num_lst):
	mini = num_lst[0]
	maxi = num_lst[0]
	for num in num_lst:
		if num > maxi:
			maxi = num
		if num < mini:
			mini = num
	return mini,maxi
print(mini_maxi([2,2,1,4,5,7]))	

def mean_sd(num_lst):
	mean = 0
	sd = 0
	for num in num_lst:
		mean += num
	mean = mean / len(num_lst)
	
	for num in num_lst:
		sd += (num - mean)**2
	sd = (sd / (len(num_lst)-1))**0.5
	
	return mean, sd
#print(mean_sd([1,2,3,4,5]))

def median(num_lst):
	length = len(num_lst)
	if length % 2 == 0:
		index1 = len(num_lst)//2
		index2 = (len(num_lst)//2)-1
		med = (num_lst[index1] + num_lst[index2]) / 2
	else: 
		med = num_lst[len(num_lst)//2]
	return med
#print(median([1,2,3,4,5]))
#print(median([1,2,3,4,5,6]))