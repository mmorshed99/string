#The count-and-say sequence is the sequence of integers beginning as follows:
#
#1, 11, 21, 1211, 111221, ...
#1 is read off as one 1 or 11.
#11 is read off as two 1s or 21.
#
#21 is read off as one 2, then one 1 or 1211.
#
#Given an integer n, generate the nth sequence.
#
#Note: The sequence of integers will be represented as a string.
#
#Example:
#
#if n = 2,
#the sequence is 11.
#
#
class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
       def count_and_say(A):
          if A == 1:
            return '1'
          curr_num = '1'
          count = 1
          while(True):
            count += 1  
            temp = curr_num
            curr_num = ''
            temp_list = list(temp)
            elem_count = 0
            curr_elem = temp_list[0]
            for i in range(0,len(temp_list)):
                if temp_list[i] == curr_elem:
                   elem_count += 1
                else:
                   curr_num = curr_num + str(elem_count) + curr_elem    
                   curr_elem = temp_list[i]
                   elem_count = 1
                if i == len(temp_list) - 1:
                   curr_num = curr_num + str(elem_count) + curr_elem    
            if count == A:           
                break
          return curr_num
       return count_and_say(A)      
