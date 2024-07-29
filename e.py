def first_last_same(numbers_list):
    print("Given list:", numbers_list)

    first_num = numbers_list[0]
    last_num = numbers_list[-1]

    if first_num == last_num:
        return True
    else:
        return False
    
numbers_x = [10, 20, 30, 40, 10]
print("result is",first_last_same(numbers_x))
numbers_y = [75, 65, 35, 75, 40]
print("result is", first_last_same(numbers_y))




#Exercise 5: Check if the first and last number of a list is the same

#Write a function to return True if the first and last number of a given list is same. If numbers are different then return False