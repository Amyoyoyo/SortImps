package test.merge.two;

import merge.two.Merge;
import org.junit.Assert;
import org.junit.Test;

public class MergeTest {
    @Test
    public void mergeSortTest(){
        int[] nums;

        nums=new int[]{1,11,12,4,2,6,9,0,3,7,8,2};
        Merge.mergeSort(nums);
        Assert.assertArrayEquals(new int[]{0,1,2,2,3,4,6,7,8,9,11,12},nums);
    }
}
