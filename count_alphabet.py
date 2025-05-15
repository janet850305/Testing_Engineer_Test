from collections import OrderedDict

mystring="Hello welcome to Cathay 60th year anniversary"
def count_alphabet(str1):
    alpha_dict={}
    str1 =str1.upper()
    for i in str1:
    
        if i != " ":
            if i not in alpha_dict:
                alpha_dict[i]=1
            else:
                alpha_dict[i] += 1
    sorted_dict = sorted(alpha_dict.items(), key=lambda x: str(x[0]))
    for key,value in sorted_dict:
        print(f"{key} {value}")
count_alphabet(mystring)