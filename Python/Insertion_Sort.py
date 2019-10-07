import random

def insertion_sort(nums):
    for i in range(1,len(nums)):
        for j in range(i):
            if nums[i]<nums[j]:
                temp=nums[i]
                for t in range(i-1,j,-1):
                    nums[t+1]=nums[t]
                nums[j]=temp
    return nums

def insertion_sort2(nums):
    for i in range(1,len(nums)):
        current=nums[i]
        preIndex=i-1
        while (preIndex>=0 and nums[preIndex]>current):
            nums[preIndex+1]=nums[preIndex]
            preIndex-=1
        nums[preIndex+1]=current
    return nums

if __name__ == "__main__":
    nums = [random.randint(0, 100) for x in range(10)]
    print('original:', nums)
    print('after sort:', insertion_sort2(nums))