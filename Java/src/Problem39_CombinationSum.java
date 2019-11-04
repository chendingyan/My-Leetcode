import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class Problem39_CombinationSum {
    public static List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        ArrayList<Integer> list = new ArrayList<>();
        Arrays.sort(candidates);
        //System.out.println(candidates);
        backtrack(candidates, target, res, 0, list);
        System.out.println(res);
        res = new ArrayList<>();
        list = new ArrayList<>();
        Arrays.sort(candidates);
        //System.out.println(candidates);
        helper(candidates, target,  res, 0,  list);
        System.out.println(res);
        return res;
    }

    public static void backtrack(int[] candidates, int target, List<List<Integer>> res, int i, ArrayList<Integer> tmp_list) {
        if (target < 0) return;
        if (target == 0) {
            res.add(new ArrayList<>(tmp_list));
            return;
        }
        for (int start = i; start < candidates.length; start++) {
            if (target < candidates[start]) break;
            //System.out.println(start);
            tmp_list.add(candidates[start]);
            //System.out.println(tmp_list);
            backtrack(candidates, target - candidates[start], res, start, tmp_list);
            tmp_list.remove(tmp_list.size() - 1);
        }
    }
    public static void helper(int [] candidates, int target,  List<List<Integer>> res, int i, ArrayList<Integer> tmp_list){
        if(target < 0){
            return;
        }
        if(target == 0){
            res.add(new ArrayList<>(tmp_list));
            return;
        }
        for(int start = i; start < candidates.length; start++){
            if(candidates[start] > target){
                break;
            }else{
                tmp_list.add(candidates[start]);
                helper(candidates, target - candidates[i],  res, start, tmp_list);
                tmp_list.remove(tmp_list.size()-1);
            }
        }

    }



    public static void main(String[] args) {
        int [] candidates = new int []{2,3,6,7};
        int target = 7;
        combinationSum(candidates,target);
    }
}
