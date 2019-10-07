def shell_sort(nums):
    gap = 1
    while gap < len(nums) / 3:
        gap = 3 * gap + 1

    while gap > 0:
        for i in range(gap, len(nums)):
            current = nums[i]
            preIndex = i - gap
            while preIndex >= 0 and nums[preIndex] > current:
                nums[preIndex + gap] = nums[preIndex]
                preIndex -= gap
            nums[preIndex + gap] = current
        gap = gap // 3
    return nums


def bucket_sort(nums, bucket_size):
    minNum, maxNum = min(nums), max(nums)
    bucketNum = (maxNum - minNum) // bucket_size + 1
    buckets = [[] for x in range(bucketNum)]

    for i in range(len(nums)):
        buckets[(nums[i] - minNum) // bucket_size].append(nums[i])

    result = []
    for bucket in buckets:
        if bucket:
            shell_sort(bucket)
            result += bucket
    return result


if __name__ == '__main__':
    # nums = [random.randint(0, 100) for x in range(11)]
    # checker(nums, merge_sort(nums))
    nums = [22, 9, 80, 85, 46, 48, 86, 12, 66, 19, 52]
    print('original:', nums)
    print('after sort:', bucket_sort(nums, 5))
