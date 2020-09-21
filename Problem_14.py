"""


Provide an array of n-1 integers in the range of 1 to n with no duplicates in list, One of the integers is missing in the list. Write a code to find the missing integer.

Examples:

Input : arr[] = [1, 2, 3, 5, 6, 7, 8]
Output : 4


Input : arr[] = [1, 2, 4, 5, 6, 7, 8, 9]
Output : 3 


"""

def missing_number(arr):
  n = len(arr) + 1
  s = n *(n+1) // 2
  return s- sum(arr) 


arr = [1, 2, 3, 5, 6, 7, 8]
arr2 = [1, 2, 4, 5, 6, 7, 8, 9]

print(missing_number(arr))
print(missing_number(arr2))

# Complexity : O(n)