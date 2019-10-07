import random

def selection_sort(nums):
    for i in range(len(nums)):
        minIndex = i
        for j in range(i + 1, len(nums)):
            minIndex = j if nums[j] < nums[minIndex] else minIndex
        if minIndex != i:
            nums[i], nums[minIndex] = nums[minIndex], nums[i]
    return nums


if __name__ == "__main__":
    nums = [random.randint(0, 100) for x in range(10)]
    print('original:', nums)
    nums = selection_sort(nums)
    print('after sort:', nums)

    # i = 1 if 1==1 else 2

    # a = [i + 2 for i in ]
