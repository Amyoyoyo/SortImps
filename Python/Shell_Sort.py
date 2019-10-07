import random

def shell_sort(nums):
    gap=1
    while gap<len(nums)/3:
        gap=3*gap+1

    while gap>0:
        for i in range(gap,len(nums)):
            current=nums[i]
            preIndex=i-gap
            while preIndex>=0 and nums[preIndex]>current:
                nums[preIndex+gap]=nums[preIndex]
                preIndex-=gap
            nums[preIndex+gap]=current
        gap=gap//3
    return nums



def checker(orin_nums,sorted_nums):
    for i in range(len(sorted_nums)-1):
        if sorted_nums[i]>sorted_nums[i+1]:
            print('Wrong!!!!!')
            print('original:', orin_nums)
            print('after sort:', sorted_nums)
            return False
    print('Correct.')
    return True

if __name__ == "__main__":
    checkTimes=100
    for i in range(checkTimes):
        nums = [random.randint(0, 100) for x in range(random.randint(0, 100))]
        if not checker(nums, shell_sort(nums)):
            print('wrong!')
            break
    print('done!All correct')
    nums = [random.randint(0, 100) for x in range(random.randint(0, 100))]
    # nums = [random.randint(0, 100) for x in range(11)]
    checker(nums, shell_sort(nums))
    # print('original:', nums)
    # print('after sort:', shell_sort(nums))
