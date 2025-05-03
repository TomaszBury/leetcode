
#include <iostream>
#include <string>
#include <algorithm>

bool isPalindrome(int x) {
    std::string strNum = std::to_string(x);
    std::string reversedStrNum = strNum;
    std::reverse(reversedStrNum.begin(), reversedStrNum.end());
    return strNum == reversedStrNum;
}

int main() {
    int number;
    std::cout << "Enter an integer: ";
    std::cin >> number;

    if (isPalindrome(number)) {
        std::cout << "true" << std::endl;
    } else {
        std::cout << "false" << std::endl;
    }

    return 0;
}