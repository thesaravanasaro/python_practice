#Exercise 6: Display numbers divisible by 5 from a list

#Iterate the given list of numbers and print only those numbers which are divisible by 5

num_list =[10, 20, 30, 40, 50,]
print("given list",num_list)
print('Divisible by 5:')
for num in num_list:
    if num %5==0:
        print(num)