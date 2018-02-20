### Find Atoi ###
#Steps:
#Count how many spaces at the beginning
#Check after the spacing if there is + or - (if there is no digit), if not a +/-/digit, return 0
#if last position has non digit, return 0
#if after +/-, there is non-digit, return 0
#Set to neg number if, there is - at the beginning (make sure index not less than 0)
#keep reading digitts, if it is > max int, return max int, else return the integer
class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        import sys
        spaces = 0
        is_neg = 0
        A_list = list(A)
        return_str = ""
        return_int = 0
        while(A_list[spaces] == " "):
            spaces += 1
            if spaces == len(A_list):
                return 0
        if A_list[spaces].isdigit() != True:
            if A_list[spaces] == "+" or A_list[spaces] == "-":
                if spaces == len(A_list) or A_list[spaces+1].isdigit() != True:
                    return 0
                if A_list[spaces] == "-":
                  is_neg = 1
            else:
                return 0
            spaces += 1
        while(True):
            if spaces == len(A_list) or A_list[spaces].isdigit() != True:
              break
            return_str += A_list[spaces]
            return_int = int(return_str)
            if is_neg:
                return_int = -return_int
                if return_int < -2147483648: #-sys.maxint-1:
                    return -2147483648 #-sys.maxint-1
            else:
                if return_int > 2147483647: #sys.maxint:
                    return 2147483647
            spaces += 1
        return return_int
