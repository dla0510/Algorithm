import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    //시간복잡도 : O(n)
    //공간복잡도 : O(n)??

    public static int maxAscendingSum(int[] nums) {
        int[] sum = new int[nums.length]; //sum[6]
        int pos = 0;
        sum[pos] = nums[0]; //sum[0]에 10담기
        int i = 1;
        while(i<nums.length){
            if(nums[i]>nums[i-1]){
                //nums[i]이 nums[i-1]보다 크면 sum[pos]에 nums[i] 더하기
                sum[pos]+=nums[i];
            }else{
                //nums[i]가 nums[i-1]보다 작으면 pos를 i로 바꾸고 sum[pos]에 nums[i]더하기
                pos=i; sum[pos]+=nums[i];
            }
            i++;
        }
        //sum[0]=60 sum[3]=65

        int com = sum[0];
        for(int j=1;j<sum.length;j++){
            if(sum[j]!=0){
                com=Math.max(com,sum[j]);
            }
        }
        return com;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        //input 받아서 nums[]에 담기
        String str = br.readLine();
        int idx = str.indexOf("[");
        str = str.substring(idx+1,str.length()-1);
        String[] array = str.split(",");
        int[] nums = new int[array.length];
        for(int i=0;i<nums.length;i++){
            nums[i]= Integer.parseInt(array[i]);
        } // nums = [10,20,30,5,10,50]

        System.out.println(maxAscendingSum(nums));
        //ascending order이 유지되는 한 값들을 합친 sum값들을 담은 배열 sum


    }
}