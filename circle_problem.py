def find_last_person(n):
    people = list(range(1, n + 1))  
    index = 0 
    count = 1 

    while len(people) > 1:
        if count == 3:
            people.pop(index)
            count = 1 
        else:
            index += 1
            count += 1
        if index >= len(people):
            index = 0

    return people[0] 


n = 100 #輸入n:0-100
result = find_last_person(n)
print(f"第 {result} 順位")