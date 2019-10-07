package insertion.simple;

public class SimpleInsertion {
    public static void simpleInsertionSort(int[] nums){
        for (int i = 1; i < nums.length; i++) {
            int currentNum=nums[i];
            int tempIndex=i-1;
            while (tempIndex>=0 && nums[tempIndex]>currentNum){
                nums[tempIndex+1]=nums[tempIndex];
                tempIndex--;
            }
            nums[tempIndex+1]=currentNum;
        }
    }

    private static void swop(int[] nums, int index1, int index2){
        int temp=nums[index1];
        nums[index1]=nums[index2];
        nums[index2]=temp;
    }
}
