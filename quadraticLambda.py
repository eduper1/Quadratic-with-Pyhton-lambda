# Creating quadratic function ax^2 + bx + c
def quadratic_function(a, b, c):
    # returns the output of x in f(x) = ax^2 + bx + c
    return lambda x: a*x**2 + b*x + c

# calling function 
func = quadratic_function(2, 3, -5)

# output is -5 where x=0 for line 7
print(func(0))

# output is 0 where x=1 for line 7
print(func(1))

# output is 9 where x=2 for line 7
print(func(2))
