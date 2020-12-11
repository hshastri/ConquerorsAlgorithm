def QuickSort(arr, left, right):
	if (left >= right):
		return
	pivot : int = (left + right) // 2
	index : int = partition(arr, left, right, pivot)
	#print(index)
	QuickSort(arr, left, index - 1)
	QuickSort(arr, index, right)

def partition(arr, left, right, pivot):
	while (left <= right):
		while (arr[left] < arr[pivot]):
			left += 1
		while (arr[right] > arr[pivot]):
			right -= 1
		if (left <= right):
			swap(arr, left, right)
			left += 1
			right -= 1
	return left

def swap(arr, i : int, j: int):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp

def main():
	arr = [10, 7, 3, 2]
	QuickSort(arr, 0, len(arr) - 1)
	print(arr)

if __name__ == '__main__':
	main()