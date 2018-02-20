class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        A_list = A.split(".")
        B_list = B.split(".")
        idx1 = 0
        idx2 = 0
        if len(A_list) == 1 and len(B_list) == 1:
            if int(A_list[0]) == int(B_list[0]):
                return 0
            if int(A_list[0]) > int(B_list[0]):
                return 1
            else:
                return -1
        while(True):
            if idx1 == len(A_list) and idx2 == len(B_list):
                return 0
            if idx1 == len(A_list):
                if int(B_list[idx2]) == 0 and idx2+1 == len(B_list):
                    return 0
                return -1
            if idx2 == len(B_list):
                if int(A_list[idx1]) == 0 and idx1+1 == len(A_list):
                    return 0
                return 1
            if int(A_list[idx1]) > int(B_list[idx2]):
                return 1
            if int(A_list[idx1]) < int(B_list[idx2]):
                return -1
            idx1 += 1
            idx2 += 1
