## Python References vs Pointers

# Python does not have pointers in the same way as C or C++. 
# Instead, Python variables are references to objects.

## Mutable Objects (list, dict, set)
# With mutable objects like lists, two variables can reference the same object:

a = [10, 20, 30]
b = a

b.append(40)

print(a)  # [10, 20, 30, 40]
print(b)  # [10, 20, 30, 40]

print(id(a)) # 139948610001792
print(id(b)) # 139948610001792 

## Immutable Objects (int, float, string, tuple)
# Integers are immutable. When we assign a new value, 
# the variable references a different object instead of modifying the original.

a = 10
b = a

print(a)  # 10
print(b)  # 10

print(id(a)) # 140051262997008
print(id(b)) # 140051262997008

b = 20

print(a)  # 10
print(b)  # 20

print(id(a))  # 140051262997008
print(id(b))  # 140051262997328
