class Solution:
    def myAtoi(self, string: str) -> int:
        if (string.startswith(' ')):
            string_2 = string.strip()
        else:
            string_2 = string
        res = 0
        sign = 1
        i = 0
        result = string_2.find('.')
        if (string_2.startswith('-')):
            sign = -1
            i = 1
        elif (string_2.startswith('+')):
            sign = 1
            i = 1
        if (result != -1):
            len_1 = result
        else:
            len_1 = len(string_2)
        if  re.match("^[a-zA-Z]+.*", string_2):
            return 0
        else:
            for j in range(i,len_1):
                if not string_2[j].isdigit():
                    break
                else:
                    res = res * 10 + (ord(string_2[j]) - ord('0')) 
            num = sign*res
            neg_limit= -2147483648
            pos_limit= 2147483647
            if num<neg_limit:
                return neg_limit
            elif num>pos_limit:
                return pos_limit
            else:
                return num
