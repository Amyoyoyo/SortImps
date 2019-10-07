package selection.heap;

public class Heap {
    public static void heapSort(int[] nums) {
        for (int tailIndex = nums.length - 1; tailIndex > 0; tailIndex--) {
            heaptify(nums, tailIndex);
            swop(nums, 0, tailIndex);
        }
    }

    private static void heaptify(int[] nums, int tailIndex) {
        for (int i = tailIndex; i > 0; i--) {
            int parentIndex = (i - 1) / 2;
            if (nums[i] > nums[parentIndex]) {
                swop(nums, i, parentIndex);
            }
        }
    }

    private static void swop(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
