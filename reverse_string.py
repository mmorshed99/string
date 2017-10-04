#Given an input string, reverse the string word by word.
#
#Example:
#
#Given s = "the sky is blue",
#
#return "blue is sky the".
#
#
class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
       def rev_st(A):
          if A == None:
            return A
          A_list = A.split()
          j = len(A_list) - 1
          for i in range(0,len(A_list)//2):
              temp = A_list[i]
              A_list[i] = A_list[j]
              A_list[j] = temp
              j -= 1
          for i in range(0,len(A_list)-1):
              A_list[i] += ' '
          return ''.join(str(e) for e in A_list)
          
       return rev_st(A)
