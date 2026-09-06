## Big O

# Big O notation describes how an algorithm's time or space requirements grow 
# as the input size (n) increases. It helps us compare the efficiency of algorithms
# without depending on a specific machine or execution time.

## O(n) — Linear Time

# O(n) means the number of operations grows linearly with the input size.
# Time Complexity: O(n)
# n = 10    → ~10 operations

def print_numbers(numbers):
  for number in range(numbers):
    print(number)

print_numbers(10)
