from numpy.linalg import inv


def transpose(matrix):
    outcome = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            outcome[j][i] = matrix[i][j]
    return outcome


def multiplication(matrix1, matrix2):
    outcome = [[0 for i in range(len(matrix2[0]))] for j in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                try:
                    outcome[i][j] += float(round(float(matrix1[i][k]) * float(matrix2[k][j]), 3))
                except ValueError or TypeError:
                    pass
    return outcome


def vector_matrix_multip(matrix, vector):
    results = []
    for i in range(len(matrix)):
        items = 0
        for j in range(len(vector)):
            try:
                items += float(round(float(matrix[i][j]), 3)) * float(round(float(vector[j]), 3))
            except ValueError:
                pass
            except TypeError:
                pass
        results.append(items)
    return results


def lin(X, y):
    transpose1 = transpose(X)
    inverse = inv(multiplication(transpose1, X))
    part = multiplication(inverse, transpose1)
    linear_regression = vector_matrix_multip(part, y)
    return linear_regression
