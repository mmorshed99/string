class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        def find_val(sent_char):
            if sent_char == "I":
                return 1
            elif sent_char == "V":
                return 5
            elif sent_char == "X":
                return 10
            elif sent_char == "L":
                return 50
            elif sent_char == "C":
                return 100
            elif sent_char == "D":
                return 500
            else:
                return 1000
        A_list = list(A)
        int_val = 0
        i = len(A_list) - 1
        while(i >= 0):
            curr_val = find_val(A_list[i])
            int_val += curr_val
            if i != 0:
                next_val = find_val(A_list[i-1])
                if next_val < curr_val:
                    int_val -= next_val
                    i = i -2
                    continue
            i = i -1
        return int_val
