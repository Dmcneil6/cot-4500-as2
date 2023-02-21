
from assignmnet_2 import * 

# question 1

x_data = [3.6, 3.8, 3.9]
f_data = [1.675, 1.436, 1.318]

# Define the point to interpolate
x_interp = 3.7

# Call the Neville's method function
res = neville_method(x_data, f_data, x_interp)

# Print the result
print("Q1: The 2nd degree interpolating value for f(3.7) is:\n", res)


# question 2 and 3

# Given data
x_data = np.array([7.2, 7.4, 7.5, 7.6])
f_data = np.array([23.5492, 25.3913, 26.8224, 27.4589])

x = 7.3
res = newton_forward_method(x_data, f_data, x)  
print("Difference Table:")
print(res[0])
print("\nQ2 b: Polynomial Coefficients for degrees 1, 2, and 3: ")
print(res[1])
print("\nQ3: approximate f({x}) :")
print(res[2])

#question 4
# given data
x_data = [3.6, 3.8, 3.9]
f_data = [1.675, 1.436, 1.318]
df_data = [-1.195, -1.188, -1.182]

# print divided difference table
print("Q4: Divided difference table:")
table = divided_difference(x_data, f_data)


# print Hermite polynomial approximation matrix
print("Hermite polynomial approximation matrix:")
hermite_matrix(x_data, f_data, df_data)


# question 5
x_data = np.array([2, 5, 8, 10])
f_data = np.array([3, 5, 7, 9])


res = cubic_spline_interpolation(x_data, f_data)

print("Q5: Find" )
print("a. Matrix A:")
print(res[0])
print("\nb. Vector b:")
print(res[1])
print("\nc. Vector x:")
print(res[2])
