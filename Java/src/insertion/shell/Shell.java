package insertion.shell;

public class Shell {
    public static void shellSort(int[] nums){
        int gap=1;
        while (gap<nums.length*3){
            gap=gap*3+1;
        }
        while (gap>0){
            for (int i = gap ; i < nums.length; i++) {
                int currentNum=nums[i];
                int tempIndex=i-gap;
                while (tempIndex>=0 && nums[tempIndex]>currentNum){
                    nums[tempIndex+gap]=nums[tempIndex];
                    tempIndex-=gap;
                }
                nums[tempIndex+gap]=currentNum;
            }
            gap/=3;
        }
    }
}
