#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Get the number of Fibonacci numbers to generate
n = int(input("Enter the number of Fibonacci numbers to generate: "))

# Initialize the first two numbers in the sequence
fibonacci_numbers = [0, 1]

# Generate the Fibonacci numbers
for i in range(2, n):
    next_number = fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2]
    fibonacci_numbers.append(next_number)

# Print the Fibonacci numbers
print("Fibonacci numbers:")
for number in fibonacci_numbers:
    print(number, end=" ")


# In[ ]:




