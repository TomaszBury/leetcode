#include <iostream>
#include <vector>
#include <algorithm>


std::vector<int> twoSum(const std::vector<int>& nums, int target){
    std::vector<int> numResult;

    for (int i = 0; i < nums.size(); ++i){
        for (int j = (1 + i); j < nums.size(); ++j){

            if (target == (nums[i] + nums[j])){
                std::cout << "We have winer!" << std::endl;
                numResult.push_back(i);
                numResult.push_back(j);
                return numResult;
            }
        }
    }
    return numResult;
}

int main(){
    std::vector<int> nums = {2,5,5,11}; 
    int target = 10;

    std::vector<int> result_1 = twoSum(nums, target);
    
    std::cout << "Resutl: ";
    std::for_each(result_1.begin(), result_1.end(), [](int val){
        std::cout << val << " ";
    });
    std::cout << std::endl;
}
