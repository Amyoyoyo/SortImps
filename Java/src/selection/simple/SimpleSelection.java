package selection.simple;

public class SimpleSelection {
    public static void simpleSelectSort(int[] nums){
        int minIndex=0;
        for (int i = 0; i < nums.length; i++) {
            for (int j = i; j < nums.length; j++) {
                if (nums[j]<nums[minIndex]){
                    minIndex=j;
                }
            }
            swop(nums,minIndex,i);
        }
    }

    private static void swop(int[] nums, int index1, int index2){
        int temp=nums[index1];
        nums[index1]=nums[index2];
        nums[index2]=temp;
    }
}
