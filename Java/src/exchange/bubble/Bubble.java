package exchange.bubble;

public class Bubble {
    public static void main(String[] args) {
        int[] nums;

        nums=new int[]{1,11,12,4,2,6,9,0,3,7,8,2};
        Bubble.bubblesort(nums);
        System.out.println(Bubble.printNums(nums));
    }
    public static void bubblesort(int[] nums){
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < nums.length -1- i; j++) {
                if(nums[j]>nums[j+1]){
                    swop(nums,j,j+1);
                }
            }
        }
    }
    private static void swop(int[] nums, int index1, int index2){
        int temp=nums[index1];
        nums[index1]=nums[index2];
        nums[index2]=temp;
    }
    private static String printNums(int[] nums){
        StringBuffer result=new StringBuffer();
        for (int num : nums) {
            result.append(num);
            result.append(", ");
        }
        return result.toString();
    }
}
