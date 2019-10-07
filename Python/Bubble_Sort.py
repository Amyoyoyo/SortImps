import random

def swap(nums,index1,index2):
    temp=nums[index1]
    nums[index1]=nums[index2]
    nums[index2]=temp

def bubble_sort(nums):
    tail=len(nums)-1
    pointer=0
    while tail>0:
        if nums[pointer]>nums[pointer+1]:
            swap(nums,pointer,pointer+1)
        pointer += 1
        if pointer==tail:
            pointer=0
            tail-=1
    return nums

def bubble_sort2(nums):
    for i in range(len(nums)):
        j=0
        while j < len(nums)-1-i:
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
            j+=1
    return nums

if __name__ == '__main__':
    nums=[random.randint(0,100) for x in range(10)]
    print('original:',nums)
    print('after sort:',bubble_sort2(nums))