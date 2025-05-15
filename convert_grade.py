import math

def revert(arr):
    rev_arr = []
    for i in arr:
        rev_i = 0;
        count = 0;
        while(i != 0):#25
    
            temp = i % 10; #2
            rev_i = rev_i*10 +temp  
            i = i // 10 #2
        rev_arr.append(rev_i)
    return rev_arr
input = [35,46,57,91,29]
print(revert(input))