## O(log n) — Logarithmic Time

# O(log n) means the algorithm reduces the problem size significantly, often by half in each step.
# Always remember: Binary Search requires the input list to be sorted.

def binary_search(numbers, target):
  left = 0
  right = len(numbers) - 1

  while left <= right:
    mid = (left + right)

    if numbers[mid] == target:
      return True
    elif numbers[mid] < target:
      left = mid + 1
    else:
      right = mid - 1

  return False

print(binary_search([3, 4, 5, 6, 7], 3)) # True
