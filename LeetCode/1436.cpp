class Solution {
public:
    /*
    Find the cityB that is not a cityA. Use an unordered_set (hash table) to store the cityAs. 
    Time complexity: O(n), Space complexity: O(n). 
    */
    string destCity(vector<vector<string>>& paths) {
        std::unordered_set<string> cityAs; 
        for (int i = 0; i < paths.size(); i++) {
            string cityA = paths[i][0]; 
            cityAs.insert(cityA); 
        }
        for (int i = 0; i < paths.size(); i++) {
            string cityB = paths[i][1]; 
            if (cityAs.count(cityB) == 0)
                return cityB; 
        }
        return NULL; 
    }
};