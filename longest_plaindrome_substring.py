class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        
        longest_len = 1
        longest_start = 0
        list_A = list(A)
        return_list = []
        return_string = ''
        for i in range(len(list_A)):
            start = i-1
            end = i+1
            while(start >= 0 and end < len(list_A) and list_A[start] == list_A[end]):
                if end - start + 1 > longest_len:
                    longest_len = end - start + 1
                    longest_start = start
                start -= 1
                end   += 1
            start = i
            end = i+1
            while(start >= 0 and end < len(list_A) and list_A[start] == list_A[end]):
                if end - start + 1 > longest_len:
                    longest_len = end - start + 1
                    longest_start = start
                start -= 1
                end   += 1
        longest_end = longest_start + longest_len
        for i in range(longest_start,longest_end):
            return_list.append(list_A[i])
        return_string = ''.join([str(x) for x in return_list])
        return return_string
