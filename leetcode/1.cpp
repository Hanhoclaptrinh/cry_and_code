#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numMap; // hash map
        for (int i = 0; i < nums.size(); i++) {
            int c = target - nums[i];

            if (numMap.find(c) != numMap.end()) {
                return {numMap[c], i};
            }

            numMap[nums[i]] = i;
        }
        return {};
    }


    // use nested loop
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] + nums[j] == target) {
                    return {i, j};
                }
            }
        }
        return {};
    }
};