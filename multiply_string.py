#Given two numbers represented as strings, return multiplication of the numbers as a string.
#
# Note: The numbers can be arbitrarily large and are non-negative.
#Note2: Your answer should not have leading zeroes. For example, 00 is not a valid answer. 
#For example, 
#given strings "12", "10", your answer should be “120”.
#
class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def multiply(self, A, B):
        result = []
        carry = 0
        shift = 0
        max_len = max(len(A),len(B))
        for i in reversed(range(len(A))):
            temp = []
            for j in reversed(range(len(B))):
                temp.append(((int(B[j]) * int(A[i]))+carry) % 10)
                carry = ((int(B[j]) * int(A[i]))+carry) // 10
            if carry != 0:
                temp.append(carry)
                carry = 0
            start = shift
            temp_carry = 0
            for j in range(len(temp)):
                if start < len(result):
                    temp_sum = (result[start] + temp[j] + temp_carry) % 10
                    temp_carry = (result[start] + temp[j] + temp_carry) // 10
                    result[start] = temp_sum
                else:
                    temp_sum = (temp[j] + temp_carry) % 10
                    temp_carry = (temp[j] + temp_carry) // 10
                    result.append(temp_sum)
                start += 1
            if temp_carry != 0:
                result.append(temp_carry)
                temp_carry = 0
            shift += 1
        result_invert = []
        for i in reversed(range(len(result))):
            result_invert.append(result[i])
        save = 0
        while(save < len(result_invert) and result_invert[save] == 0):
            save += 1
        result_invert = result_invert[save:]
        if result_invert == []:
            result_invert = [0]
        return_str = ''.join(str(x) for x in result_invert)
        return return_str 
