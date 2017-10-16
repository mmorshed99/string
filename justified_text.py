def get_raw_lines(A,n):
    new_A = []
    temp = []
    temp_len = 0
    for i in range(0,len(A)):
        temp.append(A[i])
        curr = list(A[i])
        temp_len += len(curr)
        if temp_len > n:
            temp = temp[:-1]
            new_A.append(temp)
            temp = []
            temp.append(A[i])
            temp.append(" ")
            temp_len = len(curr) + 1
            
        elif temp_len == n:
            new_A.append(temp)
            temp = []
            temp_len = 0
        else:
            temp.append(" ")
            temp_len += 1
        if i == len(A) -1 :
            new_A.append(temp)
    return new_A

def get_justified_line(A,n):
    total_char = 0
    return_list = []
    temp = []
    gaps = 0
    for i in range(0,len(A)):
        if A[i] == " ":
            continue
        curr = list(A[i])
        gaps += 1
        temp.append(A[i])
        total_char += len(curr)
    spaces = n - total_char
    gaps = gaps -1 
    equal_spaces = spaces // gaps
    extra_spaces = spaces % gaps
    space_buffer = []
    for i in range(0,gaps):
        if extra_spaces > 0:
            space_buffer.append(equal_spaces+1)
            extra_spaces -= 1
        else:
            space_buffer.append(equal_spaces)
    for i in range(0,len(temp)):
        if i == len(temp) -1 :
            return_list.append(temp[i])
            break
        return_list.append(temp[i])
        for j in range(0,space_buffer[i]):
           return_list.append(" ")
    return return_list
A = ["This", "is", "an", "example", "of", "text", "justification."]
raw_lines = get_raw_lines(A,16)
processed_lines = [] 
for i in range(0,len(raw_lines)-1):
    processed_lines.append(get_justified_line(raw_lines[i],16))
processed_lines.append(raw_lines[len(raw_lines)-1])
final_result = []
for i in range(0,len(processed_lines)):
    final_result.append(''.join(str(e) for e in processed_lines[i]))
print(final_result)
