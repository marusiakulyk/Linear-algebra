from numpy.linalg import inv


def transpose(matrix):
    outcome = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            outcome[j][i] = matrix[i][j]
    return outcome


transposed = transpose([[1, 0], [1, 1], [1, 2]])


def multiplication(matrix1, matrix2):
    outcome = [[0 for i in range(len(matrix2[0]))] for j in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                outcome[i][j] += matrix1[i][k] * matrix2[k][j]
    return outcome


x = multiplication(transpose([[1, 0], [1, 1], [1, 2]]), [[1, 0], [1, 1], [1, 2]])

def lin(x, transposed, y):
    inversed = inv(x)

    part = multiplication(inversed, transposed)
    linear_regression = multiplication(part, y)
    return linear_regression
