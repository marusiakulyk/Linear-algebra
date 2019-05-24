import Linear_regression


def process_data(matrix, y):
    x_ = [[1]+i[1:] for i in matrix]
    vector = [i[0] for i in matrix]
    coef = Linear_regression.lin(x_, vector)
    res = [coef[0]] + Linear_regression.vector_matrix_multip(coef[1:], y)
    res_num = 0
    for i in res: res_num += i
    return res_num
