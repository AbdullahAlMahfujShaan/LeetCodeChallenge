class Solution {
public:
    string addStrings(string num1, string num2) {
        int num1_len = num1.length();
        int num2_len = num2.length();
        
        int max_len = max(num1_len, num2_len);
        int carry = 0;
        string result = "";
        
         for (int i = max_len - 1; i >= 0; i--) {
            int digit1 = i - max_len + num1_len >= 0
                ? num1[i - max_len + num1_len] - '0'
                : 0;
            int digit2 = i - max_len + num2_len >= 0
                ? num2[i - max_len + num2_len] - '0'
                : 0;
            int sum = digit1 + digit2 + carry;
            if (sum >= 10) {
                carry = 1;
                sum = sum - 10;
            } else carry = 0;
            result = (char)(sum + '0') + result;
        }
        if (carry) result = (char)(carry + '0') + result;
        return result;
    }
};