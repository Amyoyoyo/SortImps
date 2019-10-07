package merge.two;

public class Merge {
    public static void mergeSort(int[] nums) {
        int[] resultNums = new int[nums.length];
        split(nums, resultNums, 0, nums.length - 1);
    }

    private static void split(int[] nums, int[] resultNums, int leftIndex, int rightIndex) {
        if (leftIndex == rightIndex) {
            resultNums[leftIndex] = nums[leftIndex];
        } else {
            int midIndex = leftIndex + ((rightIndex - leftIndex) >> 1);     //将无序的部分分为左右两部分
            split(nums, resultNums, leftIndex, midIndex);              //递归地将无序的左部分分割为两部分
            split(nums, resultNums, midIndex + 1, rightIndex);//递归地将无序的右部分分割为两部分
            merge(nums, resultNums, leftIndex, midIndex, rightIndex);   //递归地将有序的左右两部分归并为一个序列
        }
    }

    private static void merge(int[] nums, int[] resultNums, int leftIndex, int midIndex, int rightIndex) {
        int i, j, k;
        for (i = leftIndex, j = midIndex + 1, k = leftIndex; i <= midIndex && j <= rightIndex; k++) {
            if (nums[i] <= nums[j]) {
                resultNums[k] = nums[i++];
            } else {
                resultNums[k] = nums[j++];
            }
        }
        if (i <= midIndex) {//将有序剩余的左部分复制到resultNums
            for (; i <= midIndex; i++, k++) {
                resultNums[k] = nums[i];
            }
        }
        if (j <= rightIndex) {//将有序剩余的右部分复制到resultNums
            for (; j <= rightIndex; j++) {
                resultNums[k] = nums[j];
            }
        }
        for (int m = leftIndex; m <= rightIndex; m++) {
            nums[m] = resultNums[m];
        }
    }
}
