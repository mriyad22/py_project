"""
Python Program for cube sum of first n natural numbers

Mathematics Formula: Sum of cubes upto n = (n * (n + 1) // 2) ** 2
"""

#Using Mathematical Formula

n = int(input("Enter a number: "))
result = (n * (n + 1) // 2) ** 2
print(f"Sum of the cubes of the first {n} natural numbers: {result}")

#--------------------------------------------------------------------
#Using Brute Force approach

n = int(input("Enter a number: "))
sum = 0

for i in range(1, n + 1):
    sum += i ** 3

print(sum)


#--------------------------------------------------------------------
#Using Generator Expression

"""
A generator expression allows us to generate cubes and 
sum them in a single, memory-efficient line.
"""

n = int(input("Enter a number: "))
result = sum(i**3 for i in range(1, n + 1))

print(result)


#--------------------------------------------------------------------
#Using Enumerate List

n = int(input("Enter a number: "))

res = sum([(i + 1) ** 3 for i, _ in enumerate(range(n))])
print(res)


"""
* enumerate(range(n)): returns pairs (index, value) where:
    index starts from 0
    value is each number from 0 to n-1
* (i + 1) ** 3: gives the cube of each natural number from 1 to n
* sum(): adds up all cubes.
"""