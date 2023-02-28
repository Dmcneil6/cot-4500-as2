import numpy as np


# Define Neville's method function
def neville_method(x, fx, x_interp):
    n = len(x)
    Q = [[0]*n for _ in range(n)]
    for i in range(n):
        Q[i][0] = fx[i]
    for j in range(1, n):
        for i in range(n-j):
            Q[i][j] = ((x_interp - x[i+j])*Q[i][j-1] + (x[i] - x_interp)*Q[i+1][j-1]) / (x[i] - x[i+j])
    return Q[0][-1]



def newton_forward_method(x_data, f_data, _x):
    # Create the difference table
    n = len(x_data)
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = f_data
    for j in range(1, n):
        for i in range(n-j):
            diff_table[i][j] = (diff_table[i+1][j-1] - diff_table[i][j-1]) / (x_data[i+j] - x_data[i])

    # Print the difference table
    # for row in diff_table:
    #     print(row)

    # Get the polynomial coefficients for degree 1, 2, and 3
    polynomial_coeffs = []
    for i in range(1, 4):
        polynomial_coeffs.append(diff_table[0][i])
    # print("\nQ2 b: Polynomial Coefficients for degrees 1, 2, and 3: ")
    # print(polynomial_coeffs)

    # Given
    x = _x
    # Using polynomial approximation  approximate f(7.3)

    p1 = diff_table[0][0] + (x - x_data[0]) * diff_table[0][1]
    p2 = p1 + (x - x_data[0]) * (x - x_data[1]) * diff_table[0][2]
    f_approx_p3 = p2 + (x - x_data[0]) * (x - x_data[1]) * (x - x_data[2]) * diff_table[0][3]

    return [diff_table, polynomial_coeffs, f_approx_p3]


def print_table(table):
    for row in table:
        print("\t".join("{:.3f}".format(val) if val != 0 else "0." for val in row))

def divided_difference(x, f):
    n = len(x)
    table = [[0] * n for i in range(n)]
    for i in range(n):
        table[i][0] = f[i]
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (x[i + j] - x[i])
    print_table(table)



def hermite_matrix(x, f, df):
    n = len(x)
    m = 2 * n
    table = [[0] * m for i in range(m)]
    for i in range(n):
        table[2 * i][0] = x[i]
        table[2 * i + 1][0] = x[i]
        table[2 * i][1] = f[i]
        table[2 * i + 1][1] = f[i]
        table[2 * i + 1][2] = df[i]
        if i > 0:
            table[2 * i][2] = (table[2 * i][1] - table[2 * i - 1][1]) / (table[2 * i][0] - table[2 * i - 1][0])
    for j in range(3, m):
        for i in range(m - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (table[i + j - 1][0] - table[i][0])
    
    print_table(table)




def cubic_spline_interpolation(x_data, f_data):
    # Create the tridiagonal matrix A
    n = len(x_data)
    A = np.zeros((n, n))
    A[0, 0] = 1
    A[-1, -1] = 1
    for i in range(1, n-1):
        h_i = x_data[i] - x_data[i-1]
        h_i1 = x_data[i+1] - x_data[i]
        A[i, i-1] = h_i
        A[i, i] = 2 * (h_i + h_i1)
        A[i, i+1] = h_i1

    # Create the vector b
    b = np.zeros(n)
    for i in range(1, n-1):
        b[i] = 3 * ((f_data[i+1] - f_data[i]) / (x_data[i+1] - x_data[i]) 
                - (f_data[i] - f_data[i-1]) / (x_data[i] - x_data[i-1]))

    # Solve for the vector x
    x = np.linalg.solve(A, b)

    return[A, b, x]