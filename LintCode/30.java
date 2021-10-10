/**
 * Definition of Interval:
 * public classs Interval {
 *     int start, end;
 *     Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

public class Solution {
    /**
     * @param intervals: Sorted interval list.
     * @param newInterval: new interval.
     * @return: A new interval list.
     */
     /**
      1. Sort the intervals based on increasing order of start.
      2. Push the first interval on to a stack.
      3. For each interval do the following
        a. If the current interval does not overlap with the stack top, push it.
        b. If the current interval overlaps with stack top,
           update stack top with the end of current interval.
      4. At the end stack contains the merged intervals. 
      */
    public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
        if(intervals.size()==0){
            intervals.add(newInterval);
            return intervals;
        }
        
        int index=0;
        Interval curr, top;
        List<Interval> merge = new Stack<>();
        
        while(index<intervals.size()){
            curr=intervals.get(index);
            if(curr.start<newInterval.start){
                index++;
            }
            else{break;}
        }
        intervals.add(index, newInterval);//insert newInterval and make sure that intervals is sorted
        
        merge.add(intervals.get(0));
        for(Interval cur : intervals){
            top=merge.get(merge.size()-1);
            if(cur.start>top.end){
                merge.add(cur);
            }
            if(cur.start<=top.end){
                top.end=Math.max(cur.end, top.end);
            }
        }
        return merge;
    }
}