def print_positive_numbers(list1):
    result = []
    for num in list1:
        if num > 0:
            result.append(num)
    print(result)
    
list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]

print_positive_numbers(list1)
print_positive_numbers(list2)
