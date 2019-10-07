import random


def counting_sort(nums):
    maxNum, minNum = max(nums), min(nums)

    aux = [0] * (maxNum - minNum + 1)
    minIndex = 0 - minNum
    for i in range(len(nums)):
        aux[minIndex + nums[i]] += 1

    pointer = 0
    for i in range(len(aux)):
        while aux[i] > 0:
            nums[pointer] = i - minIndex
            aux[i] -= 1
            pointer += 1
    return nums


def counting_sort2(nums):
    maxNum, minNum = max(nums), min(nums)

    aux = [0] * (maxNum - minNum + 1)
    minIndex = 0 - minNum
    for i in range(len(nums)):
        aux[minIndex + nums[i]] += 1

    for i in range(1, len(aux)):
        aux[i] += aux[i - 1]

    target = [None] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        targetIndex = aux[nums[i] + minIndex] - 1
        target[targetIndex] = nums[i]
        aux[nums[i] + minIndex] -= 1
    return target


if __name__ == '__main__':
    # nums = [random.randint(-5, 10) for x in range(11)]
    # checker(nums, merge_sort(nums))
    nums = [7, 4, 0, -5, -2, -2, -4, 1, 6, -2, 7]
    print('original:', nums)
    print('after sort:', counting_sort2(nums))
