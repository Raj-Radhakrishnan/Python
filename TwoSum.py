def find_two_sum(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    """
    list =[]
    count =1
    count1 =1
    for each in numbers:

        for each1 in numbers:
            if int(each) + int(each1) == target_sum:
                list.append(count)
                list.append(count1)
                tuple(list)
                return list
            count1 +=1
        count +=1


print(find_two_sum([3, 1, 5, 7, 5, 9], 10))