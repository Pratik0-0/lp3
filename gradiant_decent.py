#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Function
def f(x):
    return (x + 3) ** 2

# Derivative of function
def gradient(x):
    return 2 * (x + 3)

# Initial values
x = 2
learning_rate = 0.1
iterations = 50

# Gradient Descent
for i in range(iterations):

    x = x - learning_rate * gradient(x)

    print("Iteration:", i + 1,
          "x =", round(x, 6),
          "y =", round(f(x), 6))

print("\nLocal Minimum:")
print("x =", x)
print("y =", f(x))

# x = 3 y = 0


# In[ ]:




