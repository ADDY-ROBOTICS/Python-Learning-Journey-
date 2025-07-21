#Write Python code to change the second item in a list named items containing "pen", "book", "ruler" to "notebook" and print the updated list.


stationery = ['pen', 'book', 'ruler', 'notebook']
stationery.insert(1,'eraser')  # Insert 'eraser' at index 2
print(stationery)  # Output: ['pen', 'book', 'eraser',