class Solution 
{
public:
    /*
    Use two pointers, one points to the left boundary and the other points to the right boundary. 
    Area of current container = min(leftHeight, rightHeight) * distance. Start from the left-most and right-most positions. At each step, among the two possible actions (with the other boundary fixed, move the left boundary or the right boundary), always move the shorter boundary because it's the only way that may increase the area. 
    Time complexity: O(n), Space complexity: O(1). 
    */
    int maxArea(vector<int>& height) 
    {
        int left = 0, right = height.size() - 1;
        int maxArea = 0;
        while (left < right)
        {
            int curArea = min(height[left], height[right]) * (right - left); 
            maxArea = max(maxArea, curArea);
            
            // Move the shorter boundary
            if (height[left] < height[right])
                left++;
            else
                right--;
        }
        return maxArea;
    }
};