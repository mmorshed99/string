### Find Atoi ###
#Steps:
#Count how many spaces at the beginning
#Check after the spacing if there is + or - (if there is no digit), if not a +/-/digit, return 0
#if last position has non digit, return 0
#if after +/-, there is non-digit, return 0
#Set to neg number if, there is - at the beginning (make sure index not less than 0)
#keep reading digitts, if it is > max int, return max int, else return the integer
