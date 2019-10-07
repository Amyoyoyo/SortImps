package count;

public class Count {
    public static void countSort(int[] nums) {
        int min = nums[0];
        int max = nums[0];
        for (int num : nums) {
            min = (min > num) ? num : min;
            max = (max < num) ? num : max;
        }
        int[] countNums = new int[max - min + 1];
        for (int num : nums) {
            countNums[num - min] += 1;
        }
        int pointer = 0;
        for (int i = 0; i < countNums.length; i++) {
            if (countNums[i] != 0) {
                while (countNums[i] > 0) {
                    nums[pointer++] = i + min;
                    countNums[i]--;
                }
            }
        }
    }
}
