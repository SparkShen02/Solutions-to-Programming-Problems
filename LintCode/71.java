import java.util.*;  
import java.util.Collections;

/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */
public class Solution {
    /**
     * @param root: A Tree
     * @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
     */
    public List<List<Integer>> zigzagLevelOrder(TreeNode root){
        List<List<Integer>> result=new ArrayList<>();
        if(root==null){return result;}
        List<TreeNode> next=new ArrayList<>();
        List<TreeNode> line=new ArrayList<>();
        List<Integer> lineResult=new ArrayList<>();
        
        int countLine=0;
        TreeNode current;
        next.add(root);
        while(next.size()!=0){
            countLine++;
            List<TreeNode> temp=new ArrayList<>();
            line=new ArrayList(next);
            next=new ArrayList(temp);
            while(line.size()!=0){
                current=line.remove(0);
                lineResult.add(current.val);
                if(current.left!=null){next.add(current.left);}
                if(current.right!=null){next.add(current.right);}
            }
            if(countLine%2==0){Collections.reverse(lineResult);}
            result.add(lineResult);
            lineResult=new ArrayList<>();
        }
        return result;
    }
}