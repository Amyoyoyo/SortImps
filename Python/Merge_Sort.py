import random

def merge(left,right):
    i=0
    j=0
    sortedNums=[]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            sortedNums.append(left[i])
            i+=1
        else:
            sortedNums.append(right[j])
            j+=1
    if i!=len(left):
        sortedNums+=left[i:]
    if j!=len(right):
        sortedNums += right[j:]

    return sortedNums

def merge_sort(nums):
    if len(nums)>=2:
        middle=len(nums)//2
        left=nums[:middle]
        right=nums[middle:]
        return merge(merge_sort(left),merge_sort(right))
    else:
        return nums
    # 可直接写成如下语句，但是上面的语句初学者更易理解
    # def merge_sort(nums):
    #     return merge(merge_sort(nums[:len(nums) // 2]), merge_sort(nums[len(nums) // 2:])) if len(nums)>=2 else nums

def merge_sort2(nums):
    return merge(merge_sort(nums[:len(nums) // 2]), merge_sort(nums[len(nums) // 2:])) if len(nums) >= 2 else nums

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
    # checkTimes=100
    # for i in range(checkTimes):
    #     nums = [random.randint(0, 100) for x in range(random.randint(0, 100))]
    #     if not checker(nums, merge_sort(nums)):
    #         print('wrong!')
    #         break
    # print('done!All correct')
    # nums = [random.randint(0, 100) for x in range(random.randint(0, 100))]
    nums = [random.randint(0, 100) for x in range(11)]
    # checker(nums, merge_sort(nums))
    print('original:', nums)
    print('after sort:', merge_sort2(nums))