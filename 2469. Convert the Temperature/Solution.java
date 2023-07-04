import java.util.Arrays;

class Solution {
    public double[] convertTemperature(double celsius) {
        double[] arr={celsius + 273.15,celsius * 1.80 + 32.00};
        return arr;
    }
    public static void main(String[] args) {
        Solution solution=new Solution();
        double[] result= solution.convertTemperature(36.50);
        System.out.println(Arrays.toString(result));
    }
}
