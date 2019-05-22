import Linear_regression


def process_data(matrix, y):
    coef = Linear_regression.lin(matrix, y)
    res = coef[0] + Linear_regression.vector_matrix_multip(coef[1:], y)
    return res
