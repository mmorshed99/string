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
