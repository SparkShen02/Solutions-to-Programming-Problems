class Solution {
public:
    /*
    Traverse timePoints, and use an array of length 1440 to record whether a time-point (0~1439) is in timePoints. 
    Then, traverse the array, and for each time-point, find the closest next time-point. 
    Time complexity: O(n), Space complexity: O(1). 
    */
    int findMinDifference(vector<string>& timePoints) {
        int arr[1440]; 
        for (int i = 0; i < 1440; i++) 
            arr[i] = 0; 
        
        int minTimeInMin = INT_MAX; 
        for (int i = 0; i < timePoints.size(); i++) {
            int curTimeInMin = (timePoints[i][0] - '0') * 10; 
            curTimeInMin += timePoints[i][1] - '0'; 
            curTimeInMin *= 60; 
            curTimeInMin += (timePoints[i][3] - '0') * 10; 
            curTimeInMin += timePoints[i][4] - '0'; 
            
            if (arr[curTimeInMin] == 1)
                return 0; 
            arr[curTimeInMin] = 1;
            minTimeInMin = min(minTimeInMin, curTimeInMin); 
        }

        int ans = INT_MAX; 
        int curTime = minTimeInMin; 
        while (curTime < 1440) {
            int lastTime = curTime;
            curTime += 1;
            while (arr[curTime%1440] != 1)
                curTime += 1; 
            ans = min(ans, curTime - lastTime); 
        }
        return ans; 
    }
};