def heaptify(nums, tailIndex):
    for i in range(tailIndex, 0, -1):
        parent = (i - 1) // 2
        if parent < 0:
            break
        if nums[i] > nums[parent]:
            nums[i], nums[parent] = nums[parent], nums[i]
    return nums


def heap_sort(nums):
    for i in range(len(nums)):
        tailIndex = len(nums) - 1 - i  # tailIndex后为有序区
        nums = heaptify(nums, tailIndex)
        nums[0], nums[tailIndex] = nums[tailIndex], nums[0]
    return nums


if __name__ == '__main__':
    # nums = [random.randint(0, 100) for x in range(11)]
    # checker(nums, merge_sort(nums))
    nums = [22, 9, 80, 85, 46, 48, 86, 12, 66, 19, 52]
    print('original:', nums)
    print('after sort:', heap_sort(nums))
