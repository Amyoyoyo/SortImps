import random


def Distribute(nums, key):
    # 由于对数值排序，基数为10（0,1,2,......,9）
    radixList = [[] for i in range(10)]

    for i in range(len(nums)):
        current = nums[i]
        for _ in range(key):
            index = current % 10
            current //= 10
        radixList[index].append(nums[i])
    return radixList


def Collection(nums, radixList):
    pointer = 0
    for radixNums in radixList:
        for num in radixNums:
            nums[pointer] = num
            pointer += 1
    return nums


def radix_sort(nums):
    maxNum = max(nums)
    d = 0
    # 确定关键字个数：个位（1位），十位(2位)，百位(3位)，千位(4位)........
    while maxNum > 0:
        d += 1
        maxNum //= 10

    for key in range(1, d + 1):  # 按低位优先LSD依次对各个关键字进行分配和收集
        radixList = Distribute(nums, key)
        nums = Collection(nums, radixList)

    return nums


if __name__ == '__main__':
    # nums = [random.randint(0, 100) for x in range(11)]
    nums = [random.randint(0, 100) for x in range(random.randint(0, 100))]
    # checker(nums, merge_sort(nums))
    # nums = [22, 9, 80, 85, 46, 48, 86, 12, 66, 19, 52]
    print('original:', nums)
    print('after sort:', radix_sort(nums))
