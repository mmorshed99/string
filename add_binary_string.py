def add_string(A,B):
    A_list = list(A)
    B_list = list(B)
    if A == None:
        return B
    if B == None:
        return A
    carry = 0
    count_A = len(A)- 1
    count_B = len(B) -1
    result = []
    while(True):
        if count_A > -1 and count_B > -1:
          A_int = int(A_list[count_A])
          B_int = int(B_list[count_B])
          temp = A_int+B_int
          if temp == 2:
            temp = carry
            carry = 1
          else:
            temp = temp + carry
            carry = 0
            if temp ==2:
                temp = 0
                carry = 1
          result.append(temp)
        count_A -= 1
        count_B -= 1
        if count_A < 0 and count_B <0:
            break
        elif count_A < 0:
            temp = int(B_list[count_B]) + carry
            carry = 0
            if temp == 2:
                temp = 0
                carry = 1
            result.append(temp)
        elif count_B < 0:
            temp = int(A_list[count_A]) + carry
            carry = 0
            if temp == 2:
                temp = 0
                carry = 1
            result.append(temp)
    if carry > 0:
        result.append(carry)

    return result

A = '00111'
B = '00010'

my_result=add_string(A,B)
my_result_sorted = []
j = len(my_result)-1
#zero = 1
for i in range(0,len(my_result)):
    my_result_sorted.append(my_result[j])
    if my_result[j] != 0:
        zero = 0
    j = j -1
#if zero:
#    print('0')
my_result_sorted2 = []
remove_zero = 1
for i in range(0,len(my_result_sorted)):
    if i == len(my_result_sorted)-1:
        my_result_sorted2.append(my_result_sorted[i])
        break
    if remove_zero:
      if my_result_sorted[i] == 0:
          continue
      else:
         remove_zero = 0
    my_result_sorted2.append(my_result_sorted[i])
        
return_result = ''.join(str(e) for e in my_result_sorted2)
print(return_result)
