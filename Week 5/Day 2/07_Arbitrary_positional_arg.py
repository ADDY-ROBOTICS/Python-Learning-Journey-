#Write a Python function that takes any number of positional arguments and returns their sum
def sum_all(*args):
     """This function takes arbitrary numbers of number and provides their sum """
     total = 0
     for num in args:
            total += num
     return total

print(sum_all(1,2,3,4,5))


sum_all()

