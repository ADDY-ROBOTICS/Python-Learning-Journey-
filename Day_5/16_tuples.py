# Tuples in Python are immutable, meaning their contents cannot be changed after creation.

t1 = (1, 2, 3, 4, 5)
print("Original tuple:", t1)

# To add an element, you must create a new tuple.
t2 = t1 + (6,)
print("After adding 6:", t2)

# To remove an element, you must also create a new tuple.
element_to_remove = 3
t3 = tuple(x for x in t1 if x != element_to_remove)
print("After removing 3:", t3)

# These examples show that tuples cannot be modified directly; any 'change' requires creating a new tuple.


