class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        def multiply(A):
           carry = 0
           B_list = []
           return_list = []
           for i in reversed(range(len(A))):
              temp = (int(A[i]) * 2) + carry
              if temp > 9:
                temp_str = str(temp)
                temp_list = list(temp_str)
                B_list.append(temp_list[1])
                carry = int(temp_list[0])
                if i == 0:
                  B_list.append(str(carry))
              else:
                carry = 0
                B_list.append(str(temp))
           return ''.join(str(B_list[i]) for i in reversed(range(len(B_list))))
        for i in range(len(A)):
            if A[i] != "0":
                A = A[i:]
                break
        temp = "2"
        while(True):
            if len(temp) == len(A):
                if temp == A or temp > A:
                    break
                else:
                    temp = multiply(temp)
            elif len(temp) < len(A):
                temp = multiply(temp)
            else:
                break
        if temp == A:
            return 1
        else:
            return 0
