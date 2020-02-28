def fib(n):
    if n == 0:
        #weird base case to test but ok
        return 0
    elif n == 1: 
        return 1
    return exponentiate_matrix(n-1, [[1,1],[1,0]])[0][0]


def matrix_mult(a, b):
    c_1 = a[0][0]*b[0][0] + a[0][1]*b[0][1]
    c_2 = a[0][0]*b[0][1] + a[0][1]*b[1][1]
    c_3 = a[1][0]*b[0][0] + a[1][1]*b[0][1]
    c_4 = a[1][0]*b[0][1] + a[1][1]*b[1][1]
    return [[c_1,c_2],[c_3,c_4]]


def exponentiate_matrix(power, input_matrix):
    function_matrix = [[1,1],[1,0]]
    if power == 1:
        return function_matrix
    else:
        if power % 2 == 0:
            square_root = exponentiate_matrix(power//2, input_matrix)
            return matrix_mult(square_root, square_root)
        else:
            return matrix_mult(function_matrix, exponentiate_matrix(power - 1, input_matrix))


def fib1_0(n):
    phi = (1+5**0.5)/2
    if n == 0:
        return 0
    else:
        return int((pow(phi, n))/5**0.5)


def fib1_1(n):
    phi = (1+5**0.5)/2
    if n == 0:
        return 0
    else:
        return fast_power(phi, n)/5**0.5


def fib2_1(n):
    phi = (1+5**0.5)/2
    phi_inverse = (1-5**0.5)/2
    if n == 0:
        return 0
    else:
        return (fast_power(phi, n)/2 - fast_power(phi, n)/2)/5**0.5


def fast_power(value, power):
    if power == 1:
        return value
    elif power % 2 == 0:
        return fast_power(value, power//2)**2
    else:
        return value * fast_power(value, power-1)