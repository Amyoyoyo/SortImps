package test.exchange.quick;

import exchange.quick.Quick;
import org.junit.Assert;
import org.junit.Test;

import java.util.Queue;

public class QuickTest {
    @Test
    public void quickSortTest(){
        int[] nums;

        nums=new int[]{1,11,12,4,2,6,9,0,3,7,8,2};
        Quick.quickSort(nums);
        Assert.assertArrayEquals(new int[]{0,1,2,2,3,4,6,7,8,9,11,12},nums);
    }
}
