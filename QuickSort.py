def QuickSort(arr):
	return QuickSortHelper(arr, 0, len(arr) - 1)

def QuickSortHelper(arr, left, right):
	if (left >= right):
		return
	pivot : int = (left + right ) // 2
	index : int = partition(arr, left, right, pivot)
	QuickSortHelper(arr, left, index - 1)
	QuickSortHelper(arr, index, right)

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
	arr = [10, 7, 3, 12, 0, 69, 11, 2, 6]
	QuickSort(arr)
	print(arr)

if __name__ == '__main__':
    main()