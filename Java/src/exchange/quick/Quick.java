package exchange.quick;

public class Quick {
    public static void quickSort(int[] nums){
        qSort(nums,0,nums.length-1);
    }

    private static void qSort(int[] nums,int lowIndex,int highIndex){
        if(lowIndex<highIndex){
            int pivotIndex=partition(nums,lowIndex,highIndex);
            qSort(nums,lowIndex,pivotIndex-1);
            qSort(nums,pivotIndex+1,highIndex);
        }
    }

    private static int partition(int[] nums,int lowIndex,int highIndex){
        int pivotNum=nums[lowIndex];
        while (lowIndex<highIndex){
            while (nums[highIndex]>pivotNum && highIndex>lowIndex){
                highIndex--;
            }
            nums[lowIndex]=nums[highIndex];
            while (nums[lowIndex]<=pivotNum && lowIndex<highIndex){
                lowIndex++;
            }
            nums[highIndex]=nums[lowIndex];
        }
        nums[lowIndex]=pivotNum;
        return lowIndex;
    }
}
