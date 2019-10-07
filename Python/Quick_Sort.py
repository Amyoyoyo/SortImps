import random


def partition(nums, low, high):
    pivotVal = nums[low]
    while low < high:
        while nums[high] > pivotVal and high > low:
            high -= 1
        nums[low] = nums[high]
        while nums[low] < pivotVal and low < high:
            low += 1
        nums[high] = nums[low]
    nums[low] = pivotVal
    return low


def qSort(nums, low, high):
    if (low < high):
        pivotKey = partition(nums, low, high)
        qSort(nums, low, pivotKey - 1)
        qSort(nums, pivotKey + 1, high)
    return nums


def quick_sort(nums):
    return qSort(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    # nums = [random.randint(0, 100) for x in range(11)]
    # checker(nums, merge_sort(nums))
    nums = [22, 9, 80, 85, 46, 48, 86, 12, 66, 19, 52]
    print('original:', nums)
    print('after sort:', quick_sort(nums))
