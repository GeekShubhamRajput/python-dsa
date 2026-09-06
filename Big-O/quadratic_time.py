## O(n²) — Quadratic Time

# O(n²) means the number of operations grows approximately with the square of 
# the input size. It commonly occurs when one loop runs inside another loop.

def print_pairs(number):
  for i in range(number):
    for j in range(number):
      print(i, j)

print_pairs(3)
