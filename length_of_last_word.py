class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        mylen = 0
        A_list = list(A)
        found_char = 0
        for i in reversed(range(len(A_list))):
            if found_char:
                if A_list[i] == " ":
                    return mylen
                else:
                    mylen += 1
                continue
            if found_char == 0 and A_list[i] != " ":
                found_char = 1
                mylen += 1
        return mylen
### another day
class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        count = 0
        if len(A) == 0:
            return 0
        i = len(A)-1
        while(i >= 0):
            if A[i] == " ":
                i -= 1
                continue
            else:
                while(A[i] != " "):
                    count += 1
                    i -= 1
                    if i < 0:
                        break
                break
        return count
