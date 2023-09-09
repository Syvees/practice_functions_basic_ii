# Countdown
list1 = []
def countdown (num):
    for i in range (num, -1, -1):
        list1.append(i)
    return list1

countdown (5)
print(list1)


# Print and Return
def print_and_return(list2):
    print(list2[0])
    return list2[1]

x = print_and_return([1,2])


# First Plus Length
def first_plus_length(list3):
    sum = list3[0] + len(list3)
    return sum
y = first_plus_length([1,2,3,4,5])


# Values Greater than Second
def values_greater_than_second(list4):
    new_list = []
    count = 0
    if len(list4) >= 2:
        for i in list4:
            if i > list4[1]:
                new_list.append(i)
                count+=1
        print(count)
        return new_list
    else:
        return False
values_greater_than_second([5,2,3,2,1,4])

#This Length, That Value
def length_and_value (size, value):
    new_list2 = []
    for i in range (0,size,1):
        new_list2.append(value)
    print(new_list2)
length_and_value(4,7)