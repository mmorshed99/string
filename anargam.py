#Given an array of strings, return all groups of strings that are anagrams. 
#Represent a group by a list of integers representing the index in the original list. Look at the sample case for clarification.
#Input : cat dog god tca
#Output : [[1, 4], [2, 3]]
class Solution:
	# @param A : tuple of strings
	# @return a list of list of integers
	def anagrams(self, A):
	    my_dict = {}
	    return_list = []
	    idx = 0
	    for i in A:
	        idx += 1
	        temp_list = list(i)
	        temp_sorted = sorted(i)
	        temp_str = ''.join(str(x) for x in temp_sorted)
	        try:
	            my_dict[temp_str].append(idx)
	        except:
	            my_dict[temp_str] = []
	            my_dict[temp_str].append(idx)
	    for i in my_dict.keys():
	        return_list.append(my_dict[i])
	    return return_list
