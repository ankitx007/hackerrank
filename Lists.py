# Consider a list (list = []). You can perform the following commands:
#
# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
#
# Input Format
#
# The first line contains an integer, , denoting the number of commands.
# Each line  of the  subsequent lines contains one of the commands described above.
#
# Constraints
#
# The elements added to the list must be integers.
# Output Format
#
# For each command of type print, print the list on a new line.
#
# Sample Input 0
#
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
# Sample Output 0
#
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]

N = int(input())
array = []
for i in range(N):
    inputs = input().split()
    if len(inputs) == 3:
        array.insert(int(inputs[1]), int(inputs[2]))
    elif len(inputs) == 2:
        if inputs[0] == "append":
            array.append(int(inputs[1]))
        else:
            array.remove(int(inputs[1]))
    else:
        if inputs[0] == "print":
            print(array)
        elif inputs[0] == "sort":
            array.sort()
        elif inputs[0] == "pop":
            array.pop()
        else:
            array.reverse()
