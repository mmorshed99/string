#Implement strStr().
#
#strstr - locate a substring ( needle ) in a string ( haystack ). 
#
#
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
     def find_strstr(A,B):
        A_list = list(A)
        B_list = list(B)
        if len(A_list)==0 or len(B_list)==0:
            return -1
        curr_master = A_list[0]
        curr_slave = B_list[0]
        master_id = 0
        slave_length = len(B_list)-1
        curr_length = 0
        while(True):
            if curr_master == curr_slave:
                if curr_length == slave_length:
                    return master_id-slave_length
                if master_id < len(A_list)-1:
                    curr_master = A_list[master_id+1]
                    master_id += 1
                    curr_length += 1
                    curr_slave = B_list[curr_length]
                else:
                    return -1
            else:
                master_id = master_id - curr_length
                curr_length = 0
                curr_slave = B_list[0]
                if master_id < len(A_list)-1:
                    curr_master = A_list[master_id+1]
                    master_id += 1
                else:
                    return -1
     return find_strstr(A,B) 
