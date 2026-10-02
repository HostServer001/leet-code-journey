// https://leetcode.com/problems/palindrome-number/

#include <vector>
using namespace std;


class Solution {
public:
    bool isPalindrome(int x) {
        string x_str = to_string(x);
        string x_str_rev;
        int i = x_str.size();

        while (i != -1){
            x_str_rev += x_str[i];
            i -= 1;
        }
        
        x_str_rev.erase(0,1);
        
        if (x_str == x_str_rev){
            return true;
        }
        else{
            return false;
        }
    }
};

//Notes
//This was my first time solving a problem is C++
